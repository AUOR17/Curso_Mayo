import sqlite3

conexion = sqlite3.connect("db_local.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, 
        empresa TEXT NOT NULL, 
        presupuesto REAL    
    )
''')

nuevo_lead = ("Sara Coonor", "Skynet", 150000.0)

cursor.execute('''
    INSERT INTO leads (nombre, empresa, presupuesto)
    VALUES (?,?,?)
''', nuevo_lead)

# conexion.commit()

cursor.execute("SELECT * FROM leads")

registros =  cursor.fetchall()

# print(registros)

for lead in registros:

    print(f"    -ID: {lead[0]} | Nombre: {lead[1]} | Empresa: {lead[2]} | Presupuesto: {lead[3]}")