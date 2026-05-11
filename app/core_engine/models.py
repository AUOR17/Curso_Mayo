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

    def __str__(self): # print(Personaje)
        return f"{self.nombre} | HP: {self.salud} / {self.salud_maxima}"
    
class Guerrero(Personaje):

    def __init__(self, nombre, salud_maxima, puntos_armadura):
        super().__init__(nombre, salud_maxima)        
        self.puntos_armadura = puntos_armadura

    def __str__(self):
        ficha_base = super().__str__()
        return f"Guerrero: {ficha_base} | Armadura: {self.puntos_armadura}"
    
class Mago(Personaje):
    def __init__(self, nombre, salud_maxima, mana_maximo):
        super().__init__(nombre, salud_maxima)
        self.mana_maximo = mana_maximo
        self._mana = mana_maximo

    def lanzar_hechizo(self,costo_mana):

        if self._mana >= costo_mana:
            self._mana -= costo_mana
            print(f"El mago {self.nombre} ha lanzado un hechiizo con {costo_mana} MP ")
        else:
            print(f"{self.nombre} se ha quedad sin mana")

    def __str__(self):
        ficha_base = super().__str__()
        return f"Mago: {ficha_base} | Mana: {self._mana}/{self.mana_maximo}"
    
class JefeFinal(Personaje):

    def __init__(self, nombre, salud_maxima, multiplicador_dano):
        super().__init__(nombre, salud_maxima)
        self.multiplicador_dano = multiplicador_dano
        self.enfurecido = False

    def recibir_dano_critico(self, cantidad):
        self.salud -= cantidad

        if 0 < self.salud <= (self.salud_maxima * 0.3) and not self.enfurecido:
            self.enfurecido = True
            self.multiplicador_dano *= 2
            print(f"El cielo se oscurece, pues el {self.nombre} ha entrado a la fase 2")
            print(f" Su multiplicador de daño subio a {self.multiplicador_dano}x")   

    def __str__(self):
        ficha_bae = super().__str__()
        estado = "Enfurecido" if self.enfurecido else "Acechando"
        return f"Jefe: {ficha_bae} | Daño: {self.multiplicador_dano} | Estado: {estado}"
    
class Gremio:

    def __init__(self, nombre_gremio):
        self.nombre_gremio = nombre_gremio
        self.miembros = []

    def reclutar(self, nuevo_personaje:Personaje): 
        self.miembros.append(nuevo_personaje)
        print(f"{nuevo_personaje.nombre} se ha unido al gremio {self.nombre_gremio}")

    def listar_miembros(self):

        if not self.miembros:
            print("El gremio esta vacio.")
        else:
            for miembro in self.miembros:
                print(miembro)
        
        print("-"*60)