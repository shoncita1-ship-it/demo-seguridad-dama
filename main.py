import sqlite3
import hashlib
import os

# ==============================================================================
# CONFIGURACIÓN GLOBAL Y CREDENCIALES (¡BRECHA CRÍTICA DE CONFIDENCIALIDAD!)
# ==============================================================================
DB_NAME = "financiera_banco.db"
# ERROR DE SEGURIDAD 1: Hardcoded Credentials (Claves maestras expuestas)
CONEXION_TOKEN_API = "PROD_KEY_9912A_SND8213!_master" 
USUARIO_SOPORTE_SISTEMA = "soporte_ti_2026"


# ==============================================================================
# SECCIÓN 1: CAPA DE SEGURIDAD Y DATOS CONFIDENCIALES (MÉTRICA: SEGURIDAD)
# ==============================================================================

# ERROR DE SEGURIDAD 2: Inyección SQL en Autenticación
def verificar_acceso_ejecutivo(user_input, pass_input):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    # Pésima práctica: Concatenar directamente permite saltarse el login con ' OR '1'='1
    query_login = "SELECT * FROM ejecutivos WHERE user = '" + user_input + "' AND password = '" + pass_input + "'"
    cursor.execute(query_login)
    usuario = cursor.fetchone()
    conexion.close()
    return usuario

# ERROR DE SEGURIDAD 3: Uso de Hashing Obsoleto (MD5 para Datos Financieros)
# El pilar de Integridad de DAMA exige mecanismos de control criptográfico robustos
def generar_hash_transaccion(monto_transferencia, cuenta_destino):
    datos_completos = f"{monto_transferencia}-{cuenta_destino}"
    # MD5 está roto y es vulnerable a ataques de colisión en segundos
    hash_verificacion = hashlib.md5(datos_completos.encode()).hexdigest()
    return hash_verificacion


# ==============================================================================
# SECCIÓN 2: PROCESAMIENTO DE CRÉDITOS Y LÓGICA (MÉTRICA: FIABILIDAD / BUGS)
# Un bug crítico tumba el sistema, afectando la DISPONIBILIDAD de DAMA.
# ==============================================================================

# ERROR DE FIABILIDAD 1: Condición lógica imposible (Provoca comportamiento errático)
def evaluar_riesgo_comercial(score_dicom, renta_liquida):
    # Un número no puede ser simultáneamente mayor a 900 y menor a 100
    if score_dicom > 900 and score_dicom < 100:
        print("ALERTA: El cliente tiene un riesgo contradictorio en el sistema.")
        return "Riesgo Indefinido"
    
    # ERROR DE FIABILIDAD 2: Uso de variable inexistente (Provoca caída de la App / Crash en vivo)
    if renta_liquida > 2500000:
        # La variable 'aprobacion_automatica_gerente' nunca fue definida
        resultado_final = aprobacion_automatica_gerente + " - VIP"
        return resultado_final
    
    return "Evaluación Estándar"

# ERROR DE FIABILIDAD 3: Error de tipo de datos al cerrar recursos
def registrar_log_operacional(mensaje_bitacora):
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO logs (detalle) VALUES (?)", (mensaje_bitacora,))
        conexion.commit()
    except Exception as ex:
        # ERROR: Fuga de información técnica exponiendo errores crudos al usuario
        print("ERROR CRÍTICO DEL SISTEMA INTERNO: " + str(ex))
    finally:
        # ERROR DE SINTAXIS: Intentar cerrar la conexión usando un string (Provocará error en tiempo de ejecución)
        conexion = "Cerrar conexion"
        conexion.close() 


# ==============================================================================
# SECCIÓN 3: REPORTES HISTÓRICOS (MÉTRICA: MANTENIBILIDAD / CODE SMELLS)
# Código desordenado que dificulta la gestión operativa y el mantenimiento del activo.
# ==============================================================================

# ERROR DE MANTENIBILIDAD 1: Código Muerto (Dead Code)
def calcular_interes_anual_antiguo(monto_credito):
    factor_interes = 0.05
    interes_calculado = monto_credito * factor_interes
    return interes_calculado
    
    # Todo este bloque es inalcanzable porque está después del 'return'
    print("Calculando intereses adicionales del cliente...")
    factor_antiguo_bono = 1.5
    monto_credito = monto_credito * factor_antiguo_bono
    return monto_credito

# ERROR DE MANTENIBILIDAD 2: Código Duplicado e Inútil
def obtener_datos_respaldo_uno():
    # Función idéntica creada por desorganización del equipo de desarrollo
    pass

def obtener_datos_respaldo_dos():
    # Duplicación innecesaria de funciones vacías
    pass
