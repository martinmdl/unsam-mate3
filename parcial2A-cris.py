"""Parcial 2do"""
# # Ejercicio 1
# Dada la siguiente matriz que determina nodos, pesos y conexiones, resolver usando networkx:

#    a  b  c  d  e  t
# a    12    14
# b        7  4  11 23
# c               2 10
# d               6
# e                  9
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
# q) Emitir la ruta ponderada más corta entre ‘a’ y ‘t’ usando el algoritmo de
# Dijkstra
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
import warnings
import networkx as nx
import matplotlib.pyplot as plt
# Para el ej2)
import re
warnings.filterwarnings('ignore')
# Defino 2 funciones(mas tarde seran tomadas como metodos)


def emito_grafo(grafo_nx, pos,titulo):
    """Emite un grafico, recibe un grafico nx y una posicion(con o sin disposicion)"""
    nx.draw_networkx_nodes(grafo_nx, pos, node_color='violet', node_size=600)
    nx.draw_networkx_labels(grafo_nx, pos, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edges(grafo_nx, pos, edge_color='grey',
                           width=2)
    # arrows= True, arrowstyle='<|-|>', arrowsize=10(Para digrafo!)
    labels = nx.get_edge_attributes(grafo_nx, 'weight')
    nx.draw_networkx_edge_labels(grafo_nx, pos, edge_labels=labels)
    plt.title(titulo)
    plt.axis('off')
    plt.show()


def cargo_grafo(grafo_nx):
    """Carga aristas con Peso"""
    grafo_nx.add_weighted_edges_from([('a', 'b', 12),
                               ('a', 'd', 14),
                               ('b', 'd', 4),
                               ('b', 'e', 11),
                               ('b', 'c', 7),
                               ('b', 't', 23),
                               ('c', 't', 10),
                               ('c', 'e', 2),
                               ('d', 'e', 6),
                               ('e', 't', 9)])


# Respuesta;
# a) Construir los nodos y b) Construir con enlaces y pesos
grafo = nx.Graph()
cargo_grafo(grafo)
# c) Emitir números de nodos
print(f"El numero de nodos es: {grafo.number_of_nodes()}")
# d) Emitir los nodos
print(f"Los nodos son: {grafo.nodes()}")
# e) Emitir números de enlaces
print(f"El numero de enlaces es: {grafo.number_of_edges()}")
# f) Emitir los enlaces
print(f"Los enlaces son: {grafo.edges()}")
# g) Emitir los vecinos de ‘b’
print(f"Los vecinos de b son: {list(grafo.neighbors('b'))}")
# h) Emitir cantidad de aristas de cada nodo
for nodo in grafo.nodes():
    print(f"los vecinos de {nodo}: {len(list(grafo.neighbors(nodo)))}")
print("Cantidad de aristas segun moni de cada nodo: ", grafo.degree())
# i) Convertir en diccionario la salida anterior
dic={}
for par in grafo.degree():
    dic[par[0]]=par[1]
print(dic)
print(dict(grafo.degree()))
# j) Crear la matriz de adyacencia y emitirla
matriz_adj=nx.adjacency_matrix(grafo)
print(matriz_adj.todense())
# k) Crear la matriz de incidencia y emitirla
matriz_ins=nx.incidence_matrix(grafo)
print(matriz_ins.todense())
# l) Emitir valores de los enlaces del nodo ‘c’
print(f"Los valres de lo enlaces del nodo C son: {grafo['c']}")
# m) Emitir el peso de la relación entre ‘b’ y ‘e’
print(f"El peso de la relacion entre b y e es: {grafo['b']['e']['weight']}")
# n) Emitir la ruta más corta desde ‘a’ al objetivo
print(
    f"Ruta mas corta desde a hasta el objetivo:{nx.algorithms.shortest_path(grafo, 'a')} ")
# o) Emitir la longitud desde ‘a’ hasta el objetivo
print(
    f"Longitud de a hasta el objetivo es:{nx.single_source_shortest_path_length(grafo, 'a')}")
# p) Emitir el promedio de la ruta más corta usando el método de floyd-warshall
print(
    f"Promedio de la ruta mas corta usando floyd-warshall \
    es:{nx.algorithms.average_shortest_path_length(grafo, method='floyd-warshall')}")
# q) Emitir la ruta ponderada más corta entre ‘a’ y ‘t’ usando el algoritmo de Dijkstra
print(
    f"Ruta mas corta usando el algoritmo de \
    Dijkstra entre:{nx.algorithms.dijkstra_path(grafo, 'a', 't')}")
# r) Emitir la longitud de la ruta ponderada entre ‘a’ y ‘t’
print(
    f"Longitud de Ruta ponderada más corta entre a y t:{nx.dijkstra_path_length(grafo,'a','t')}")
# s) Emitir la longitud de la ruta desde el nodo ‘c
print(
    f"Longitud de Ruta ponderada más corta \
    desde el nodo:{nx.single_source_dijkstra_path_length(grafo,'c')}")
# t) Emitir el radio del grafo
print(f"Radio:{nx.radius(grafo)}")
# u) Emitir el diámetro del grafo
print(f"Diámetro:{nx.diameter(grafo)}")
# v) Emitir la excentricidad
print(f"Excentricidad:{nx.eccentricity(grafo)}")

# w) Emitir el centro del grafo
print(f"Centro:{nx.center(grafo)}")

# x) Emitir la periferia del grafo
print(f"Periferia:{nx.periphery(grafo)}")

# y) Emitir la densidad.
print(f"Densidad:{nx.density(grafo)}")
# z) Dibujar el grafo y emitir con matplotlib.pyplot
disposicion = nx.shell_layout(grafo)
emito_grafo(grafo,disposicion,'Grafo')
# aa) Convertir en grafo dirigido. Dibujar el nuevo grafo y emitir con matplotlib.pyplot
digrafo = grafo.to_directed()
cargo_grafo(digrafo)
disposicion_digrafo = nx.shell_layout(digrafo)
# emito_grafo(digrafo, disposicion_digrafo,'Digrafo')

# # Ejercicio 2
# Las siguientes líneas de texto fueron extraídas de un archivo con muchas entradas,
# representan: ip, usuario, fecha y hora y petición. Encuentra la expresión regular
# para extraer y emitir la cadena entre ‚ ‛. Desarrolla el código correspondiente.
"""
98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
"""

TEXTO ="""
98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
"""
REGEX = r'[A-Z]+\s[/\w-]+\s[A-Z]+/[\d.]+'
REGEX2 = r"[A-Z]+\s[/\w-]+\s[A-Z]+/[\d]+\.[\d]+"
#Otras soluciones.
BUSCAR = r"[A-Z]+\s/[/\w-]+\s[A-Z]+/\d\.\d"
lista_match = re.findall(REGEX2, TEXTO)
for encontrado in lista_match:
    print(f"Se encontro el siguiente string: {encontrado}")
# print(lista_match)

# Ejercicio 3
# Crear la clase grafo con sus métodos (en Python) para el ejercicio 1.
class Graph():
    """Clase generadora de Graph que requiere de un nombre y conocer el peso de sus aristas"""
    def __init__(self,nombre):
        self.nombre = nombre
        self.nombre = nx.Graph()
    def carga_aristas(self,aristas_peso):
        """Carga datos"""
        self.nombre.add_weighted_edges_from(aristas_peso)
    def dibujar(self):
        """Setea un formato"""
        pos = nx.shell_layout(self.nombre)
        etiquetas = nx.get_edge_attributes(self.nombre, 'weight')
        nx.draw_networkx(self.nombre, pos, node_color="violet", node_size=600,edge_color="grey", width=2, font_size=10,arrows=True, arrowstyle='<|-|>', arrowsize=10)
        nx.draw_networkx_edge_labels(self.nombre, pos, edge_labels=etiquetas)
        plt.title('Grafo Dirigido')
        plt.axis('off')
        plt.show()
    def a_digraph(self):
        """Convierte a di grafo"""
        self.nombre = self.nombre.to_directed()
    def get_graph(self):
        """Devuelve el grafo """
        return self.nombre

grafico = Graph("R")
grafico.carga_aristas([('a', 'b', 12), ('a', 'd', 14), ('b', 'c', 7), ('b', 'd', 4), ('b', 'e', 11),('b', 't', 23), ('c', 'e', 2), ('c', 't', 10), ('d', 'e', 6), ('e', 't', 9)])
grafico.dibujar()