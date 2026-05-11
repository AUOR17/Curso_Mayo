import psycopg2
import sys
from core_engine.database import inicializar_db, obtener_conexion
from core_engine.models import Guerrero, Mago, Gremio

def fundar_gremio():
    nombre = input("Ingrese el nombre del gremio: ")
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO gremios (nombre_gremio) VALUES (%s)", (nombre,))
        conexion.commit()
        print(f"Gremio {nombre} fundado con éxito.")
    except Exception as e:
        print(f"Error al fundar el gremio: {e}")
    except psycopg2.IntegrityError:
        print(f"Alto ahi, ya existe un Gremio registrado con el nombre: {nombre}")
    finally:
        conexion.close()

def reclutar_aventurero():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try: 
        hay_gremios = mostrar_gremios_disponibles(cursor)

        if not hay_gremios:
            print("Se debe fundar un Gremio")
            return
        
        gremio_id = input("Ingresa el ID del grmeio elegido: ")
        nombre = input("Nombre del aventurero: ")
        clase = input("Elige la clase (1 para Guerrero, 2 para Mago)")

        if clase == "1":
            armadura = int(input("Puntos de armadura: "))
            nuevo_pj = Guerrero(nombre, salud_maxima=160, puntos_armadura=armadura)
            cursor.execute('''
                INSERT INTO personajes (nombre, salud_maxima, tipo_clase, puntos_armadura, gremio_id)
                VALUES (%s,%s,%s,%s,%s)
            ''', (nuevo_pj.nombre, nuevo_pj.salud_maxima, "Guerrero", nuevo_pj.puntos_armadura, gremio_id))
        elif clase == "2":
            mana = int(input("Ingrese los puntos de mana maximo: "))
            nuevo_pj = Mago(nombre, salud_maxima=160, mana_maximo=mana)
            cursor.execute('''
                INSERT INTO personajes (nombre, salud_maxima, tipo_clase, mana_maximo, gremio_id)
                VALUES (%s,%s,%s,%s,%s)
            ''', (nuevo_pj.nombre, nuevo_pj.salud_maxima, "Mago", nuevo_pj.mana_maximo, gremio_id))
        else:
            print("Clase no reconocida")
            return
        
        conexion.commit()
        print(f"{nuevo_pj.nombre} ha sido reclutado")

    except psycopg2.IntegrityError:
        print(f"Ya existe un personaje llamado '{nombre}'")

    except Exception as e:
        print(f"Ocurrio un error: {e}")

    finally:
        conexion.close()

def mostrar_gremios_disponibles(cursor):

    print(" --- Mapa de gremios Activos ---")
    cursor.execute("SELECT id, nombre_gremio FROM gremios")
    gremios = cursor.fetchall()

    if not gremios:
        print("No existe ningun gremio, Hay que fundar uno")
        return False
    
    for gremio in gremios:
        print(f"[{gremio[0]}] {gremio[1]}")
    
    return True

def ver_taberna():
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:

        hay_gremios = mostrar_gremios_disponibles(cursor)
        if not hay_gremios:
            return
        
        gremio_id = input("Ingrese el ID del gremio para ver sus miembros: ")

        cursor.execute('''
            SELECT p.nombre, p.salud_maxima, p.tipo_clase, p.puntos_armadura, p.mana_maximo, g.nombre_gremio
            FROM personajes p
            JOIN gremios g ON p.gremio_id = g.id
            WHERE g.id = %s
        ''', (gremio_id,))

        resultados = cursor.fetchall()

        if not resultados:
            print(f"La taberna esta vacia")
            return
        
        nombre_gremio = resultados[0][5]

        mi_gremio = Gremio(nombre_gremio)

        for fila in resultados:
            nombre, salud, tipo, armadura, mana, _ = fila

            if tipo == "Guerrero":
                pj = Guerrero(nombre, salud, armadura)
            elif tipo == "Mago":
                pj = Mago(nombre, salud, mana)

            mi_gremio.reclutar(pj)

        mi_gremio.listar_miembros()

    except Exception as e:
        print(f"Ocurrio un error al leer la base: {e}")
    finally:
        conexion.close()

if __name__ == '__main__':

    try:
        while True:

            print("Consola interactiva \n" + "*"*60)
            print("1.- Presione 1 para inicializar la base de Datos")
            print("2.- Presione 2 para fundar un nuevo Gremio")
            print("3.- Presione 3 para reclutar un aventurero")
            print("4.- Presione 4 para entrar a la Taberna")
            print("5.- Presione 5 para salir del juego")

            option = input("Seleccione la opcion deseada: ")

            if option == "1":
                inicializar_db()
            elif option =="2":
                fundar_gremio()
            elif option == "3":
                reclutar_aventurero()
            elif option == "4":
                ver_taberna()
            elif option == "5":
                break
            else:
                print("Opcion no valida")

    except KeyboardInterrupt:
        print ("El usuario detuvo el programa")
        sys.exit(0)