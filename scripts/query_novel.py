import rdflib
from collections import defaultdict
from prettytable import PrettyTable
import csv

def main():
    # 1) RDF Graph 읽기
    g = rdflib.Graph()
    ttl_file = "results/novel_posthumanism_rdf.ttl"
    g.parse(ttl_file, format="turtle")

    EX = rdflib.Namespace("http://example.org/posthuman#")
    g.bind("ex", EX)

    # 2) mention-level 쿼리
    #  ex:subject ?char; ex:predicate ?rel; ex:object ?concept 로 연결된
    #  a ex:Mention 노드에 대해, strugglesWith/linkedTo/questions만 필터링
    query = """
    PREFIX ex: <http://example.org/posthuman#>
    SELECT ?char ?rel ?concept (COUNT(*) as ?relCount)
    WHERE {
      ?m a ex:Mention ;
         ex:subject ?char ;
         ex:predicate ?rel ;
         ex:object ?concept .
      FILTER(?rel IN (ex:strugglesWith, ex:linkedTo, ex:questions))
    }
    GROUP BY ?char ?rel ?concept
    ORDER BY ?char ?rel
    """

    qres = g.query(query)

    # 3) 결과를 저장할 자료구조
    #    => char_dict[charName]["strugglesWith"][conceptName] = count
    char_dict = defaultdict(lambda: {
        "strugglesWith": defaultdict(int),
        "linkedTo": defaultdict(int),
        "questions": defaultdict(int),
    })

    # CSV 출력을 위해 담아둘 리스트
    csv_rows = []

    for row in qres:
        char_uri = row["char"]
        rel_uri = row["rel"]
        concept_uri = row["concept"]
        count_val = int(row["relCount"])

        # http://example.org/posthuman#strugglesWith -> strugglesWith
        relation_str = rel_uri.split("#")[-1]
        # http://example.org/posthuman#Deckard -> Deckard
        char_name = char_uri.split("#")[-1]
        # http://example.org/posthuman#Cyborg_Theory -> Cyborg_Theory
        concept_name = concept_uri.split("#")[-1]

        # 자료구조에 누적
        char_dict[char_name][relation_str][concept_name] += count_val

    # 4) PrettyTable 생성
    table = PrettyTable()
    table.field_names = ["Character", "Struggles With (count)", "Linked To (count)", "Questions (count)"]

    # 5) char_dict를 캐릭터 이름 알파벳순 정렬 후 테이블 한 행씩 생성
    for char_name, rel_map in sorted(char_dict.items()):
        # 각 관계별 (concept, count) 목록을 count 내림차순 정렬
        struggles_items = sorted(rel_map["strugglesWith"].items(), key=lambda x: -x[1])
        linked_items = sorted(rel_map["linkedTo"].items(), key=lambda x: -x[1])
        questions_items = sorted(rel_map["questions"].items(), key=lambda x: -x[1])

        # "Cyborg_Theory (13), Animal_Ethics (7)" 형태로 문자열 변환
        struggles_str = ", ".join(f"{c} ({cnt})" for c, cnt in struggles_items) if struggles_items else "-"
        linked_str = ", ".join(f"{c} ({cnt})" for c, cnt in linked_items) if linked_items else "-"
        questions_str = ", ".join(f"{c} ({cnt})" for c, cnt in questions_items) if questions_items else "-"

        table.add_row([char_name, struggles_str, linked_str, questions_str])

    # 6) PrettyTable 콘솔 출력
    print(table)

    # 7) CSV로 저장
    #    => "Character,Relation,Concept,Count" 형식으로 쭉 나열
    with open("results/mention_counts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Character", "Relation", "Concept", "Count"])

        # char_dict를 다시 순회해서 (char, rel, concept, count) 구조로 출력
        for char_name, rel_map in sorted(char_dict.items()):
            for concept_name, cnt in sorted(rel_map["strugglesWith"].items(), key=lambda x: -x[1]):
                writer.writerow([char_name, "strugglesWith", concept_name, cnt])
            for concept_name, cnt in sorted(rel_map["linkedTo"].items(), key=lambda x: -x[1]):
                writer.writerow([char_name, "linkedTo", concept_name, cnt])
            for concept_name, cnt in sorted(rel_map["questions"].items(), key=lambda x: -x[1]):
                writer.writerow([char_name, "questions", concept_name, cnt])

    print("CSV file saved to results/mention_counts.csv")

if __name__ == "__main__":
    main()
