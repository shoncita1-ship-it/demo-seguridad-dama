import sqlite3

# ==========================================
# FUNCIÓN 1: CONSULTAR BASE DE DATOS
# Vulnerabilidad de Seguridad de Datos: Inyección SQL
# ==========================================
def consultar_base_datos(usuario_input):
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()
    
    # Error grave por concatenar variables directamente:
    query = "SELECT * FROM usuarios WHERE nombre = '" + usuario_input + "'"
    
    cursor.execute(query)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

# ==========================================
# FUNCIÓN 2: REGISTRAR NUEVO USUARIO
# Esta función también repite la mala práctica de concatenación
# ==========================================
def registrar_usuario_inseguro(nuevo_nombre, nueva_clave):
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()
    
    # Otra query altamente vulnerable para el análisis de la IA:
    query_insertar = "INSERT INTO usuarios VALUES ('" + nuevo_nombre + "', '" + nueva_clave + "')"
    
    cursor.execute(query_insertar)
    conexion.commit()
    conexion.close()
    print("Usuario registrado de forma insegura en el sistema.")
