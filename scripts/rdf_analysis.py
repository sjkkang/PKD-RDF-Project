"""
rdf_analysis.py

This script demonstrates how to load two RDF/Turtle files using rdflib,
execute a SPARQL query, and export character-predicate-concept counts to a CSV file.

Installation:
    pip install rdflib

Directory Structure Assumption:
    /Users/sujinkkang/Dropbox/pkd_rdf_project/results/novel_posthumanism_rdf.ttl
    /Users/sujinkkang/Dropbox/pkd_rdf_project/results/criticism_rdf.ttl
    /Users/sujinkkang/Dropbox/pkd_rdf_project/scripts/rdf_analysis.py
"""

import csv
from rdflib import Graph

def main():
    """
    Main function that loads two Turtle files into one rdflib Graph,
    runs a SPARQL query, and saves the results in a CSV file.
    """

    # 1) Create an rdflib Graph instance
    g = Graph()

    # 2) Absolute paths to the two Turtle files
    novel_ttl = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/novel_posthumanism_rdf.ttl"
    criticism_ttl = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/criticism_rdf.ttl"

    g.parse(novel_ttl, format="turtle")
    g.parse(criticism_ttl, format="turtle")

    # 3) Define the SPARQL query
    #    - Rename (COUNT(*) AS ?count) to (COUNT(*) AS ?cnt) to avoid naming collision.
    query = """
    PREFIX ex: <http://example.org/posthuman#>
    PREFIX char: <http://example.org/characters#>
    PREFIX concept: <http://example.org/concepts#>

    SELECT ?character ?predicate ?concept (COUNT(*) AS ?cnt)
    WHERE {
      ?character ?predicate ?concept .
      FILTER (
        ?predicate IN (
          ex:strugglesWith,
          ex:linkedTo,
          ex:questions
        )
      )
    }
    GROUP BY ?character ?predicate ?concept
    ORDER BY ?character ?predicate ?concept
    """

    # 4) Execute the SPARQL query
    results = g.query(query)

    # 5) Create CSV file
    output_csv = "table5_like_output.csv"
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["character", "predicate", "concept", "count"])

        # 6) Iterate over query results
        for row in results:
            # row.cnt now corresponds to the COUNT(*) we renamed
            # Convert each SPARQL result to string
            character_uri = str(row.character)
            predicate_uri = str(row.predicate)
            concept_uri   = str(row.concept)

            # Convert the count literal to Python and then to string
            count_value   = str(row.cnt.toPython())

            # Optional: Extract local names from URIs
            character_name = character_uri.split('#')[-1] if '#' in character_uri else character_uri
            predicate_name = predicate_uri.split('#')[-1] if '#' in predicate_uri else predicate_uri
            concept_name   = concept_uri.split('#')[-1]   if '#' in concept_uri   else concept_uri

            writer.writerow([character_name, predicate_name, concept_name, count_value])

    print(f"Done! The CSV file '{output_csv}' has been created in the current directory.")

if __name__ == "__main__":
    main()
