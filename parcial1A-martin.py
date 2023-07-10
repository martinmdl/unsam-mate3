# En una comunidad de 100 deportistas se sabe que 30 de ellos entrenan fútbol, 50 entrenan squash 
# y 60 entrenan tenis. 22 entrenan tenis y fútbol, 30 entrenan squash y tenis y 15 entrenan squash y fútbol. 
# Si 10 deportistas entrenan los tres deportes 
# 1-¿cuántos entrenan sólo tenis?
# 2-¿cuántos entrenan sólo fútbol?
# 3-¿cuántos entrenan sólo squash?
# 4-¿cuántos entrenan tenis o fútbol?

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

lista_futbol = [3, 5, 10, 12]
tupla_squash = (10, 20, 15, 5)
diccio_tenis = {"infantil": 12, "juniors": 10, "adolescentes": 20, "adultos": 18}
universo = 100
ninguno = 17

##########################
# TRANSFORMO A CONJUNTOS #
##########################

def to_set(data_strutcture):
    """recibo una estrcutura de datos tipo dict, set, tuple, list"""
    if(isinstance(data_strutcture, dict)):
        return set(data_strutcture.values())
    return set(data_strutcture)

set_futbol, set_squash, set_tenis = to_set(lista_futbol), to_set(tupla_squash), to_set(diccio_tenis)

#####################################
# OPERO CON ARITMETICA DE CONJUNTOS #
#####################################

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

##################################
# OPERO CON METODOS DE CONJUNTOS #
##################################

def venn3_combinations_methods(option, a, b, c):
    match option:
        case "Abc":            
            return a.difference(b.union(c))
        case "aBc":
            return b.difference(a.union(c))
        case "abC":
            return c.difference(a.union(b))
        case "ABc":
            return a.intersection(b).difference(c)
        case "AbC":
            return a.intersection(c).difference(b)
        case "aBC":
            return b.intersection(c).difference(a)
        case "ABC":
            return a.intersection(b).intersection(c)
        case _:
            return -1

# solo_futbol = venn3_combinations_arithmetic("Abc", set_futbol, set_squash, set_tenis)
# solo_squash = venn3_combinations_arithmetic("aBc", set_futbol, set_squash, set_tenis)
# solo_tenis = venn3_combinations_arithmetic("abC", set_futbol, set_squash, set_tenis)
# solo_futbol_y_squash = venn3_combinations_arithmetic("ABc", set_futbol, set_squash, set_tenis)
# solo_futbol_y_tenis = venn3_combinations_arithmetic("AbC", set_futbol, set_squash, set_tenis)
# solo_squash_y_tenis = venn3_combinations_arithmetic("aBC", set_futbol, set_squash, set_tenis)
# solo_futbol_y_squash_y_tenis = venn3_combinations_arithmetic("ABC", set_futbol, set_squash, set_tenis)

solo_futbol = venn3_combinations_methods("Abc", set_futbol, set_squash, set_tenis)
solo_squash = venn3_combinations_methods("aBc", set_futbol, set_squash, set_tenis)
solo_tenis = venn3_combinations_methods("abC", set_futbol, set_squash, set_tenis)
solo_futbol_y_squash = venn3_combinations_methods("ABc", set_futbol, set_squash, set_tenis)
solo_futbol_y_tenis = venn3_combinations_methods("AbC", set_futbol, set_squash, set_tenis)
solo_squash_y_tenis = venn3_combinations_methods("aBC", set_futbol, set_squash, set_tenis)
solo_futbol_y_squash_y_tenis = venn3_combinations_methods("ABC", set_futbol, set_squash, set_tenis)

def futbol_o_tenis(futbol, tenis):
    acum = 0
    for element in futbol | tenis:
        acum = acum + element
    return acum

tenis_o_futbol = futbol_o_tenis(set_futbol, set_tenis)

#############################
# GRAFICO CON VENN3 CIRCLES #
#############################

plt.figure('Modelo de parcial')
v = venn3((3, 5, 0.5, 6, 1.2, 2, 1), set_labels = ("Futbol", "Squash", "Tenis"))

for element in ('100', '010', '110', '001', '101', '011', '111'):
    v.get_label_by_id(element).set_fontsize(10) # tamaño letra
    v.get_patch_by_id(element).set_alpha(0.5) # opacidad color

v.get_label_by_id("100").set_text(solo_futbol)
v.get_label_by_id("010").set_text(solo_squash)
v.get_label_by_id("001").set_text(solo_tenis)
v.get_label_by_id("110").set_text(solo_futbol_y_squash)
v.get_label_by_id("101").set_text(solo_futbol_y_tenis)
v.get_label_by_id("011").set_text(solo_squash_y_tenis)
v.get_label_by_id("111").set_text(solo_futbol_y_squash_y_tenis)

c = venn3_circles(subsets=(3, 5, 0.5, 6, 1.2, 2, 1))

plt.text(-1.3, 0.70, f"Universo = {universo}", size = 9,
    bbox = dict(boxstyle = "square", ec = (1.0, 0.7, 0.5), fc = (1.0, 0.9, 0.8)))
plt.text(-1.3, 0.60, f"Fuera de los conjuntos = {ninguno}", size = 9,
    bbox = dict(boxstyle = "square", ec = (1.0, 0.7, 0.5), fc = (1.0, 0.9, 0.8)))
plt.text(-1.3, 0.20,
    f"1. Solo tenis = {solo_tenis}\n"
    f"2. Solo futbol = {solo_futbol}\n"
    f"3. Solo squash = {solo_squash}\n"
    f"4. Solo tenis = {tenis_o_futbol}",
    size = 9)

plt.axis('on')
plt.title("Deportistas")
plt.show()