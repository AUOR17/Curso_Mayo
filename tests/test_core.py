import pytest
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from core_engine.models import Guerrero, Mago, JefeFinal, Gremio
from core_engine.database import iniciaizar_db, obtener_conexion

@pytest.fixture
def db_limpia():

    ruta_db = "partida_guardada.db"
    if os.path.exists(ruta_db):
        os.remove(ruta_db)
    
    iniciaizar_db()

    yield

    if os.path.exists(ruta_db):
        os.remove(ruta_db)

def test_reglas_encapsulamiento():

    kratos = Guerrero("kratos", salud_maxima=100, puntos_armadura=40)

    kratos.salud = -5000

    assert kratos.salud == 0

    kratos.salud = 99999
    assert kratos.salud == 100

@pytest.mark.parametrize("clase_personaje, nombre, salud_max, atributo_extra", [
    (Guerrero, "Arthur", 120, 50),
    (Mago, "Merlin", 80, 200),
    (JefeFinal, "browser", 500, 1.5)
])
def test_creacion_personaje_npc(clase_personaje, nombre, salud_max, atributo_extra):

    personaje_creado = clase_personaje(nombre, salud_max, atributo_extra)

    assert personaje_creado.nombre == nombre
    assert personaje_creado.salud_maxima == salud_max

    if isinstance(personaje_creado, Mago):
        assert personaje_creado.mana_maximo == 200
    elif isinstance(personaje_creado, JefeFinal):
        assert personaje_creado.enfurecido == False
    elif isinstance(personaje_creado, Guerrero):
        assert personaje_creado.puntos_armadura == 50