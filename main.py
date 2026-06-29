import sqlite3

# VULNERABILIDAD CRÍTICA: Concatenar variables expone los datos a Inyección SQL
def consultar_base_datos(usuario_input):
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()
    
    # Error grave de seguridad de datos:
    query = "SELECT * FROM usuarios WHERE nombre = '" + usuario_input + "'"
    
    cursor.execute(query)
    return cursor.fetchall()
