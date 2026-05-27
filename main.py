import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo não direcionado
G = nx.Graph()

# Adicionando os vértices (locais)
vertices = [
    "FIB",
    "Centro",
    "Confianca Castelo",
    "Duque",
    "Nuno",
    "Boulevard"
]

G.add_nodes_from(vertices)

# Adicionando as arestas ponderadas (tempo entre os locais)
G.add_edge("FIB", "Centro", weight=13)
G.add_edge("Centro", "Boulevard", weight=9)

G.add_edge("FIB", "Confianca Castelo", weight=8)
G.add_edge("Confianca Castelo", "Boulevard", weight=12)

G.add_edge("FIB", "Duque", weight=14)
G.add_edge("Duque", "Boulevard", weight=11)

G.add_edge("FIB", "Nuno", weight=16)
G.add_edge("Nuno", "Boulevard", weight=12)

# Posições manuais para o grafo ficar organizado
pos = {
    "FIB": (0, 0),
    "Centro": (3.5,3),
    "Confianca Castelo": (2, 1),
    "Duque": (3, -1),
    "Nuno": (3, -3),
    "Boulevard": (5, 0)
}

# Tamanho da janela
plt.figure(figsize=(10, 6))

# Desenhar o grafo
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
)

# Mostrar pesos das arestas
labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels
)

# Mostrar gráfico
plt.show()

# Algoritmo de Dijkstra
menor_caminho = nx.dijkstra_path(
    G,
    source="FIB",
    target="Boulevard",
    weight="weight"
)

menor_tempo = nx.dijkstra_path_length(
    G,
    source="FIB",
    target="Boulevard",
    weight="weight"
)

# Exibir resultado
print("Melhor rota:")
print(" -> ".join(menor_caminho))

print(f"Tempo total: {menor_tempo} minutos")


#Aplicando o BFS para comparação
caminho_bfs = nx.shortest_path(
    G,
    source="FIB",
    target="Boulevard"
)

print("\nCaminho usando BFS:")
print(" -> ".join(caminho_bfs))

print("\nCaminho usando Dijkstra:")
print(" -> ".join(menor_caminho))
print(f"Tempo total: {menor_tempo} minutos")

#Floyd-Warshall consegue ver o menor caminho entre todos os vertices
fw = nx.floyd_warshall(G, weight='weight')
print(fw["FIB"]["Boulevard"])