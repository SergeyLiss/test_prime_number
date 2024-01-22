import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()  # создаём объект графа

# определяем список узлов (ID узлов)
# nodes = [(1, {'name': '100'}), (2, {"name": "A"}), (3, {"name": "+"}), (4, {"name": "xyz"}), (5, {"name": "5"})]
nodes = ['100', "A", "+", "xyz", "5"]

# определяем список рёбер
# список кортежей, каждый из которых представляет ребро
# кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
edges = [(nodes[0], nodes[1]), (nodes[0], "+"), (nodes[1], "+"), ("+", "xyz"), ("+", "5")]

# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()