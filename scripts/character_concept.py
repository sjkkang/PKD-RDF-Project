import rdflib
from collections import defaultdict
from prettytable import PrettyTable

def main():
    g = rdflib.Graph()

    # 파일 경로를 results 폴더 내로 변경
    ttl_file = "results/novel_posthumanism_rdf.ttl"
    g.parse(ttl_file, format="turtle")

    EX = rdflib.Namespace("http://example.org/posthuman#")
    g.bind("ex", EX)

    query = """
    PREFIX ex: <http://example.org/posthuman#>
    SELECT ?char ?rel ?concept (COUNT(*) as ?relCount)
    WHERE {
      ?char ?rel ?concept .
      FILTER(?rel IN (ex:strugglesWith, ex:linkedTo, ex:questions))
    }
    GROUP BY ?char ?rel ?concept
    ORDER BY ?char ?rel
    """

    qres = g.query(query)

    char_dict = defaultdict(lambda: {
        "strugglesWith": defaultdict(int),
        "linkedTo": defaultdict(int),
        "questions": defaultdict(int),
    })

    for row in qres:
        char_uri = row["char"]
        rel_uri = row["rel"]
        concept_uri = row["concept"]
        count_val = int(row["relCount"])

        relation_str = rel_uri.split("#")[-1]
        char_name = char_uri.split("#")[-1]
        concept_name = concept_uri.split("#")[-1]

        char_dict[char_name][relation_str][concept_name] += count_val

    table = PrettyTable()
    table.field_names = ["Character", "Struggles With (count)", "Linked To (count)", "Questions (count)"]

    for char_name, relations_map in sorted(char_dict.items()):
        struggles_items = sorted(relations_map["strugglesWith"].items(), key=lambda x: -x[1])
        linked_items = sorted(relations_map["linkedTo"].items(), key=lambda x: -x[1])
        questions_items = sorted(relations_map["questions"].items(), key=lambda x: -x[1])

        struggles_str = ", ".join([f"{c} ({cnt})" for c, cnt in struggles_items]) if struggles_items else "-"
        linked_str = ", ".join([f"{c} ({cnt})" for c, cnt in linked_items]) if linked_items else "-"
        questions_str = ", ".join([f"{c} ({cnt})" for c, cnt in questions_items]) if questions_items else "-"

        table.add_row([char_name, struggles_str, linked_str, questions_str])

    print(table)

if __name__ == "__main__":
    main()
