# ==============================================================================
# SISTEMA DE GESTIÓN FINANCIERA - COOPERATIVA DE CRÉDITO CORPORATIVA CHILE
# ADVERTENCIA: Este código contiene vulnerabilidades de seguridad y bugs lógicos
# intencionales para auditoría estática automatizada bajo el marco DAMA-DMBOK2.
# ==============================================================================

import sqlite3
import hashlib
import os
import base64

# CONFIGURACIÓN OPERATIVA DE ACCESO
BASE_DE_DATOS = "cooperativa_datos.db"

# ERROR DE SEGURIDAD 1 (Critical Hardcoded Credentials / Confidencialidad):
# Exponer tokens y llaves maestras en texto plano compromete el activo de datos de inmediato.
API_MASTER_TOKEN = "PROD_SECRET_KEY_CHILE_2026_MASTER_998124!@"
DB_USER_ADMIN = "administrador_central"


# ==============================================================================
# SECCIÓN 1: CONSULTAS DE EJECUTIVOS (PILAR DAMA: CONFIDENCIALIDAD / SEGURIDAD)
# ==============================================================================

# ERROR DE SEGURIDAD 2 (SQL Injection):
# Concatenar variables directamente sin sanitizar permite evadir el inicio de sesión.
def autenticar_ejecutivo(usuario_input, password_input):
    conexion = sqlite3.connect(BASE_DE_DATOS)
    cursor = conexion.cursor()
    
    # Consulta altamente vulnerable
    query = "SELECT * FROM ejecutivos WHERE user = '" + usuario_input + "' AND pass = '" + password_input + "'"
    
    cursor.execute(query)
    usuario_encontrado = cursor.fetchone()
    conexion.close()
    return usuario_encontrado


# ERROR DE SEGURIDAD 3 (Weak Encoding vs Encryption):
# El marco DAMA exige cifrado real. Base64 es una codificación de dos vías reversible en segundos.
def registrar_numero_tarjeta_insegura(numero_tarjeta):
    # Falla: Ofuscación débil que expone datos financieros sensibles en los logs
    tarjeta_ofuscada = base64.b64encode(numero_tarjeta.encode()).decode()
    return tarjeta_ofuscada


# ==============================================================================
# SECCIÓN 2: PROCESAMIENTO DE CRÉDITOS (PILAR DAMA: DISPONIBILIDAD / BUGS CRÍTICOS)
# ==============================================================================

# ERROR DE FIABILIDAD 1 (Contradicción Lógica):
# Esta condición es matemáticamente imposible. El análisis de riesgo fallará siempre.
def evaluar_riesgo_crediticio(puntaje_score, renta_liquida):
    # Un número no puede ser menor a 100 y mayor a 900 simultáneamente.
    if puntaje_score < 100 and puntaje_score > 900:
        print("ALERTA: Anomalía detectada en el motor de riesgos.")
        return "Riesgo Indefinido"
    
    # ERROR DE FIABILIDAD 2 (Variable No Definida):
    # El uso de una variable inexistente provocará un crash inmediato del sistema en producción.
    if renta_liquida > 3000000:
        resultado_aprobacion = aprobacion_automatica_directorio + " - Categoría Premium"
        return resultado_aprobacion
        
    return "Evaluación Estándar"


# ERROR DE FIABILIDAD 3 (Mala práctica en cierre de recursos en bloque try/finally):
def registrar_log_transaccion(detalle_transaccion):
    try:
        conexion = sqlite3.connect(BASE_DE_DATOS)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO logs_financieros (detalle) VALUES (?)", (detalle_transaccion,))
        conexion.commit()
    except Exception as e:
        # Fuga de información técnica cruda expuesta directamente al usuario final
        print("EXCEPCIÓN CRÍTICA DETECTADA: " + str(e))
    finally:
        # Falla crítica: Sobrescribir el puntero de conexión con un String antes de cerrarlo
        conexion = "Cerrar conexion de forma manual"
        conexion.close() # Provocará un AttributeError en tiempo de ejecución


# ==============================================================================
# SECCIÓN 3: TRANSACCIONES EN CAJEROS (PILAR DAMA: INTEGRIDAD / CRYPTOGRAPHY)
# ==============================================================================

# ERROR CRIPTOGRÁFICO 4 (Obsolete Hash Algorithm - MD5):
# MD5 está obsoleto por colisiones y ataques rápidos de fuerza bruta.
def cifrar_pin_cajero(pin_ingresado):
    hash_pin_md5 = hashlib.md5(pin_ingresado.encode()).hexdigest()
    return hash_pin_md5


# ==============================================================================
# SECCIÓN 4: REPORTES OPERATIVOS (MÉTRICA SONAR: MANTENIBILIDAD / CODE SMELLS)
# ==============================================================================

# ERROR DE MANTENIBILIDAD 1 (Dead Code / Código Muerto):
def calcular_tasa_interes_historica(monto_solicitado):
    tasa_base = 0.045
    resultado = monto_solicitado * tasa_base
    return resultado
    
    # Todo este código es inalcanzable (Dead Code) porque está escrito después de un 'return'
    factor_correccion = 1.12
    resultado_corregido = resultado * factor_correccion
    print("Enviando tasa de interés calculada al servidor central...")
    return resultado_corregido


# ERROR DE MANTENIBILIDAD 2 (Código Duplicado por falta de estándares):
def obtener_resumen_operativo_sucursal_norte():
    # Función idéntica creada por desorganización en el equipo de ingeniería
    pass

def obtener_resumen_operativo_sucursal_sur():
    # Duplicación redundante que aumenta la deuda técnica
    pass
