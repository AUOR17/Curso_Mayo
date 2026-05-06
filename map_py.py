inventario = [
    {"sku": "A1", "producto": "LAPTOP gamer", "precio_str": "$1200.50", "moneda": "USD"},
    {"sku": "B2", "producto": "ratón Inalámbrico", "precio_str": "€45.00", "moneda": "EUR"},
    {"sku": "C3", "producto": "TECLADO MECÁNICO", "precio_str": "$85.99", "moneda": "USD"}
]

TASA_CONVERSION = 1.08

def normalizar_producto(item: dict) -> dict:

    precio = float(item['precio_str'].replace("$", '').replace("€", ""))

    if item['moneda'] == "EUR":
        precio = round(precio * TASA_CONVERSION, 2)

    return  {
        "sku": item["sku"], 
        "producto":  item["producto"].title(),
        "precio_usd": precio
    }

inventario_limpio = list(map(normalizar_producto, inventario))

for prod in inventario_limpio:
    print(f" - {prod["sku"]} | {prod["producto"]} | {prod["precio_usd"]}")