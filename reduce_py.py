from functools import reduce

ventas_sucursales = [
    {"Laptops": 5000, "Smartphones": 3000, "Accesorios": 500},
    {"Laptops": 2000, "Smartphones": 4500, "Accesorios": 1200},
    {"Laptops": 8000, "Smartphones": 1500, "Accesorios": 300},
    {"Monitores": 4000, "Accesorios": 800} # Esta sucursal vendió algo nuevo
]

def consolidar_reporte(datos: dict, reporte_actual:dict) -> dict:

    copia = datos.copy()

    for categoria, monto in reporte_actual.items():

        if categoria in copia.items():
            copia[categoria] += monto
        else:
            copia[categoria] = monto

    return copia

reporte_completo = reduce(consolidar_reporte, ventas_sucursales,{})

for categoria, total in sorted(reporte_completo.items(), key=lambda x: x[1], reverse=True):
    print(f"  - {categoria.ljust(15)}: ${total:,.2f}")