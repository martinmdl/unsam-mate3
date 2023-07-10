# EJERCICIO 1
# Dada la siguiente matriz que determina nodos, pesos y conexiones, resolver usando networkx:

#    a  b  c  d  e  t
# a    12    14
# b        7  4  11 23
# c               2 10
# d               6
# e                  9

# a) Construir los nodos
# b) Construir con enlaces y pesos
# c) Emitir números de nodos
# d) Emitir los nodos
# e) Emitir números de enlaces
# f) Emitir los enlaces
# g) Emitir los vecinos de ‘b’
# h) Emitir cantidad de aristas de cada nodo
# i) Convertir en diccionario la salida anterior
# j) Crear la matriz de adyacencia y emitirla
# k) Crear la matriz de incidencia y emitirla
# l) Emitir valores de los enlaces del nodo ‘c’
# m) Emitir el peso de la relación entre ‘b’ y ‘e’
# n) Emitir la ruta más corta desde ‘a’ al objetivo
# o) Emitir la longitud desde ‘a’ hasta el objetivo
# p) Emitir el promedio de la ruta más corta usando el método de floyd-warshall
# q) Emitir la ruta ponderada más corta entre ‘a’ y ‘t’ usando el algoritmo de Dijkstra
# r) Emitir la longitud de la ruta ponderada entre ‘a’ y ‘t’
# s) Emitir la longitud de la ruta desde el nodo ‘c
# t) Emitir el radio del grafo
# u) Emitir el diámetro del grafo
# v) Emitir la excentricidad
# w) Emitir el centro del grafo
# x) Emitir la periferia del grafo
# y) Emitir la densidad.
# z) Dibujar el grafo y emitir con matplotlib.pyplot
# aa) Convertir en grafo dirigido. Dibujar el nuevo grafo y emitir con matplotlib.pyplot

# EJERCICIO 2
# Las siguientes líneas de texto fueron extraídas de un archivo con muchas entradas,
# representan: ip, usuario, fecha y hora y petición. Encuentra la expresión regular
# para extraer y emitir la cadena entre ‚ ‛. Desarrolla el código correspondiente.

# """
# 98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
# 229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
# 197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
# """

# EJERCICIO 3
# Crear la clase grafo con sus métodos (en Python) para el ejercicio 1.

import warnings
import networkx as nx
import matplotlib.pyplot as plt
import re
warnings.filterwarnings('ignore')

###########
# PUNTO 1 #
###########

aristas = [
    ('a', 'b', 12),
    ('a', 'd', 14),
    ('b', 'c', 7),
    ('b', 'd', 4),
    ('b', 'e', 11),
    ('b', 't', 23),
    ('c', 'e', 2),
    ('c', 't', 10),
    ('d', 'e', 6),
    ('e', 't', 9)
]

def cargar_grafo(name, edges):
    name.add_weighted_edges_from(edges)

grafo1 = nx.Graph()
cargar_grafo(grafo1, aristas)

print(f"C. Numero de nodos: {grafo1.number_of_nodes()}")

print(f"D. Nodos: {grafo1.nodes()}")

print(f"E. Numero de enlaces: {grafo1.number_of_edges()}")

print(f"F. Enlaces: {grafo1.edges()}")

print(f"G. Vecinos de 'b': {list(grafo1.neighbors('b'))}")

print(f"H. Cantidad de aristas de cada nodo: {grafo1.degree()}")

print(f"I. Transformo punto H en diccionario: {dict(grafo1.degree())}")

matriz_adyacencia = nx.adjacency_matrix(grafo1)
print(f"J. Matriz de adyacencia:\n{matriz_adyacencia.todense()}")

matriz_insidencia = nx.incidence_matrix(grafo1)
print(f"K. Matriz de incidencia:\n{matriz_insidencia.todense()}")

print(f"L. Valores de enlaces de 'c': {grafo1['c']}")

print(f"M. Peso de la relacion entre 'b' y 'e': {grafo1['b']['e']['weight']}")

print(f"N. Ruta mas corta desde 'a' hasta el objetivo: {nx.algorithms.shortest_path(grafo1, 'a')} ")

print(f"O. Longitud de 'a' hasta el objetivo es: {nx.single_source_shortest_path_length(grafo1, 'a')}")

print(f"P. Promedio de la ruta mas corta usando floyd-warshall es: {nx.algorithms.average_shortest_path_length(grafo1, method='floyd-warshall')}")

print(f"Q. Ruta ponderada mas corta entre 'a' y 't' usando Dijkstra: {nx.algorithms.dijkstra_path(grafo1, 'a', 't')}")

print(f"R. Longitud de ruta ponderada más corta entre 'a' y 't': {nx.dijkstra_path_length(grafo1, 'a', 't')}")

print(f"S. Longitud de la ruta desde el nodo 'c': {nx.single_source_dijkstra_path_length(grafo1,'c')}")

print(f"T. Radio del grafo: {nx.radius(grafo1)}")

print(f"U. Diámetro del grafo: {nx.diameter(grafo1)}")

print(f"V. Excentricidad del grafo: {nx.eccentricity(grafo1)}")

print(f"W. Centro del grafo: {nx.center(grafo1)}")

print(f"X. Periferia del grafo: {nx.periphery(grafo1)}")

print(f"Y. Densidad del grafo: {nx.density(grafo1)}")

pos1 = nx.shell_layout(grafo1)

def mostrar_grafo(graph, positions):
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_nodes(graph, positions, node_color = 'orange')
    nx.draw_networkx_edges(graph, positions, edge_color ='grey', width = 1.5)
    nx.draw_networkx_labels(graph, positions, font_size = 10)
    nx.draw_networkx_edge_labels(graph, positions, edge_labels = labels)
    plt.axis('off')
    plt.show()
    
mostrar_grafo(grafo1, pos1)

grafo2 = grafo1.to_directed()
cargar_grafo(grafo2, aristas)
pos2 = nx.shell_layout(grafo2)
mostrar_grafo(grafo2, pos2)

###########
# PUNTO 2 #
###########

match = r"[A-Z]+\s[A-Za-z0-9/-]+\s[A-Z]+[./0-9]+"
# match = r"[A-Z]+\s[A-Za-z0-9/-]+\s[A-Z]{1,5}[/][0-9]+[.][0-9]+" # MAS ESTRICTO
texto = """
98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
"""
encontrado = re.findall(match, texto)
for linea in encontrado:
    print(linea)

###########
# PUNTO 3 #
###########

class Grafo:

    def __init__(self, edges, name):
        self.aristas = edges
        self.nombre = name
        self.nombre = nx.Graph()

    def cargar(self):
        self.nombre.add_weighted_edges_from(self.aristas)

    def emitir(self):
        pos = nx.shell_layout(self.nombre)
        labels = nx.get_edge_attributes(self.nombre, 'weight')
        nx.draw_networkx_nodes(self.nombre, pos, node_color = 'violet')
        nx.draw_networkx_edges(self.nombre, pos, edge_color ='grey', width = 1.5)
        nx.draw_networkx_labels(self.nombre, pos, font_size = 10)
        nx.draw_networkx_edge_labels(self.nombre, pos, edge_labels = labels)
        plt.axis('off')
        plt.show()

    def mostrar_direcciones(self):
        self.nombre = self.nombre.to_directed()

    def nombre(self):
        return self.nombre

grafo3 = Grafo(aristas, "grafo3")
grafo3.cargar()
grafo3.emitir()
grafo3.mostrar_direcciones()
grafo3.emitir()










