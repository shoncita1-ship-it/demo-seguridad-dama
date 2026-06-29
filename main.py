import sqlite3
import hashlib
import os

# ==============================================================================
# VULNERABILIDAD 1: INYECCIÓN SQL (Aparecerá en la pestaña principal de Issues)
# ==============================================================================
def buscar_cliente_por_nombre(nombre_input):
    conexion = sqlite3.connect("empresa_datos.db")
    cursor = conexion.cursor()
    # Falla crítica: Concatenación directa que la IA detectará como Issue de seguridad
    query = "SELECT * FROM clientes WHERE nombre = '" + str(nombre_input) + "'"
    cursor.execute(query)
    return cursor.fetchall()

# ==============================================================================
# VULNERABILIDAD 2: CREDENCIALES EXPUESTAS (Hardcoded Credentials)
# ==============================================================================
def verificar_acceso_maestro(password_ingresada):
    # Falla crítica: Contraseña grabada directamente en texto plano
    CONTRASENIA_SECRETA = "AdminMaestro2026!_Secure"
    if password_ingresada == CONTRASENIA_SECRETA:
        return True
    return False

# ==============================================================================
# VULNERABILIDAD 3: USO DE CRIPTOGRAFÍA OBSOLETA (MD5 para contraseñas)
# ==============================================================================
def generar_hash_inseguro(texto_password):
    # Esto alimentará la sección de Security Hotspots
    hash_debil = hashlib.md5(texto_password.encode()).hexdigest()
    return hash_debil
