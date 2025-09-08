import os
import rdflib
import spacy
import torch
from urllib.parse import quote
from sentence_transformers import SentenceTransformer, util
from collections import defaultdict
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from safetensors.torch import load_file  

# =============================================================================
# 1) Define Relative Paths Using os.path.join()
# =============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "../models/posthuman_finetuned")
RDF_OUTPUT_PATH = os.path.join(BASE_DIR, "../results/novel_posthumanism_rdf_fixed.ttl")
CRITICISM_RDF_PATH = os.path.join(BASE_DIR, "../results/criticism_rdf_fixed.ttl")
NOVEL_TEXT_PATH = os.path.join(BASE_DIR, "../data/primary_text.txt")

# =============================================================================
# 2) Initialize RDF Graph and Namespace
# =============================================================================
g = rdflib.Graph()
EX = rdflib.Namespace("http://example.org/posthuman#")

# =============================================================================
# 3) Load NLP and AI Models
# =============================================================================
print("Loading models...")
nlp = spacy.load("en_core_web_sm")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH, local_files_only=True)

# If a safetensors file exists, load it explicitly
safetensors_path = os.path.join(MODEL_PATH, "model.safetensors")
if os.path.exists(safetensors_path):
    weights = load_file(safetensors_path)
    model.load_state_dict(weights)
model.eval()
print("✅ Models loaded successfully.")

# =============================================================================
# 4) Load and Debug Criticism RDF
# =============================================================================
criticism_graph = rdflib.Graph()
criticism_graph.parse(CRITICISM_RDF_PATH, format="turtle")
print(f"✅ Loaded {len(criticism_graph)} triples from Criticism RDF.")

# Debug: Print first 10 triples from the criticism RDF
print("\n🔍 Sample Criticism RDF Triples:")
for i, (s, p, o) in enumerate(criticism_graph):
    print(s, p, o)
    if i >= 9:  # Show only 10 triples for debugging
        break

# Extract critical concepts and associated text from Criticism RDF
query = """
SELECT DISTINCT ?concept ?text WHERE {
    ?concept ?p ?text .
    FILTER (
        ?p IN (
            <http://example.org/posthuman#hasCriticism>,
            <http://example.org/posthuman#hasDefinition>,
            <http://example.org/posthuman#hasReference>,
            <http://example.org/posthuman#hasExample>
        )
    )
}
"""

criticism_data = {}
for row in criticism_graph.query(query):
    concept_uri = str(row[0])
    text_val = str(row[1])
    if concept_uri in criticism_data:
        criticism_data[concept_uri].append(text_val)
    else:
        criticism_data[concept_uri] = [text_val]

if not criticism_data:
    print("⚠ Warning: No concept data extracted from Criticism RDF. Verify its contents!")
    criticism_data_empty = True
else:
    criticism_data_empty = False
    print(f"✅ Extracted {len(criticism_data)} concepts from Criticism RDF.")

# Precompute concept embeddings if data is available
concept_embeddings = {c: embedding_model.encode(c) for c in criticism_data.keys()} if not criticism_data_empty else {}

# =============================================================================
# 5) Helper Functions
# =============================================================================
def safe_uri(text):
    """Convert text to a valid RDF URI using the EX namespace."""
    text = text.strip().replace(" ", "_")
    text = "".join(c for c in text if c.isalnum() or c == "_")
    return rdflib.URIRef(EX + quote(text))

def predict_text(text):
    """Predict if a passage is relevant to posthumanism using DistilBERT."""
    inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    return torch.argmax(logits, dim=1).item() == 1

def infer_concept(text):
    """
    Infer the most relevant concept from criticism data using Sentence-BERT.
    If criticism data is empty, return a fallback concept.
    """
    text_embedding = embedding_model.encode(text)
    if criticism_data_empty or not concept_embeddings:
        print("⚠ No concept mapping found, returning fallback concept.")
        return None  # Do not return an artificial concept
    
    best_concept_uri = max(
        criticism_data.keys(),
        key=lambda c: util.pytorch_cos_sim(text_embedding, concept_embeddings[c]).item()
    )
    return safe_uri(best_concept_uri)

def extract_named_entities(text):
    """Extract named entities and classify them into humans, androids, animals, and locations."""
    doc = nlp(text)
    entities = {"humans": [], "androids": [], "animals": [], "locations": []}
    lower_text = text.lower()
    for ent in doc.ents:
        ent_uri = safe_uri(ent.text)
        if ent.label_ == "PERSON":
            if "android" in lower_text or "replicant" in lower_text:
                entities["androids"].append(ent_uri)
            else:
                entities["humans"].append(ent_uri)
        elif ent.label_ == "ANIMAL":
            entities["animals"].append(ent_uri)
        elif ent.label_ in ["GPE", "LOC"]:
            entities["locations"].append(ent_uri)
    return entities

def assign_relationship(character, text, concept_uri):
    """
    Assign a relationship between a character and a concept based on textual cues.
    Uses keywords to choose between exemplifies, strugglesWith, questions, or linkedTo.
    """
    lower_text = text.lower()
    if "exemplify" in lower_text or "represent" in lower_text or "demonstrate" in lower_text:
        predicate = "exemplifies"
    elif "struggle" in lower_text or "conflict" in lower_text or "resist" in lower_text:
        predicate = "strugglesWith"
    elif "question" in lower_text or "doubt" in lower_text or "uncertain" in lower_text:
        predicate = "questions"
    else:
        predicate = "linkedTo"
    g.add((character, EX[predicate], concept_uri))

# =============================================================================
# 6) Process Novel Text and Build RDF Triples
# =============================================================================
if not os.path.exists(NOVEL_TEXT_PATH):
    print("❌ Error: Novel text file does not exist.")
    exit(1)

with open(NOVEL_TEXT_PATH, "r", encoding="utf-8") as file:
    novel_text_lines = file.readlines()

for i, line in enumerate(novel_text_lines):
    line = line.strip()
    if not line:
        continue

    # Use the AI model to filter for posthumanism-relevant passages
    if not predict_text(line):
        continue

    # Infer the most relevant concept for the passage
    main_concept_uri = infer_concept(line)
    if not main_concept_uri:  # Skip adding triples if no valid concept was found
        continue

    # Create a unique node for the passage (to allow frequency counts)
    passage_node = safe_uri(f"passage_{i}")
    g.add((main_concept_uri, EX["isMentionedIn"], passage_node))

    # Extract named entities from the passage
    entities = extract_named_entities(line)

    # Link each entity to the inferred concept using context-sensitive relationships
    for human in entities["humans"]:
        assign_relationship(human, line, main_concept_uri)
    for android in entities["androids"]:
        g.add((android, EX["strugglesWith"], main_concept_uri))
    for animal in entities["animals"]:
        g.add((animal, EX["symbolizes"], main_concept_uri))
    for loc in entities["locations"]:
        g.add((loc, EX["contextualizes"], main_concept_uri))

# =============================================================================
# 7) Serialize Final RDF
# =============================================================================
g.serialize(destination=RDF_OUTPUT_PATH, format="turtle")
print(f"✅ Fixed RDF stored at {RDF_OUTPUT_PATH}")
