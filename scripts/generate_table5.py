"""
generate_table5.py

This script queries the updated RDF/Turtle files to extract Table 5-style results.
It runs a SPARQL query on the RDF files and exports the results to a structured CSV format.
"""

import csv
from rdflib import Graph

# 📂 Paths to updated RDF files
updated_novel_ttl_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/updated_novel_posthumanism_rdf.ttl"
updated_criticism_ttl_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/updated_criticism_rdf.ttl"

# 📂 Output CSV file
output_csv_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/table5_results.csv"

# Initialize graph
g = Graph()
g.parse(updated_novel_ttl_path, format="turtle")
g.parse(updated_criticism_ttl_path, format="turtle")

# Define SPARQL Query
query = """
PREFIX ex: <http://example.org/posthuman#>
PREFIX char: <http://example.org/characters#>
PREFIX concept: <http://example.org/concepts#>

SELECT ?character ?predicate ?concept (SUM(?occ) AS ?total_count)
WHERE {
  ?character ?predicate ?concept .
  ?character ex:occurrenceCount ?occ .
}
GROUP BY ?character ?predicate ?concept
ORDER BY DESC(?total_count)
"""

# Execute SPARQL query
results = g.query(query)

# Save results to CSV
with open(output_csv_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["character", "predicate", "concept", "total_count"])

    for row in results:
        character_uri = str(row.character)
        predicate_uri = str(row.predicate)
        concept_uri   = str(row.concept)
        total_count   = str(row.total_count.toPython())

        # Extract the local names from URIs
        character_name = character_uri.split('#')[-1] if '#' in character_uri else character_uri
        predicate_name = predicate_uri.split('#')[-1] if '#' in predicate_uri else predicate_uri
        concept_name   = concept_uri.split('#')[-1]   if '#' in concept_uri   else concept_uri

        writer.writerow([character_name, predicate_name, concept_name, total_count])

print(f"✅ Table 5 results saved to: {output_csv_path}")
