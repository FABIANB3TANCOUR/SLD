# SLD

## Práctica Resolución SLD
Fabián Betancourt Fernández

equipo: Finanzas

Esta practica consiste en generar dos clasulas de Horn, con base a una base de conocimiento con hechos y reglas, para poder tener una respuesta a una consulta utilizando Unificación.

**Nota:**

el codigo cuenta con casi todas las reglas y consultas, pero solo se usan las mencionadas en este .md

**Base de Conocimiento**

**Hechos:**

{
    
    "gastos": {
        
        "fijos": {
            
            "renta": "alta",
            
            "electricidad": "alta",
            
            "telefono/internet": "media",
            
            "agua": "alta"
	
    “seguros”: media/alta
       
        },
        
        "variables":{
           
            "transporte": "media",
            
            "ropa": "baja",
            
            "entretenimiento": "baja",
            
            "comida": "alta"
	
    “intereses_deuda”: alta
        
        }
    
    }

}

**Reglas(solo se usan 3 reglas):**

1. Si no hay ingreso no se puede generar el presupuesto ni ahorro.

2. Si los ingresos son menores que la suma de los gastos entonces requiere ajustes.

3. Si se requiere ajuste los gastos de prioridad baja son los primeros en recortarse.

**Consultas (se usan la siguientes consultas):**

¿Mis gastos requieren ajustes?

¿Qué gastos puedo reducir?




