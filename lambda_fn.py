calcular_impuesto = lambda venta: venta*1.16

venta_iva = calcular_impuesto(453)

print(venta_iva)

calcular_impuesto = lambda precio: round(precio*1.35,2)
print(f"El precio de 780 con impuesto calculado es de: {calcular_impuesto(780)}")

etiqueta = lambda cantidad: "MAYOREO" if cantidad >= 10 else "MENUDEO"
print(f"Tu venta es de tipo: {etiqueta(70)}")

producto = "ALARM CLOCK BAKELINE PINK"

obtener_cat = lambda categoria: categoria.split()[0]

categoria = obtener_cat(producto)
print(categoria)

inventario = [
    ("CIRCUS PARADE LUNCH BOX", 1.95),
    ("DOORMAT RED RETROSPOT", 7.08),
    ("STRAWBERRY TRINKET BOX", 1.25),
    ("CHRISTMAS GLASS BALL", 6.95)
]

inventario.sort(key=lambda x: x[1], reverse=True)

# for item in inventario:
#     print(f"    - {item[0]}: ${item[1]}")

leads = [
    {"nombre": "Empresa A", "presupuesto": 2000, "estado": "Nuevo"},
    {"nombre": "Empresa B", "presupuesto": 8000, "estado": "Contactado"},
    {"nombre": "Empresa C", "presupuesto": 15000, "estado": "Nuevo"},
    {"nombre": "Empresa D", "presupuesto": 5000, "estado": "Cerrado"}
]

lead_ordenados = sorted(leads, key=lambda x: x['presupuesto'])

# for l in lead_ordenados:
#     print(f"    - {l['nombre']}: ${l['presupuesto']}")

leads_nuevos = list(filter(lambda x: x["estado"] == "Nuevo",leads))
print(leads_nuevos)

for l in leads_nuevos:
    print(f"    - {l['nombre']} es nuevo y tiene un presupuesto de: {l['presupuesto']}")

nombres_editados = list(map(lambda x: x['nombre'].upper(), leads))

for n in nombres_editados:
    print(f"Nombre convertido: {n}")

print(nombres_editados)