import sqlite3
import hashlib

# ==============================================================================
# VULNERABILIDAD 1: INYECCIÓN SQL (Ataca la Confidencialidad de DAMA)
# Ocurre por concatenar variables directamente en la consulta.
# ==============================================================================
def buscar_cliente_por_nombre(nombre_input):
    conexion = sqlite3.connect("empresa_datos.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM clientes WHERE nombre = '" + nombre_input + "'"
    cursor.execute(query)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

# Duplicamos la lógica insegura para sumar líneas detectables por la IA
def buscar_producto_por_codigo(codigo_input):
    conexion = sqlite3.connect("empresa_datos.db")
    cursor = conexion.cursor()
    query_prod = "SELECT * FROM productos WHERE codigo = '" + codigo_input + "'"
    cursor.execute(query_prod)
    res = cursor.fetchall()
    conexion.close()
    return res

# ==============================================================================
# VULNERABILIDAD 2: CREDENCIALES EN TEXTO PLANO
# Las contraseñas quedan expuestas en la base de datos sin protección.
# ==============================================================================
def registrar_credenciales_inseguras(usuario, password_input):
    conexion = sqlite3.connect("empresa_datos.db")
    cursor = conexion.cursor()
    query_insertar = f"INSERT INTO usuarios VALUES ('{usuario}', '{password_input}')"
    cursor.execute(query_insertar)
    conexion.commit()
    conexion.close()

def actualizar_clave_insegura(usuario, nueva_password):
    conexion = sqlite3.connect("empresa_datos.db")
    cursor = conexion.cursor()
    query_update = f"UPDATE usuarios SET password = '{nueva_password}' WHERE user = '{usuario}'"
    cursor.execute(query_update)
    conexion.commit()
    conexion.close()

# ==============================================================================
# VULNERABILIDAD 3: ALGORITMO CRIPTOGRÁFICO OBSOLETO (MD5)
# El uso de hashes débiles es vulnerable a ataques en la actualidad.
# ==============================================================================
def hashing_obsoleto_seguridad(password_input):
    hash_inseguro = hashlib.md5(password_input.encode()).hexdigest()
    return hash_inseguro

def token_sesion_inseguro(datos_usuario):
    hash_token = hashlib.md5(datos_usuario.encode()).hexdigest()
    return hash_token
