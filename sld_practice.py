#Base de Conocimiento
HECHOS = {
    "gastos": {
        "fijos": {
            "renta": "alta", "electricidad": "alta", "telefono/internet": "media", 
            "agua": "alta", "seguros": "media"
        },
        "variables": {
            "transporte": "media", "ropa": "baja", "entretenimiento": "baja", 
            "comida": "alta", "intereses_deuda": "alta"
        }
    }
}


# Para poder calcular y usar las reglas 50/30/20, se necesitan valores monetarios.
# Ejemplo de ingresos y una escala de gasto simple (100 para baja, 200 para media, 400 para alta).

INGRESOS_EJEMPLO = 3000

GASTOS_VALOR = {
    "baja": 100,
    "media": 200,
    "alta": 400
}

def calcular_suma_gastos(gastos_hechos, valores):
    """Calcula la suma total de gastos monetarios."""
    suma = 0
    for tipo_gasto in gastos_hechos["gastos"].values():
        for gasto, prioridad in tipo_gasto.items():
            # Para manejar el formato "media/alta"
            if "/" in prioridad:
                prioridad = prioridad.split('/')[0] # Usaremos el primero como dominante (media)
            
            # USe obtiene el valor asociado al hecho (prioridad)
            valor_gasto = valores.get(prioridad, 0)
            suma += valor_gasto
    return suma

def procesar_consulta(consulta, ingresos, hechos):
    suma_total_gastos = calcular_suma_gastos(hechos, GASTOS_VALOR)
    
    # Consulta: ¿Mis gastos requieren ajustes? (Regla de la Cláusula 1)
    if "¿Mis gastos requieren ajustes?" in consulta:  
        if ingresos < suma_total_gastos:
            ajuste_necesario = "Si"
        else:
            ajuste_necesario = "No"
            
        print(f"--- Unificación (Ajuste) ---")
        print(f"Hecho: Ingresos({ingresos}) < SumaTotalGastos({suma_total_gastos})")
        print(f"Sustitución: {{'?I': {ingresos}, '?G': {suma_total_gastos}}}")
        print("----------------------------")
        
        return f"**Respuesta:** La suma de sus gastos estimados es ${suma_total_gastos} y su ingreso es ${ingresos}. Por lo tanto, **{ajuste_necesario}** requiere ajustes."

   
    # Consulta: ¿Qué gastos puedo reducir? (Reglas de Ajuste)
    elif "¿Qué gastos puedo reducir?" in consulta:
        ajuste_necesario = ingresos < suma_total_gastos
        
        if not ajuste_necesario:
            return "Sus gastos no requieren un ajuste inmediato según esta base de conocimiento."
            
        recortes = []
        
        # Regla: Si se requiere ajuste los gastos de prioridad baja son los primeros en recortarse
        gastos_bajos = [g for g, p in hechos["gastos"]["variables"].items() if p == "baja"]
        if gastos_bajos:
            recortes.append(f"1. Prioridad **Baja**: {', '.join(gastos_bajos)}")
        
        # Regla: Si se requiere ajuste y los ajustes de prioridad baja no son suficientes se recortar gastos de prioridad media.
        gastos_medios = [g for g, p in hechos["gastos"]["fijos"].items() if p.startswith("media")]
        gastos_medios += [g for g, p in hechos["gastos"]["variables"].items() if p.startswith("media")]
        if gastos_medios:
            recortes.append(f"2. Prioridad **Media**: {', '.join(gastos_medios)}")
            
        # Regla: Si se requiere ajuste y los gastos de prioridad baja y media no son suficientes se recortan gastos variables de prioridad alta
        gastos_altos_variables = [g for g, p in hechos["gastos"]["variables"].items() if p == "alta"]
        if gastos_altos_variables:
            recortes.append(f"3. Prioridad **Alta (Variables)**: {', '.join(gastos_altos_variables)}")
            
        # Regla: Los gastos fijos de prioridad alta no pueden recortarse
        gastos_altos_fijos = [g for g, p in hechos["gastos"]["fijos"].items() if p == "alta"]
        
        respuesta = "Según la regla de ajuste, debe priorizar recortes en el siguiente orden:\n" + "\n".join(recortes)
        respuesta += f"\n\n**Nota:** Los gastos fijos de prioridad alta ({', '.join(gastos_altos_fijos)}) **no pueden recortarse**."
        
        return respuesta
    
    else:
        return "Para las consultas de tiempo de ahorro o cumplimiento de 50/30/20, se necesitan los valores monetarios de cada gasto, no solo la prioridad."

suma_total_gastos_ej = calcular_suma_gastos(HECHOS, GASTOS_VALOR)
print(f"Suma Total de Gastos Estimados (Ejemplo): ${suma_total_gastos_ej}\n")

print(procesar_consulta("¿Mis gastos requieren ajustes?", INGRESOS_EJEMPLO, HECHOS))

print("\n" + "="*50 + "\n")

print(procesar_consulta("¿Qué gastos puedo reducir?", INGRESOS_EJEMPLO, HECHOS))
