import rdflib
import pandas as pd
import os

# Define paths relative to this script’s location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CRITICISM_RDF_PATH = os.path.join(BASE_DIR, "../results/criticism_rdf_fixed.ttl")
NOVEL_RDF_PATH = os.path.join(BASE_DIR, "../results/novel_posthumanism_rdf_fixed.ttl")

# Load the RDF graphs
criticism_graph = rdflib.Graph()
novel_graph = rdflib.Graph()

print("Loading Criticism RDF from:", CRITICISM_RDF_PATH)
criticism_graph.parse(CRITICISM_RDF_PATH, format="turtle")
print(f"Loaded {len(criticism_graph)} triples from Criticism RDF.")

print("Loading Novel RDF from:", NOVEL_RDF_PATH)
novel_graph.parse(NOVEL_RDF_PATH, format="turtle")
print(f"Loaded {len(novel_graph)} triples from Novel RDF.")

# SPARQL query to count concept mentions using the isMentionedIn predicate
query = """
SELECT ?concept (COUNT(?ref) AS ?mentionCount)
WHERE {
  ?concept <http://example.org/posthuman#isMentionedIn> ?ref .
}
GROUP BY ?concept
ORDER BY DESC(?mentionCount)
"""

# Query the criticism RDF
print("\nQuerying concept counts for Criticism RDF...")
criticism_counts = criticism_graph.query(query)
criticism_data = {}
for row in criticism_counts:
    # Extract the local name of the concept and convert underscores to spaces for readability
    concept = str(row[0]).split("#")[-1].replace("_", " ")
    # Skip any fallback concept
    if concept.lower() == "unknown concept":
        continue
    count = int(row[1])
    criticism_data[concept] = count

# Query the novel RDF
print("Querying concept counts for Novel RDF...")
novel_counts = novel_graph.query(query)
novel_data = {}
for row in novel_counts:
    concept = str(row[0]).split("#")[-1].replace("_", " ")
    if concept.lower() == "unknown concept":
        continue
    count = int(row[1])
    novel_data[concept] = count

# Merge the data from both RDFs into one table
all_concepts = set(criticism_data.keys()).union(set(novel_data.keys()))
merged_data = []
for concept in all_concepts:
    crit_count = criticism_data.get(concept, 0)
    novel_count = novel_data.get(concept, 0)
    merged_data.append((concept, crit_count, novel_count))

df_table4 = pd.DataFrame(merged_data, columns=["Concept", "Criticism Mentions", "Novel Mentions"])
df_table4 = df_table4.sort_values(by="Criticism Mentions", ascending=False)

print("\n=== Table 4: Concept Mentions Comparison ===")
print(df_table4)

# Save the table to a CSV file for further analysis or visualization
output_csv = os.path.join(BASE_DIR, "../results/analysis_table4.csv")
df_table4.to_csv(output_csv, index=False)
print(f"\n✅ Analysis complete! Table 4 saved to {output_csv}")
