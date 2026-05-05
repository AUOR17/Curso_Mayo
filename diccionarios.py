diccionario = {}
# print(type(diccionario))

alumno = {"nombre":"Carlos", "edad":27, "lenguaje":"Python", (1,2):"Coordenadas"}
# print(alumno)

# alumno.values("Carlos")

# print(alumno["nombre"])
# print(alumno.get((1,2),None))

alumno["Soltero"] = True
alumno.update({"Carro": "VW"})

# print(alumno)

# for llave in alumno:
#     print(llave)

# for valor in alumno.values():
#     print(f"\n{valor}")

# for key,value in alumno.items():
#     print(f"La llave es; {key}, el valor es {value}")

# elemento_borrado = alumno.pop("Soltero","No enconte el elemento")
# print(alumno)
# print(elemento_borrado)


# dict_1 = {"a":1, "b":2}
# dict_2 = {"b":99, "c":3}

# dict_1.update(dict_2)

# dict_g = dict_1 | dict_2
# print(dict_g)

# numeros  = [ 1,2,3,4,5,6,7,8,9,10]
# dict_part = {n: n**2 for n in numeros if n%2 !=0}
# print(dict_part)

perfil = {
    "nombre": "Arthur",
    "clase": "Guerrero",
    "nivel": 5,
    "oro": 150
}

# perfil["edad"] = 25
# perfil["nivel"] = 10
perfil.update({"edad":25, "nivel":10})

perfil["oro"] = perfil["oro"] * 100

# print(perfil)
# print(perfil.keys())

misiones = [
    {"id": 1, "titulo": "Cazar slimes", "recompensa_oro": 50, "nivel_minimo": 2},
    {"id": 2, "titulo": "Escoltar mercader", "recompensa_oro": 120, "nivel_minimo": 5},
    {"id": 3, "titulo": "Derrotar al Dragón", "recompensa_oro": 5000, "nivel_minimo": 20}
]

print(misiones[0]["recompensa_oro"])
print(misiones[2]["nivel_minimo"])


def evaluar_mision(jugador, lista_misiones):

    print(f"Revisando al jugadr: {jugador['nombre']}")

    for mision in lista_misiones:
        if jugador["nivel"] >= mision["nivel_minimo"]:
            print(f"El jugador puede hacer la mision {mision['titulo']}")
        elif jugador["nivel"] == mision["nivel_minimo"] -1 :
            print(f"Te falta un nivel, por favor regresa de nuevo.")
        else:
            diferencia = mision["nivel_minimo"] - jugador["nivel"]
            print(f"Te faltan {diferencia} para aceptar la mision ")

evaluar_mision(perfil, misiones)