from rdflib import Graph
import pandas as pd
from collections import defaultdict

# Load RDF files
criticism_rdf_path = "criticism_rdf.ttl"
novel_rdf_path = "novel_posthumanism_rdf.ttl"

criticism_graph = Graph()
novel_graph = Graph()

criticism_graph.parse(criticism_rdf_path, format="turtle")
novel_graph.parse(novel_rdf_path, format="turtle")

print(f"✅ Loaded {len(criticism_graph)} triples from {criticism_rdf_path}")
print(f"✅ Loaded {len(novel_graph)} triples from {novel_rdf_path}")

# ----------------------------- #
# 1️⃣ Extract Character-Concept Interactions (Fixing Count Issues)
# ----------------------------- #

# Define relationships to track
relationship_types = {
    "linkedTo": "http://example.org/posthuman#linkedTo",
    "strugglesWith": "http://example.org/posthuman#strugglesWith",
    "questions": "http://example.org/posthuman#questions"
}

# Define key characters and their possible name variants
characters_of_interest = {
    "Deckard": ["Deckard", "Rick_Deckard", "Rick"],
    "Rachael": ["Rachael", "Rachael_Rosens"],
    "Isidore": ["Isidore", "John_Isidore"],
    "Luba_Luft": ["Luba_Luft"]
}

# Dictionary to store character interactions
character_interactions = defaultdict(lambda: defaultdict(int))

# Function to clean concept URIs
def clean_concept_uri(uri):
    return uri.replace("http://example.org/posthuman#", "").replace("_", " ")

# Iterate through RDF data and count interactions
for subj, pred, obj in novel_graph:
    subj_str = str(subj)
    pred_str = str(pred)
    obj_str = clean_concept_uri(str(obj))  # Fix concept name formatting

    # Check if the subject matches any character variant
    for character, variants in characters_of_interest.items():
        if any(f"http://example.org/posthuman#{variant}" in subj_str for variant in variants):
            for rel_type, rel_uri in relationship_types.items():
                if rel_uri in pred_str:
                    character_interactions[character][(rel_type, obj_str)] += 1

# ----------------------------- #
# 2️⃣ Convert Data into Structured Format
# ----------------------------- #

# Convert to DataFrame
interaction_data = []
for character, interactions in character_interactions.items():
    for (relation, concept), count in interactions.items():
        interaction_data.append([character, relation, concept, count])

df_character_interactions = pd.DataFrame(interaction_data, columns=["Character", "Relation", "Concept", "Count"])

# ----------------------------- #
# 3️⃣ Identify Key Interaction Patterns
# ----------------------------- #

# Extract the most significant interactions per character
df_top_interactions = df_character_interactions.groupby("Character").apply(
    lambda x: x.nlargest(3, "Count")
).reset_index(drop=True)

# Print analysis summary
print("\n🔍 Most Frequent Character-Concept Interactions:")
print(df_top_interactions)

# ----------------------------- #
# 4️⃣ Save Results to CSV
# ----------------------------- #

df_character_interactions.to_csv("fixed_character_concept_analysis.csv", index=False)
df_top_interactions.to_csv("fixed_top_character_interactions.csv", index=False)

print("\n✅ Fixed Analysis complete! Results saved to 'fixed_character_concept_analysis.csv' and 'fixed_top_character_interactions.csv'.")
