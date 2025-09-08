"""
generate_table2.py

This script loads an RDF/Turtle file, extracts character-to-concept relationships,
counts occurrences, and formats the output to match Table 2.

Installation:
    pip install rdflib pandas

Usage:
    Run this script in VS Code terminal:
    python generate_table2.py
"""

import pandas as pd
from rdflib import Graph, Namespace, Literal
from collections import defaultdict

# 📂 File Path (Modify if needed)
rdf_file_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/novel_posthumanism_rdf.ttl"

# ✅ Define the namespace for predicates
ex = Namespace("http://example.org/posthuman#")

# ✅ Define key characters & concepts for Table 2
key_characters = {"Deckard", "Rachael", "Isidore", "Luba_Luft"}
key_concepts = {
    "httpexampleorgposthumanCyborg_Theory": "Cyborg Theory",
    "httpexampleorgposthumanAnimal_Ethics": "Animal Ethics",
    "httpexampleorgposthumanPosthuman_Ethics": "Posthuman Ethics",
    "empathy_box": "Empathy"  # Assuming "empathy_box" represents Empathy
}

# ✅ Define predicates for character-to-concept relationships
target_predicates = {
    "strugglesWith": "Struggles With",
    "linkedTo": "Linked To",
    "questions": "Questions"
}

# ✅ Load RDF File
print(f"📂 Loading RDF file: {rdf_file_path}")
g = Graph()
g.parse(rdf_file_path, format="turtle")

# ✅ Extract relevant triples & count occurrences
character_concept_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

for s, p, o in g:
    predicate_name = str(p).split("#")[-1] if "#" in str(p) else str(p)
    concept_name = str(o).split("#")[-1] if "#" in str(o) else str(o)

    if predicate_name in target_predicates and concept_name in key_concepts:
        character_name = str(s).split("#")[-1] if "#" in str(s) else str(s)
        mapped_predicate = target_predicates[predicate_name]
        mapped_concept = key_concepts[concept_name]

        if character_name in key_characters:
            character_concept_counts[character_name][mapped_predicate][mapped_concept] += 1

# ✅ Convert extracted data to a structured format
table2_data = []

for character, predicates in character_concept_counts.items():
    row = {"Character": character}
    for predicate, concepts in predicates.items():
        for concept, count in concepts.items():
            row[f"{predicate} ({concept})"] = count
    table2_data.append(row)

# ✅ Convert to DataFrame
df_table2 = pd.DataFrame(table2_data)

# ✅ Fill missing values with "-"
df_table2.fillna("-", inplace=True)

# ✅ Sort by character name
df_table2 = df_table2.set_index("Character").reindex(["Deckard", "Rachael", "Isidore", "Luba_Luft"]).reset_index()

# ✅ Display final Table 2 format
print("\n🎯 Final Table 2: Character-to-Concept Mapping\n")
print(df_table2.to_string(index=False))

# ✅ Save as CSV (Optional)
output_csv_path = "/Users/sujinkkang/Dropbox/pkd_rdf_project/results/table2_results.csv"
df_table2.to_csv(output_csv_path, index=False)
print(f"\n✅ Table 2 data saved to: {output_csv_path}")
