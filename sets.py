sets = {}
print(type(sets).__name__)

sets_1 = set()
print(type(sets_1).__name__)

sets_2 = {1,2,3,4,5,6,7,8,9,10}
print(type(sets_2).__name__)

etiquetas = ["urgente", "tecno", "urgente", "seguimiento", "tecno", "vip"]

etiqetas_limpias = set(etiquetas)
print(etiqetas_limpias)

compraron_software = {"TechCorp", "InnovaTech", "PymeSol"}
compraron_hardware = {"PymeSol", "Global IT", "TechCorp"}

clientes_hibridos = compraron_software & compraron_hardware
print(clientes_hibridos)

only_soft = compraron_software - compraron_hardware
print(only_soft)

todos_clientes = compraron_software | compraron_hardware
print(todos_clientes)

print(f"Etiquetas antes del cambio: {etiqetas_limpias}")

etiqetas_limpias.add("enterpise corporation in the wolrd")
etiqetas_limpias.discard("cool")

print(f"Etiquetas limpias despues del cambio: {etiqetas_limpias}")