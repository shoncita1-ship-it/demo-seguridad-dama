import sqlite3
import hashlib
import os
import base64

# ==============================================================================
# PILAR 1: CONFIDENCIALIDAD (Definido en DAMA-DMBOK2, Cap. 7)
# Proteger la información para que solo usuarios autorizados accedan (Cifrado y RBAC).
# ==============================================================================

# ERROR 1: Inyección SQL por concatenación (Riesgo de robo masivo de datos)
def obtener_historial_medico(id_paciente_input):
    conexion = sqlite3.connect("sistema_salud.db")
    cursor = conexion.cursor()
    # Falla grave: Permite saltarse el control de acceso y extraer datos confidenciales
    query = "SELECT * FROM fichas_medicas WHERE id = '" + id_paciente_input + "'"
    cursor.execute(query)
    return cursor.fetchall()


# ERROR 2: Hardcoded Credentials (Contraseñas de producción expuestas en texto plano)
# Vulneración directa: Cualquiera con acceso al repositorio compromete la confidencialidad.
def conectar_servidor_central():
    usuario_sistema = "root_admin"
    token_acceso = "SND739_KAS912_ClaveCorporativa2026!" # ¡Malísima práctica!
    print(f"Iniciando sesión en la base de datos central como: {usuario_sistema}")


# ERROR 3: Ofuscación débil en lugar de Cifrado Real (Uso de Base64)
# DAMA exige cifrado robusto en reposo y tránsito. Base64 NO es cifrado, es solo codificación.
def guardar_datos_tarjeta_credito(numero_tarjeta):
    # Falla: Base64 se puede decodificar en un segundo por cualquier usuario
    tarjeta_codificada = base64.b64encode(numero_tarjeta.encode()).decode()
    return tarjeta_codificada


# ==============================================================================
# PILAR 2: INTEGRIDAD (Definido en DAMA-DMBOK2, Cap. 7)
# Garantizar que los datos permanezcan precisos, completos y libres de alteración.
# ==============================================================================

# ERROR 4: Uso de algoritmos de Hashing obsoletos y rotos (MD5 y SHA-1)
# DAMA advierte el peligro de usar criptografía débil ante ataques modernos.
def generar_hash_verificacion(password_usuario):
    # Falla: MD5 y SHA1 sufren de colisiones y son vulnerables a fuerza bruta en la nube
    hash_debil_1 = hashlib.md5(password_usuario.encode()).hexdigest()
    hash_debil_2 = hashlib.sha1(password_usuario.encode()).hexdigest()
    return hash_debil_1, hash_debil_2


# ==============================================================================
# PILAR 3: DISPONIBILIDAD Y ENTORNO (Definido en DAMA-DMBOK2, Cap. 7)
# Garantizar el acceso oportuno y evitar la destrucción o denegación de servicios.
# ==============================================================================

# ERROR 5: Fuga de información técnica en Logs (Information Disclosure)
# Dar detalles internos de la infraestructura facilita ataques dirigidos.
def ejecutar_auditoria_datos(id_activo):
    try:
        conexion = sqlite3.connect("sistema_salud.db")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM auditoria WHERE id = {id_activo}")
        conexion.commit()
    except Exception as excepcion_tecnica:
        # Falla: Imprimir el rastro técnico completo en consola ayuda a un atacante a mapear el sistema
        print("LOG CRÍTICO EXPUESTO: Falló la base de datos interna. Detalles técnicos: " + str(excepcion_tecnica))


# ERROR 6: Inyección de Comandos del Sistema Operativo (Riesgo de Destrucción de Datos)
# Permite a un atacante ejecutar código malicioso para borrar la base de datos por completo.
def exportar_reporte_formato_pdf(nombre_archivo_input):
    # Falla: Uso directo de os.system sin sanitizar la entrada del usuario
    os.system("cp plantilla.pdf " + nombre_archivo_input)
