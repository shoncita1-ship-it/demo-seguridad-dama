import sqlite3
import hashlib

# ==============================================================================
# VULNERABILIDAD 1: INYECCIÓN SQL (Ataca la Confidencialidad e Integridad - Tríada CIA)
# Permite a un atacante robar o borrar toda la base de datos de la empresa.
# ==============================================================================
def buscar_cliente_por_nombre(nombre_input):
    conexion = sqlite3.connect("empresa_datos.db")
    cursor = conexion.cursor()
    
    # ERROR CRÍTICO: Concatenar variables permite inyección de código malicioso
    query = "SELECT * FROM clientes WHERE nombre = '" + nombre_input + "'"
    
    cursor.execute(query)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado


# ==============================================================================
# VULNERABILIDAD 2: CONTRASENIAS EN TEXTO PLANO (Ataca la Confidencialidad)
# Si un atacante entra al sistema, verá las claves de todos los usuarios sin filtro.
# ==============================================================================
def registrar_credenciales_inseguras(usuario, password_input):
    conexion = sqlite3.connect("empresa_datos.db")
    cursor = conexion.cursor()
    
    # ERROR CRÍTICO: Guardar la contraseña tal cual la escribe el usuario, sin encriptar
    query = f"INSERT INTO usuarios (user, password) VALUES ('{usuario}', '{password_input}')"
    
    cursor.execute(query)
    conexion.commit()
    conexion.close()


# ==============================================================================
# VULNERABILIDAD 3: ALGORITMO DE ENCRIPTACIÓN DESTRUIDO / OBSOLETO (MD5)
# MD5 ya no es seguro; se puede romper por "fuerza bruta" en pocos segundos en la nube.
# ==============================================================================
def hashing_obsoleto_seguridad(password_input):
    # ERROR CRÍTICO: Utilizar MD5 en pleno 2026 para proteger datos sensibles
    hash_inseguro = hashlib.md5(password_input.encode()).hexdigest()
    return hash_inseguro
