import pytest

from models import LeadService, LeadRepository, VendedorService, VendedorRepository

@pytest.fixture
def servicio_leads():
    '''
    Entrega un LeadService con su repo limpio
    '''
    repo_leads = LeadRepository()
    return LeadService(repo_leads)

@pytest.fixture
def servicio_vendedores():
    '''
    Entrega un VendedorService con su repo limpio
    '''
    repo_vendedores = VendedorRepository()
    return VendedorService(repo_vendedores)


def test_registar_lead_exitoro(servicio_leads):

    lead = servicio_leads.registar_nuevo_lead("juan", "perex", "juan@ejemplo.com", 4000)

    assert lead is not None
    assert lead.nombre == "juan"
    assert lead.apellido == "perex"
    assert lead.email == "juan@ejemplo.com"
    assert lead.presupuesto_estimado == 4000
    assert lead.estado == "Prospecto"

def test_registar_vendedor_exitoro(servicio_vendedores):

    vendedor = servicio_vendedores.contratar_vendedor("maria", "gomez", "maria@ejemplo.com", "V-123")

    assert vendedor is not None
    assert vendedor.nombre == "maria"
    assert vendedor.apellido == "gomez"
    assert vendedor.email == "maria@ejemplo.com"
    assert vendedor.n_empleado == "V-123"

def test_contratar_vendedor_gafete_invalido(servicio_vendedores):

    vendedor = servicio_vendedores.contratar_vendedor("carlos", "lopez", "carlos@live.com", "123")

    assert vendedor is None

def test_registar_lead_email_invalido(servicio_leads):

    lead = servicio_leads.registar_nuevo_lead("ana", "flores", "ana_live.com", 6000)

    assert lead is None

# parametrize con emails y gafete

@pytest.mark.parametrize("email_prueba, esperado_exitoso", [
    ("juan@ejemplo.com", True),
    ("ana.gomez@empresa.mx", True),
    ("correo-falso.com", False),
    ("sin_dominio@", True), 
    ("", False)
])
def test_registrar_lead_varios_emails(servicio_leads, email_prueba, esperado_exitoso):
    lead = servicio_leads.registar_nuevo_lead("test", "gomez", email_prueba, 10000)

    if esperado_exitoso:
        assert lead is not None
        assert lead.email == email_prueba
    else:
        assert lead is None

@pytest.mark.parametrize("gafete_prueba, esperado_exitoso", [
    ("V-001", True),
    ("V-9999", True),
    ("12345", False),
    ("v-001", False), 
    ("A-001", False)
])
def test_contratar_vendedor_varios_gafetes(servicio_vendedores, gafete_prueba, esperado_exitoso):
    vendedor = servicio_vendedores.contratar_vendedor("Test", "Ventas", "ventas@test.com", gafete_prueba)

    if esperado_exitoso:
        assert vendedor is not None
        assert vendedor.n_empleado == gafete_prueba
    else:
        assert vendedor is None