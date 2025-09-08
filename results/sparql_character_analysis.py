from rdflib import Graph
import pandas as pd

# Load RDF datasets
criticism_rdf_path = "criticism_rdf.ttl"
novel_rdf_path = "novel_posthumanism_rdf.ttl"

criticism_graph = Graph()
novel_graph = Graph()

criticism_graph.parse(criticism_rdf_path, format="turtle")
novel_graph.parse(novel_rdf_path, format="turtle")

print(f"✅ Loaded {len(criticism_graph)} triples from {criticism_rdf_path}")
print(f"✅ Loaded {len(novel_graph)} triples from {novel_rdf_path}")

# ----------------------------- #
# 1️⃣ SPARQL Query: Extract Character-Concept Interactions
# ----------------------------- #

sparql_character_query = """
SELECT ?character ?relation ?concept (COUNT(?concept) AS ?count)
WHERE {
  ?character ?relation ?concept .
  FILTER (?relation IN (
    <http://example.org/posthuman#linkedTo>, 
    <http://example.org/posthuman#strugglesWith>, 
    <http://example.org/posthuman#questions>
  ))
}
GROUP BY ?character ?relation ?concept
ORDER BY ?character ?relation DESC(?count)
"""

# Execute SPARQL query on the novel RDF dataset
query_results = novel_graph.query(sparql_character_query)

# Process query results into a structured DataFrame
character_interactions = []
for row in query_results:
    character = str(row[0]).split("#")[-1]  # Extract character name
    relation = str(row[1]).split("#")[-1]  # Extract relationship type
    concept = str(row[2]).split("#")[-1].replace("_", " ")  # Extract concept name
    count = int(row[3])

    character_interactions.append([character, relation, concept, count])

df_character_analysis = pd.DataFrame(character_interactions, columns=["Character", "Relation", "Concept", "Count"])

# ----------------------------- #
# 2️⃣ SPARQL Query: Find Alternative Names for Cyborg Theory
# ----------------------------- #

sparql_alternate_names = """
SELECT ?concept ?relatedConcept
WHERE {
  ?concept <http://example.org/posthuman#relatedTo> ?relatedConcept .
  FILTER (CONTAINS(LCASE(STR(?concept)), "cyborg_theory"))
}
"""

query_alternate_names = novel_graph.query(sparql_alternate_names)

# Extract alternate concept names
alternate_names = {str(row[1]).split("#")[-1].replace("_", " ") for row in query_alternate_names}

print("\n🔍 Alternate Names for 'Cyborg Theory':", alternate_names)

# ----------------------------- #
# 3️⃣ Identify Top Interactions for Each Character
# ----------------------------- #

df_top_concepts = df_character_analysis.groupby("Character", group_keys=False).apply(
    lambda x: x.nlargest(3, "Count")
).reset_index(drop=True)

print("\n🔍 Most Frequent Character-Concept Interactions:")
print(df_top_concepts)

# ----------------------------- #
# 4️⃣ Compute Character-Thematic Similarity
# ----------------------------- #

# Create a character-theme matrix for correlation analysis
df_character_aggregated = df_character_analysis.groupby(["Character", "Concept"], as_index=False)["Count"].sum()
character_theme_matrix = df_character_aggregated.pivot(index="Character", columns="Concept", values="Count").fillna(0)

# Compute thematic similarity between characters
character_correlation = character_theme_matrix.T.corr()

print("\n🔗 Character-Theme Correlation:")
print(character_correlation)

# ----------------------------- #
# 5️⃣ Save Results to CSV
# ----------------------------- #

df_character_analysis.to_csv("sparql_character_analysis.csv", index=False)
df_top_concepts.to_csv("sparql_top_character_themes.csv", index=False)
character_correlation.to_csv("sparql_character_correlation.csv")

print("\n✅ SPARQL Analysis Complete! Results saved as CSV files.")
