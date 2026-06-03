import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Criando o grafo
G = nx.Graph()

vertices = [
    "FIB",
    "Centro",
    "Confianca Castelo",
    "Duque",
    "Nuno",
    "Boulevard"
]

G.add_nodes_from(vertices)

# Arestas com pesos
G.add_edge("FIB", "Centro", weight=13)
G.add_edge("Centro", "Boulevard", weight=9)

G.add_edge("FIB", "Confianca Castelo", weight=8)
G.add_edge("Confianca Castelo", "Boulevard", weight=12)

G.add_edge("FIB", "Duque", weight=14)
G.add_edge("Duque", "Boulevard", weight=11)

G.add_edge("FIB", "Nuno", weight=16)
G.add_edge("Nuno", "Boulevard", weight=12)

# Posições
pos = {
    "FIB": (0, 0),
    "Centro": (3.5, 3),
    "Confianca Castelo": (2, 1),
    "Duque": (3, -1),
    "Nuno": (3, -3),
    "Boulevard": (5, 0)
}

# DIJKSTRA
menor_caminho = nx.dijkstra_path(
    G,
    source="FIB",
    target="Boulevard",
    weight="weight"
)

# Transformar caminho em arestas
arestas_dijkstra = list(zip(
    menor_caminho,
    menor_caminho[1:]
))

# BFS
caminho_bfs = nx.shortest_path(
    G,
    source="FIB",
    target="Boulevard"
)

arestas_bfs = list(zip(
    caminho_bfs,
    caminho_bfs[1:]
))


# DESENHO
plt.figure(figsize=(10, 6))

# Grafo base
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    font_size=9,
    node_color=[
        "royalblue",
        "khaki",
        "khaki",
        "khaki",
        "khaki",
        "royalblue"
    ],
    edge_color="gray"
)

# Pesos
labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels
)

# Caminho do Dijkstra (VERMELHO)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=arestas_dijkstra,
    edge_color='red',
    width=2
)

# Caminho do BFS (VERDE)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=arestas_bfs,
    edge_color='green',
    width=2,
    style='dashed'
)

plt.title("Comparação entre Dijkstra e BFS")

legenda = [
    Line2D([0], [0], color='red', lw=2, label='Dijkstra'),
    Line2D([0], [0], color='green', lw=2, linestyle='dashed', label='BFS')
]

plt.legend(handles=legenda, loc='upper right')

plt.show()


# Resultados
menor_tempo = nx.dijkstra_path_length(
    G,
    source="FIB",
    target="Boulevard",
    weight="weight"
)

print("Caminho usando Dijkstra:")
print(" -> ".join(menor_caminho))
print(f"Tempo total: {menor_tempo} minutos")

print("\nCaminho usando BFS:")
print(" -> ".join(caminho_bfs))