# COMPLEX DATA TYPES / COMPUND DATA STRUCTURES

tupla = (4, "5", 6.2, True, 6.2)
# elementos: ordenados(index) - repetibles - cualquier tipo
# tupla = tuple(objeto_iterable)
# objeto_iterable -> lista, tupla, conjunto, string, diccionarios (keys)
print(dir(tupla))
# 'count', 'index'

lista = [7, "8", 9.2]
# elementos: ordenados(index) - repetibles - cualquier tipo
# lista = list(objeto_iterable)
# objeto_iterable -> lista, tupla, conjunto, string, diccionarios (keys)
print(dir(lista))
# 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort'

conjunto = {1, "2", 3.2}
# elementos: desordenados(no index) - irrepetibles - no booleanos
# conjunto = set(objeto_iterable)
# objeto_iterable -> lista, tupla, conjunto, string, diccionarios (keys)
print(dir(conjunto))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

diccionario = {
    "nombre": "martin",
    "edad": 22,
    "altura": 1.69,
    "donante": True,
}
# elementos: ordenados(keys) - irrepetibles - cualquier tipo (keys y values)
# diccionario = dict(secuencia_pares)
# secuencia_pares -> tupla_tuplas, tupla_listas, lista_tuplas, lista_listas
print(dir(diccionario))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
# 'pop', 'popitem','setdefault', 'update', 'values'

#############################################################################################
#############################################################################################

# ITERAR LISTAS Y TUPLAS (funcionan igual)

animales = ["perro", "gato", "loro"]
numeros = [1, 2, 3, 4, 5]
diccionario = {
    "nombre": "martin",
    "edad": 22,
    "altura": 1.69
}

# continue y break
for i in numeros:
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

# linkeados respectivamente
for animal, numero in zip(animales, numeros):
    print(f"animal: {animal}")
    print(f"numero: {numero}")
else: # siempre se muestra una vez y el "break" saltea el "else"
    print("fin")

# forma incorrecta de recorrer por index
for i in range(len(animales)):
    print(animales[i])

# forma eficiente de recorrer por index (enumerate -> tuplas pares)
for animal in enumerate(animales):
    print(f"indice: {animal[0]}")
    print(f"valor: {animal[1]}")

# recorrer diccionario (items -> tuplas -> key-value)
for data in diccionario.items():
    print(f"key: {data[0]}")
    print(f"value: {data[1]}")

# "for" en una linea
numeros_doble = [i*2 for i in numeros]
print(numeros_doble)