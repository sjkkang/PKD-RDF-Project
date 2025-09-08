from rdflib import Graph
import pandas as pd
from collections import defaultdict

# RDF file paths
criticism_rdf_path = "criticism_rdf.ttl"
novel_rdf_path = "novel_posthumanism_rdf.ttl"

# Load RDF graphs
criticism_graph = Graph()
novel_graph = Graph()

criticism_graph.parse(criticism_rdf_path, format="turtle")
novel_graph.parse(novel_rdf_path, format="turtle")

print(f"Loaded {len(criticism_graph)} triples from {criticism_rdf_path}")
print(f"Loaded {len(novel_graph)} triples from {novel_rdf_path}")

# Define characters of interest
characters = ["Deckard", "Rachael", "Isidore"]

# Define a dictionary to store interactions
character_analysis = defaultdict(lambda: defaultdict(int))

# Iterate through RDF data and extract ALL interactions for each character
for subj, pred, obj in novel_graph:
    subj_str = str(subj)
    pred_str = str(pred)
    obj_str = str(obj)

    # Check if the subject is a tracked character
    for character in characters:
        character_uri = f"http://example.org/posthuman#{character.replace(' ', '_')}"
        if character_uri in subj_str:
            concept_name = obj_str.split("#")[-1].replace("_", " ")  # Extract readable concept name
            predicate_name = pred_str.split("#")[-1]  # Extract predicate name

            # Count the interactions
            character_analysis[character][concept_name] += 1

# Convert to a structured DataFrame
character_df = []
for character, interactions in character_analysis.items():
    for concept, count in interactions.items():
        character_df.append([character, concept, count])

df_character_analysis = pd.DataFrame(character_df, columns=["Character", "Concept", "Mentions"])

# ----------------------------- #
# 1️⃣ Identify Most Significant Themes Per Character
# ----------------------------- #

df_top_concepts = df_character_analysis.groupby("Character").apply(
    lambda x: x.nlargest(3, "Mentions")
).reset_index(drop=True)

print("\n🔍 Top 3 Themes for Each Character:")
print(df_top_concepts)

# ----------------------------- #
# 2️⃣ Character-Theme Overlap Analysis
# ----------------------------- #

# Create a character-theme matrix for overlap detection
character_theme_matrix = df_character_analysis.pivot(index="Character", columns="Concept", values="Mentions").fillna(0)

# Compute thematic similarity between characters
character_correlation = character_theme_matrix.T.corr()

print("\n🔗 Character-Theme Correlation:")
print(character_correlation)

# ----------------------------- #
# 3️⃣ Save Results to CSV
# ----------------------------- #
df_character_analysis.to_csv("character_analysis.csv", index=False)
df_top_concepts.to_csv("top_character_themes.csv", index=False)
character_correlation.to_csv("character_correlation.csv")

print("\n✅ Analysis complete! Results saved as CSV files.")
