import matplotlib
matplotlib.use('Agg')  # GUI 없이 이미지 저장

import rdflib
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import unicodedata

# 폰트 설정
plt.rcParams['font.family'] = 'Arial'  # 시스템에서 지원하는 폰트 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 제어문자 및 특수문자 제거 함수
def clean_text(text):
    """제어문자 및 특수문자 제거"""
    return ''.join(c for c in text if unicodedata.category(c)[0] != 'C')  # C = Control Character

# RDF 파일 로드
rdf_file_path = "results/criticism_rdf.ttl"
g = rdflib.Graph()
g.parse(rdf_file_path, format="turtle")

# NetworkX 그래프 생성
G = nx.DiGraph()

for subj, pred, obj in g:
    subj_clean = clean_text(str(subj))
    obj_clean = clean_text(str(obj))
    pred_clean = clean_text(str(pred).split("#")[-1])
    G.add_edge(subj_clean, obj_clean, label=pred_clean)

# Matplotlib을 이용한 정적 그래프 시각화
def draw_static_graph():
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    edges = G.edges(data=True)

    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)
    edge_labels = {(u, v): d["label"] for u, v, d in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("RDF 기반 지식 그래프")
    plt.savefig("rdf_graph.png")
    print("정적 그래프가 rdf_graph.png 파일로 저장되었습니다.")

# Pyvis를 이용한 인터랙티브 웹 시각화
def draw_interactive_graph():
    net = Network(notebook=False, directed=True)

    for subj, pred, obj in g:
        subj_clean = clean_text(str(subj))
        obj_clean = clean_text(str(obj))
        pred_clean = clean_text(str(pred).split("#")[-1])
        net.add_node(subj_clean, label=subj_clean, color="lightblue")
        net.add_node(obj_clean, label=obj_clean, color="lightgreen")
        net.add_edge(subj_clean, obj_clean, title=pred_clean)

    output_file = "rdf_knowledge_graph.html"
    net.show(output_file)
    print(f"웹 기반 지식 그래프가 생성되었습니다: {output_file}")

# 실행 옵션 선택
if __name__ == "__main__":
    print("실행 옵션 선택:")
    print("1. Matplotlib을 이용한 정적 그래프")
    print("2. Pyvis를 이용한 웹 기반 인터랙티브 그래프")
    
    option = input("옵션을 선택하세요 (1/2): ").strip()
    
    if option == "1":
        draw_static_graph()
    elif option == "2":
        draw_interactive_graph()
    else:
        print("올바른 옵션을 선택하세요!")