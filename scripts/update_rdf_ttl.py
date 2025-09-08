"""
update_rdf_ttl.py

This script loads two RDF/Turtle files, counts occurrences of each (subject, predicate, object) triple,
and updates the files by adding an 'ex:occurrenceCount' property using RDF reification.

Installation:
    pip install rdflib

Usage:
    Run this script in VS Code terminal:
    python update_rdf_ttl.py
"""

from rdflib import Graph, Namespace, Literal, RDF, BNode
from collections import defaultdict

# 📂 File paths (Modify if needed)
base_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/"
novel_ttl_path = base_path + "novel_posthumanism_rdf.ttl"
criticism_ttl_path = base_path + "criticism_rdf.ttl"

# 📂 Output file paths (Updated RDF files)
updated_novel_ttl_path = base_path + "updated_novel_posthumanism_rdf.ttl"
updated_criticism_ttl_path = base_path + "updated_criticism_rdf.ttl"

# Define the namespace for RDF reification and custom properties
ex = Namespace("http://example.org/posthuman#")

def process_ttl_file(input_path, output_path):
    """
    Reads an RDF Turtle file, counts occurrences of each (subject, predicate, object) triple,
    and writes a new Turtle file with 'ex:occurrenceCount' added using RDF reification.
    """
    print(f"📂 Processing: {input_path}")

    # 1️⃣ Load the RDF file
    g = Graph()
    g.parse(input_path, format="turtle")

    # 2️⃣ Count occurrences of each (subject, predicate, object) triple
    triple_counts = defaultdict(int)
    for s, p, o in g:
        triple_counts[(s, p, o)] += 1

    # 3️⃣ Create a new graph and copy original triples
    new_g = Graph()
    new_g += g  # Keep existing triples

    # 4️⃣ Add RDF reification for occurrence count
    for (s, p, o), count in triple_counts.items():
        statement = BNode()  # Create a blank node to store metadata
        new_g.add((statement, RDF.subject, s))
        new_g.add((statement, RDF.predicate, p))
        new_g.add((statement, RDF.object, o))
        new_g.add((statement, ex.occurrenceCount, Literal(count)))

    # 5️⃣ Save the updated RDF file
    new_g.serialize(destination=output_path, format="turtle")

    print(f"✅ Updated RDF file saved: {output_path}\n")

# 📌 Process both RDF files and update them
process_ttl_file(novel_ttl_path, updated_novel_ttl_path)
process_ttl_file(criticism_ttl_path, updated_criticism_ttl_path)

print("🎉 All RDF files have been updated with ex:occurrenceCount!")
