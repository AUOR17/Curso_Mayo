nombre = ["Ana", "Carlos", "Beatriz"]

# print(type(nombre).__name__)

nombre.append("Bryan")
# print(nombre)
nombre.insert(2,"Cristian")
# print(nombre)

# print(nombre[-1])

lista_2 = ["perro", "gato", "sapo", "rana"]

# print(nombre + lista_2)

lista_2.extend(nombre)
# print(lista_2)

numeros = [1,2,3,4,5,6,6,6,6,7,8,9,10,11]

numeros.remove(6) # Elimina el valor que encuentra primero en la lista
numeros.pop() # Elimina el ultimo valor de la lista
numeros.pop(1) # Eliminar el valor en el indice especificado (1)
# print(len(numeros))
# print(numeros)

# if 20 in numeros:
#     print("Encontre al numero 20")
# else:
#     print("No encuentro al numero 20")

numeros.sort(reverse=True)
# print(numeros)

abc = "abcdefghijklmnopqrstuvwxyz"

# print(abc[5:10])
# print(abc[2:6])
# print(abc[:-3])
# print(abc[-3:])
# print(abc[::5])
# print(abc[::-1])
# copia = abc[::]
# copia_1 = numeros.copy()

# print(abc[::])

numeros_1 = [1,2,3,4,5,6,7,8,9,10]
cuadrados = []

for n in numeros_1:
    cuadrados.append(n*n)

print(cuadrados)

cuadrados_c = [n*n for n in numeros_1]
print(cuadrados_c)

cuadrado_par = [n*n for n in numeros_1 if n%2 == 0]
print(cuadrado_par)