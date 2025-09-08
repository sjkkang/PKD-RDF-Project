import os
import re
import rdflib
import torch
import spacy
import nltk
from urllib.parse import quote
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from sentence_transformers import SentenceTransformer, util
from collections import defaultdict
from nltk.corpus import wordnet
from rapidfuzz import fuzz
from rdflib.namespace import RDFS

########################################################
# ✅ 1) Load Models & Initialize RDF Graph
########################################################

print("Loading AI models...")
MODEL_PATH = "models/posthuman_finetuned"
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

nlp = spacy.load("en_core_web_sm")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
print("✅ Models loaded.")

# ✅ RDF Graph
g = rdflib.Graph()
EX = rdflib.Namespace("http://example.org/posthuman#")

########################################################
# ✅ 2) Define Posthumanist Concepts (Fix for Missing `concepts`)
########################################################

concepts = {
    "Posthumanism": {
        "definition": "A perspective that challenges fixed notions of ‘the human,’ emphasizing the fluidity of human identity."
    },
    "Cyborg Theory": {
        "definition": "A framework that examines human-machine hybrids and their implications for identity and agency."
    },
    "Animal Ethics": {
        "definition": "A philosophical discussion regarding the moral and ethical considerations of non-human animals."
    },
    "Posthuman Ethics": {
        "definition": "An ethical framework that moves beyond human-centric perspectives, emphasizing relational ontology."
    },
    "Hybrid Identity": {
        "definition": "A concept exploring the merged identities between humans, machines, and non-human entities."
    },
    "Technoanimalism": {
        "definition": "A critique of the separation between human rationality and nonhuman behavior, inspired by posthuman thought."
    },
    "Networked Affect": {
        "definition": "A theory describing how emotions are shaped and circulated through digital networks and technological infrastructures."
    },
}

########################################################
# ✅ 3) Helper Functions
########################################################

def safe_uri(text):
    """Convert text to a valid URI format."""
    text = text.strip().replace(" ", "_")
    text = "".join(c for c in text if c.isalnum() or c == "_")
    return rdflib.URIRef(EX + quote(text))

def predict_text(text):
    """Use DistilBERT to predict if a text is posthumanism-related."""
    inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    return torch.argmax(logits, dim=1).item() == 1

def infer_relationships(concept_uris, text):
    """Use AI embeddings to determine relationships between concepts."""
    relationships = []
    text_embedding = embedding_model.encode(text)
    
    concept_pairs = [(concept_uris[i], concept_uris[j]) for i in range(len(concept_uris)) for j in range(i+1, len(concept_uris))]

    for c1, c2 in concept_pairs:
        c1_emb = embedding_model.encode(str(c1))
        c2_emb = embedding_model.encode(str(c2))
        similarity_score = util.pytorch_cos_sim(c1_emb, c2_emb).item()

        if similarity_score > 0.8:
            relationships.append((c1, EX["relatedTo"], c2))
        elif "criticize" in text or "challenge" in text:
            relationships.append((c1, EX["criticizes"], c2))
        elif "influence" in text or "impact" in text:
            relationships.append((c1, EX["hasInfluenceOn"], c2))
        elif "extend" in text or "expand" in text:
            relationships.append((c1, EX["extends"], c2))
        else:
            relationships.append((c1, EX["relatedTo"], c2))  # Default
        
    return relationships

########################################################
# ✅ 4) Process Criticism Texts
########################################################

criticism_dir = "data"
criticism_files = [f for f in os.listdir(criticism_dir) if f.startswith("c-") and f.endswith(".txt")]

print("Processing criticism files...")
for filename in criticism_files:
    file_path = os.path.join(criticism_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # ✅ Check if text is relevant using AI
    if not predict_text(text):
        continue  

    # ✅ Extract candidate concepts
    doc = nlp(text)
    candidate_phrases = set(ent.text for ent in doc.ents) | set(chunk.text for chunk in doc.noun_chunks)

    # ✅ Map concepts using AI embeddings
    mapped_concepts = []
    for phrase in candidate_phrases:
        phrase_emb = embedding_model.encode(phrase)
        best_match = max(concepts.keys(), key=lambda c: util.pytorch_cos_sim(phrase_emb, embedding_model.encode(concepts[c]["definition"])).item())

        if util.pytorch_cos_sim(phrase_emb, embedding_model.encode(concepts[best_match]["definition"])).item() > 0.75:
            mapped_concepts.append(best_match)

    # ✅ Add relationships to RDF
    concept_uris = [safe_uri(c) for c in mapped_concepts]
    for c_uri in concept_uris:
        g.add((c_uri, EX["isMentionedIn"], safe_uri(filename.replace(".txt", ""))))

    relationships = infer_relationships(concept_uris, text)
    for (subj, pred, obj) in relationships:
        g.add((subj, pred, obj))

    print(f"✅ Processed {filename}, extracted {len(mapped_concepts)} concepts.")

########################################################
# ✅ 5) Serialize RDF
########################################################

rdf_output_path = "results/criticism_rdf_fixed.ttl"
g.serialize(destination=rdf_output_path, format="turtle")
print(f"✅ Fixed RDF stored at {rdf_output_path}")
