from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# GUARDO VALORES DE LA CONSIGNA EN VARIABLES

juegos = (41,29,58,4,45,37,9,7) # total = 230
deportes = {"Voleybol": 10, # total = 391
    "Hockey": 87,
    "Equitación":23,
    "Ciclismo":81,
    "Paddle":11,
    "Fútbol": 45,
    "Tenis": 37,
    "Rugby": 9, 
    "Básquetbol": 7,
    "Boxeo": 6,
    "Natación":75
}
granja = [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13] # total = 545

universo = 1000
deportes_y_juegos = 98
juegos_y_granja = 152
deportes_y_granja = 88
ninguno = 90

# TRANSFORMO LAS COLECCIONES A CONJUNTOS

def a_conjunto(coleccion):
    if type(coleccion) == dict:
        return set(coleccion.values())
    else:
        return set(coleccion)

set_juegos = a_conjunto(juegos)
set_deportes = a_conjunto(deportes)
set_granja = a_conjunto(granja)

# DETERMINO LAS 7 PARTICIONES (CONJUNTOS) DE VENN3 OPERANDO CON ARITMETICA DE CONJUNTOS

def solo_X(a, b, c):
    return a - (b | c)

def solo_XY(a, b, c):
    return (a & b) - c

def solo_XYZ(a, b, c):
    return a & b & c
    

solo_juegos = solo_X(set_juegos, set_deportes, set_granja)
solo_deportes = solo_X(set_deportes, set_juegos, set_granja)
solo_granja = solo_X(set_granja, set_juegos, set_deportes)
solo_juegos_y_deportes = solo_XY(set_juegos, set_deportes, set_granja)
solo_deportes_y_granja = solo_XY(set_deportes, set_granja, set_juegos)
solo_granja_y_juegos = solo_XY(set_granja, set_juegos, set_deportes)
solo_juegos_deportes_granjas = solo_XYZ(set_granja, set_juegos, set_deportes)

# SUMO RESULTADOS

def suma_conjunto(conjunto):
    return sum(conjunto)

suma_solo_juegos = suma_conjunto(solo_juegos)
suma_solo_deportes = suma_conjunto(solo_deportes)
suma_solo_granja = suma_conjunto(solo_granja)
suma_solo_juegos_y_deportes = suma_conjunto(solo_juegos_y_deportes)
suma_solo_deportes_y_granja = suma_conjunto(solo_deportes_y_granja)
suma_solo_granja_y_juegos = suma_conjunto(solo_granja_y_juegos)
suma_solo_juegos_deportes_granjas = suma_conjunto(solo_juegos_deportes_granjas)
suma_2_de_3 = suma_solo_juegos_y_deportes + suma_solo_deportes_y_granja + suma_solo_granja_y_juegos

# GRAFICO

plt.figure('Hoy me divierto')

v = venn3((1, 1, 1, 1, 1, 1, 1), set_labels = ("Juegos", "Deportes", "Granja"))

for element in ('100', '010', '110', '001', '101', '011', '111'):
    v.get_label_by_id(element).set_fontsize(10) # tamaño letra
    v.get_patch_by_id(element).set_alpha(0.5) # opacidad color

v.get_label_by_id("100").set_text(suma_solo_juegos)
v.get_label_by_id("010").set_text(suma_solo_deportes)
v.get_label_by_id("001").set_text(suma_solo_granja)
v.get_label_by_id("110").set_text(suma_solo_juegos_y_deportes)
v.get_label_by_id("101").set_text(suma_solo_deportes_y_granja)
v.get_label_by_id("011").set_text(suma_solo_granja_y_juegos)
v.get_label_by_id("111").set_text(suma_solo_juegos_deportes_granjas)

c = venn3_circles(subsets = (1, 1, 1, 1, 1, 1, 1))

# RESPONDO PREGUNTAS

plt.text(-1.3, 0.70, f"Universo = {universo}", size = 9)
plt.text(-1.3, 0.60, f"Fuera de los conjuntos = {ninguno}", size = 9)
plt.text(-1.3, 0.20,
    "Participaron en:\n"
    f"1. Todo = {suma_solo_juegos_deportes_granjas}\n"
    f"2. Deportes y juegos = {suma_solo_juegos_y_deportes}\n"
    f"3. Juegos y granja = {suma_solo_granja_y_juegos}\n"
    f"4. Deportes y granja = {suma_solo_deportes_y_granja}\n"
    f"5. Deportes = {suma_solo_deportes}\n"
    f"6. Juegos = {suma_solo_juegos}\n"
    f"7. Granja = {suma_solo_granja}\n"
    f"8. 2 de 3 = {suma_2_de_3}",
    size = 9)

plt.axis('on')
plt.title("Actividades")
plt.show()
















