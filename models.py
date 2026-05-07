from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
    
    def get_full_name(self):
        return f"{self.nombre} {self.apellido} {self.email}"
    
class Lead(Persona):
    def __init__(self, nombre, apellido, email, presupuesto_estimado):
        super().__init__(nombre, apellido, email)
        self.estado = "Prospecto"
        self._presupuesto_estimado = 0
        self._presupuesto_estimado = presupuesto_estimado

    @property
    def presupuesto_estimado(self):
        return self._presupuesto_estimado

    @presupuesto_estimado.setter
    def presupuesto_estimado(self,valor):
        if valor < 0:
            print("Error, el presupuesto no puede ser negativo")
        else:
            self._presupuesto_estimado = valor
    
    def convert_to_customer(self):
        self.estado = "Cliente"
        print(f"{self.get_full_name()} ahora es un cliente")

class Vendedor(Persona):
    def __init__(self, nombre, apellido, email, n_empleado):
        super().__init__(nombre, apellido, email)
        self.n_empleado = n_empleado
        self.ventas_totales = 0

    def registar_venta(self,monto):
        self.ventas_totales += monto
        print(f"{self.get_full_name()} registro una venta. Total acumado: $ {self.ventas_totales}")

class IRepositorioEscritura(ABC):
    @abstractmethod
    def guardar_datos(self, entidad):
        pass

class IRepositorioLectura(ABC):
    @abstractmethod
    def obtener_datos(self):
        pass

class LeadRepository(IRepositorioEscritura, IRepositorioLectura):
    def __init__(self):
        self._db_sim = []

    def guardar_datos(self, lead: Lead):
        self._db_sim.append(lead)
        print(f" [DB], se ha guardado a {lead.email}")

    def obtener_datos(self):
        return self._db_sim
    
class VendedorRepository(IRepositorioEscritura):
    def __init__(self):
        self._db_sim = []

    def guardar_datos(self, vendedor: Vendedor):
        self._db_sim.append(vendedor)
        print(f" [DB], se ha guardado a {vendedor.n_empleado}")

class LeadService:
    def __init__(self, repositorio: IRepositorioEscritura):
        self.repositorio = repositorio

    def registar_nuevo_lead(self, nombre, apellido, email, presupuesto):
        print(f" Iniciando registro para: {email}")

        if "@" not in email:
            print(F"El eroor es que el email {email} no tiene un formato valido")
            return None

        nuevo_lead = Lead(nombre, apellido, email, presupuesto)
        self.repositorio.guardar_datos(nuevo_lead)
        self._enviar_email_bienvenida(nuevo_lead)
        return nuevo_lead
    
    def _enviar_email_bienvenida(self, lead:Lead):
        print(f" Mandando correo de bienvenida a: {lead.email}")

class VendedorService:
    def __init__(self, repositorio: IRepositorioEscritura):
        self.repositorio = repositorio

    def contratar_vendedor(self, nombre, apellido, email, n_empleado):

        print(f"[RRHH] Iniciando contratacion para: {nombre} {apellido}")

        if not str(n_empleado).startswith("V-"):
            print(f"Error, el gafete {n_empleado} es invalido")
            return None

        nuevo_vendedor = Vendedor(nombre, apellido, email, n_empleado)
        self.repositorio.guardar_datos(nuevo_vendedor)
        print(f"[RRH] {nuevo_vendedor.get_full_name()} ha sido dado de alta con exito")
        # Verificar que el n_empleado empiece con "v-"
        # guardar_datos la vendedor en caso de que todo este en orden
        return nuevo_vendedor


if __name__ == '__main__':
    
    repo_lead_memoria = LeadRepository()
    repo_vendedor_memoria = VendedorRepository()

    servicio_leads = LeadService(repo_lead_memoria)
    servicio_vendedor = VendedorService(repo_vendedor_memoria)

    lead_valido = servicio_leads.registar_nuevo_lead("Ana", "Flores", "ana@live.com", 6000)
    vendedor_estrella = servicio_vendedor.contratar_vendedor("Luis", "Martinez", "luis@yahoo.com", "V-12212421")

    if vendedor_estrella and lead_valido:
        lead_valido.convert_to_customer()
        vendedor_estrella.registar_venta(lead_valido.presupuesto_estimado)