# En la provincia de Bs. As. se realizó una encuesta sobre la posesión de determinados vehículos.
# Los datos obtenidos se agruparon de la siguiente manera:
# En una lista los porcentajes de los que tienen moto = [14, 17, 9, 13, 15, 12]
# En una tupla los porcentajes de los que tienen bicicleta = (17, 8, 9, 7, 10, 11, 12, 4, 12)
# En un diccionario los porcentajes de los que tienen auto = {"Chico":27,"Mediano":17,"Grande":16}
# Como resultado se han obtenido los siguientes datos:
# - 2% no tiene ningún vehículo.
# - 55% tienen los tres vehículos.
# - 2% sólo tienen bicicleta y auto
# - 18% sólo tienen moto y bicicleta
# - 1% sólo auto

# 1. Qué porcentaje de encuestados poseen sólo uno de los vehículos?
# 2. Qué porcentaje sólo tienen moto y auto?
# 3. Qué porcentaje tienen sólo moto?
# 4. Qué porcentaje de tienen sólo bicicleta?

# 1. Definir variables y estructuras
# 2. Funciones de cálculo sobre las estructuras
# 3. Funciones de cálculos sobre los conjuntos
# 4. Diagramas y respuestas

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

universo = 100
ninguno = 0
moto = [14, 17, 9, 13, 15, 12]
bicicleta = (17, 8, 9, 7, 10, 11, 12, 4, 12)
auto = {"Chico":27,"Mediano":17,"Grande":16}

def to_set(data_strutcture):
    if(isinstance(data_strutcture, dict)):
        return set(data_strutcture.values())
    return set(data_strutcture)

set_moto, set_bici, set_auto = to_set(moto), to_set(bicicleta), to_set(auto)

############################################################################################

def venn3_combinations_arithmetic(option, a, b, c):
    match option:
        case "Abc":            
            return a - (b | c)
        case "aBc":
            return b - (a | c)
        case "abC":
            return c - (a | b)
        case "ABc":
            return (a & b) - c
        case "AbC":
            return (a & c) - b
        case "aBC":
            return (b & c) - a
        case "ABC":
            return a & b & c
        case _:
            return -1
        
solo_moto = venn3_combinations_arithmetic("Abc", set_moto, set_bici, set_auto)
solo_bici = venn3_combinations_arithmetic("aBc", set_moto, set_bici, set_auto)
solo_auto = venn3_combinations_arithmetic("abC", set_moto, set_bici, set_auto)
solo_moto_y_bici = venn3_combinations_arithmetic("ABc", set_moto, set_bici, set_auto)
solo_moto_y_auto = venn3_combinations_arithmetic("AbC", set_moto, set_bici, set_auto)
solo_bici_y_auto = venn3_combinations_arithmetic("aBC", set_moto, set_bici, set_auto)
solo_moto_y_bici_y_auto = venn3_combinations_arithmetic("ABC", set_moto, set_bici, set_auto)

############################################################################################

plt.figure('Modelo de parcial 2')
v = venn3((1,1,1,1,1,1,1), set_labels = ("Moto", "Bici", "Auto"))

for element in ('100', '010', '110', '001', '101', '011', '111'):
    v.get_label_by_id(element).set_fontsize(10) # tamaño letra
    v.get_patch_by_id(element).set_alpha(0.5) # opacidad color

v.get_label_by_id("100").set_text(solo_moto)
v.get_label_by_id("010").set_text(solo_bici)
v.get_label_by_id("001").set_text(solo_auto)
v.get_label_by_id("110").set_text(solo_moto_y_bici)
v.get_label_by_id("101").set_text("")
v.get_label_by_id("011").set_text("")
v.get_label_by_id("111").set_text(solo_moto_y_bici_y_auto)

v.get_patch_by_id("101").set_color("white")
v.get_patch_by_id("011").set_color("white")

c = venn3_circles(subsets=(1,1,1,1,1,1,1))

plt.text(-1.3, 0.70, f"Universo = {universo}", size = 9,
    bbox = dict(boxstyle = "square", ec = (1.0, 0.7, 0.5), fc = (1.0, 0.9, 0.8)))
plt.text(-1.3, 0.60, f"Fuera de los conjuntos = {ninguno}", size = 9,
    bbox = dict(boxstyle = "square", ec = (1.0, 0.7, 0.5), fc = (1.0, 0.9, 0.8)))
plt.text(-1.3, 0.20,
    f"1. Solo tenis = {solo_auto}\n"
    f"2. Solo futbol = {solo_moto}\n"
    f"3. Solo squash = {solo_bici}\n",
    size = 9)

plt.axis('on')
plt.title("Deportistas")
plt.show()