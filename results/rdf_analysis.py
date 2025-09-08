from rdflib import Graph
import pandas as pd

# RDF file paths (Ensure the files are in the same directory)
criticism_rdf_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/criticism_rdf.ttl"
novel_rdf_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/novel_posthumanism_rdf.ttl"


# Load RDF graphs
criticism_graph = Graph()
novel_graph = Graph()

criticism_graph.parse(criticism_rdf_path, format="turtle")
novel_graph.parse(novel_rdf_path, format="turtle")

print(f"Loaded {len(criticism_graph)} triples from {criticism_rdf_path}")
print(f"Loaded {len(novel_graph)} triples from {novel_rdf_path}")

# -------------------------------- #
# 1. Counting Concept Mentions
# -------------------------------- #

# Define the concepts to analyze
concepts_to_verify = [
    "Cyborg Theory",
    "Posthumanism",
    "Animal Ethics",
    "Posthuman Ethics",
    "PostAnthropocentrism",
    "Critical Posthumanism"
]

# Count occurrences of each concept in the criticism dataset (as a subject)
criticism_counts = {concept: 0 for concept in concepts_to_verify}
for subj, pred, obj in criticism_graph:
    for concept in concepts_to_verify:
        if concept.replace(" ", "_") in str(subj):  # Checking if the concept appears as a subject
            criticism_counts[concept] += 1

# Count occurrences of each concept in the novel dataset (as an object)
novel_counts = {concept: 0 for concept in concepts_to_verify}
for subj, pred, obj in novel_graph:
    for concept in concepts_to_verify:
        concept_uri = f"http://example.org/posthuman#{concept.replace(' ', '_')}"
        adjusted_uri = f"http://example.org/posthuman#httpexampleorgposthuman{concept.replace(' ', '_')}"
        
        # Check if the concept appears as an object with correct or incorrect URI format
        if concept_uri in str(obj) or adjusted_uri in str(obj):
            novel_counts[concept] += 1

# -------------------------------- #
# 2. Organizing and Displaying Results
# -------------------------------- #

# Create a DataFrame to compare concept mentions in both datasets
df_verification = pd.DataFrame({
    "Concept": concepts_to_verify,
    "Criticism Mentions": [criticism_counts[concept] for concept in concepts_to_verify],
    "Novel Mentions": [novel_counts[concept] for concept in concepts_to_verify]
})

# Print results in a structured format
print("\nFinal Concept Mentions Analysis:")
print(df_verification)

# -------------------------------- #
# 3. Save Results to CSV
# -------------------------------- #
df_verification.to_csv("concept_mentions_analysis.csv", index=False)
print("\nAnalysis complete: Results saved to 'concept_mentions_analysis.csv'.")
