
class Personaje:
    def __init__(self, nombre, salud_maxima):
        self.nombre = nombre
        self._salud = salud_maxima
        self.salud_maxima = salud_maxima
        self.inventario = ["Pocion chica", "Pan seco"]

    @property
    def salud(self):
        return self._salud
    
    @salud.setter
    def salud(self,nueva_salud):

        if nueva_salud <= 0:
            self._salud = 0
            print(f"{self.nombre} ha caido en batalla")
        elif nueva_salud > self.salud_maxima:
            self._salud = self.salud_maxima
        else:
            self._salud = nueva_salud
            print(f"La salud del perosnaje {self.nombre} ha sido actualizada: {self._salud}/{self.salud_maxima}")

    @salud.deleter # del Personaje.salud
    def salud(self):
        print(f"Intent de borrar la salud de {self.nombre}")
        print(f"Operacion denegada.")

    def _efecto_sonido_curacion(self):
        print(f"[Efecto de sonido: glug glug]")

    def tomar_pocion(self,cantidad_curacion):
        print(f"{self.nombre} intenta tomar una pocion de +{cantidad_curacion} HP")

        self._efecto_sonido_curacion()

        self.salud = self.salud + cantidad_curacion

    def __str__(self): # print(Personaje)
        return f" Personaje: {self.nombre} | HP: {self.salud} / {self.salud_maxima}"
    
    def __repr__(self):
        return f" Personaje({self.nombre}, {self.salud_maxima})"
    
    def __gt__(self, otro_personaje):  # Personaje 1 > Personaje 2
        return self.salud_maxima > otro_personaje.salud_maxima
    
    def __add__(self,otro_personaje): # Personaje 1 + Personaje 2
        print(f"Fusion entre: {self.nombre} + {otro_personaje.nombre}")

        nuevo_nombre = f"{self.nombre[:3]}{otro_personaje.nombre[3:]}"
        nueva_salud = self.salud_maxima + otro_personaje.salud_maxima

        return Personaje(nuevo_nombre,nueva_salud)
    
    def __len__(self): # len(Personaje)
        return len(self.inventario)
    
    @classmethod
    #Personaje("chuchito", 03242)
    def crear_npc_basico(cls):
        return cls(nombre= "Aldeano Generico", salud_maxima=10)
    
    @staticmethod
    def mostrar_manual():
        print("\n Manual del Juego")
        print("1. La salud maxima no puede superarse")
        print("2. Si la salud llega a 0, el personaje muere")
        print("3. Usa pociones con sabiduria")

class Guerrero(Personaje):

    def __init__(self, nombre, salud_maxima, puntos_armadura):
        super().__init__(nombre, salud_maxima)        
        self.puntos_armadura = puntos_armadura

    def recibir_dano(self, dano_enemigo): 

        dano_real = dano_enemigo - self.puntos_armadura
        if dano_real < 0:
            dano_real = 0

        self.salud = self.salud - dano_real

    def __str__(self):
        ficha_base = super().__str__()
        return f"{ficha_base} | Armadura: {self.puntos_armadura}"

    @classmethod
    def crear_guerrero(cls):
        return cls(nombre = "Espartano", salud_maxima=200, puntos_armadura=50)
    
def encapsulamiento():

    arthur = Personaje("Arthur", 50)

    arthur._salud = "Dios"

    try:
        porcentaje = (arthur._salud / arthur.salud_maxima) * 100
    except TypeError as e:
        print(f"El juego se cerro por le error: {e}")
    
    arthur._salud = 10
    arthur.tomar_pocion(100)

def herencia():
    arthur = Personaje("Arthur", 50)
    leonel = Guerrero("Leonel", 100, 20)

    leonel.recibir_dano(25)

    try:
        print(arthur.puntos_armadura)
    except AttributeError:
        print("Error, arthur es un personaje base y no tiene armadura")

def metodos_magicos():
    arthur = Personaje("Arthur", 50)
    leonel = Guerrero("Leonel", 100, 20)

    print(arthur)
    print(repr(arthur))

    if leonel > arthur:
        print("Kratos es mas poderoso")

    guerrero_nuevo = arthur + leonel
    print(guerrero_nuevo.nombre)


    arthur.inventario.append("Excalibur")
    print(len(arthur))

def decoradores():
    Personaje.mostrar_manual()

    npc = Personaje.crear_npc_basico()
    print(npc)

    soldado = Guerrero.crear_guerrero()
    print(soldado)

    del npc.salud    

if __name__ == '__main__':
    decoradores()


    
    
