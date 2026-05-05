import sys
import random

# tupla = (24,12,12,34,45,65)
# print(tupla)
# print(type(tupla).__name__)

# tupla_1 = (13,)
# tupla_falsa = (13)

# print(type(tupla_1).__name__)
# print(type(tupla_falsa).__name__)

# print(tupla[3])

# tupla_b = (1,2,3,4,5)
# print(f"Lugar en la memoria antes de la conversion: {id(tupla_b)}")

# tupla_b[0]= 10

# tupla_b = list(tupla_b)
# tupla_b[0] = 10
# tupla_b = tuple(tupla_b)
# print(tupla_b)
# print(f"Lugar en la memoria despues de la conversion: {id(tupla_b)}")

# tupla_b = (10,) + tupla_b[1:]
# print(tupla_b)
# print(f"Lugar en la memoria despues de la conversion: {id(tupla_b)}")

# tupla_b = tupla_b + (19,)
# print(tupla_b)
# print(f"Lugar en la memoria despues de la conversion: {id(tupla_b)}")

# tupla_b = tupla_b + tuple([40,50])
# print(tupla_b)
# print(f"Lugar en la memoria despues de la conversion: {id(tupla_b)}")

# tupla_ext = (1,2,[3,5])
# print(tupla_ext)
# print(f"Lugar en la memoria de tupla_ext: {id(tupla_ext)}")

# # tupla_ext[2] = [9,9]
# tupla_ext[2].extend([9,9])
# print(tupla_ext)
# print(f"Lugar en la memoria de tupla_ext: {id(tupla_ext)}")

# tupla_ext[2][:] = [9,9]
# print(tupla_ext)
# print(f"Lugar en la memoria de tupla_ext: {id(tupla_ext)}")

datos = (1,"Angel", "Paz","7534","Cafe","Perro", "KOF","Zoro")
# datos_useful = datos[:4]
# print(datos_useful)

# id,name,calle,zip_code,animal,color,juego,personaje= datos
# id,name, calle, zip_code, *general = datos
# id,name, calle, zip_code, _,_,_,_ = datos
*datos_useful, color, animal, juego, personaje = datos

# print(f"El nombre del usuario es {datos_useful}")
# print(f"Los datos generales son: {personaje}")

n = 10000000
inicio = 1
fin = 10000000

lista_memoria = [1,2,3,4,5,6,7]
tupla_memoria = (1,2,3,4,5,6,7)

print(f"Bytes en la lista: {sys.getsizeof(lista_memoria)}")
print(f"Bytes en la tupla: {sys.getsizeof(tupla_memoria)}")

lista_rand = [random.randint(inicio, fin) for _ in range(n)]
tupla_rand = (random.randint(inicio, fin) for _ in range(n))

print(f"Bytes en la lista: {sys.getsizeof(lista_rand)}")
print(f"Bytes en la tupla: {sys.getsizeof(tupla_rand)}")
