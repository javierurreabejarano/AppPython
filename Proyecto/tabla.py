import sqlite3

conexion = sqlite3.connect("basededatos.bd")
try:
    conexion.execute("""
                     create table articulos (
                         codigo integer primary key autoincrement,
                         descripcion text,
                         precio real
                     )""")
    print("Se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close()
