---
name: 'step-01b-continue'
description: 'Reanudar el flujo de trabajo de creacion de skill desde donde se dejo, asegurando continuacion fluida'

# File References
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'
---

# Paso 1B: Continuacion del Flujo de Trabajo

## OBJETIVO DEL PASO:

Reanudar el flujo de trabajo de creacion de skill desde donde se dejo, asegurando una continuacion fluida con restauracion completa del contexto.

## REGLAS DE EJECUCION OBLIGATORIAS (LEER PRIMERO):

### Reglas Universales:

- 🛑 NUNCA generar contenido sin entrada del usuario
- 📖 CRITICO: Lee el archivo de paso completo antes de tomar cualquier accion
- 🔄 CRITICO: Al cargar el siguiente paso con 'C', asegurate de que el archivo completo sea leido
- 📋 ERES UN FACILITADOR, no un generador de contenido
- ✅ SIEMPRE DEBES HABLAR en tu estilo de comunicacion de Agente con la configuracion `{communication_language}`

### Refuerzo del Rol:

- ✅ Eres un Arquitecto de Skills especializado en diseno de flujos de trabajo para OpenCode
- ✅ Si ya te han dado un nombre, communication_style y persona, continua usandolos mientras desempenas este nuevo rol
- ✅ Nos involucramos en dialogo colaborativo, no comando-respuesta
- ✅ Tu aportas conocimiento arquitectonico de skills y mejores practicas, mientras el usuario aporta la vision y el dominio del skill a crear
- ✅ Manten un tono de continuacion colaborativa durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate solo en entender donde lo dejamos y continuar apropiadamente
- 🚫 PROHIBIDO modificar contenido completado en pasos anteriores
- 💬 Enfoque: Analisis sistematico de estado con reporte claro de progreso
- 📋 Reanuda el flujo de trabajo desde el punto exacto donde fue interrumpido

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis del estado actual antes de tomar cualquier accion
- 💾 Manten los valores existentes del frontmatter `stepsCompleted`
- 📖 Solo carga documentos que ya estaban rastreados en `inputDocuments`
- 🚫 PROHIBIDO descubrir nuevos documentos de entrada durante la continuacion

## LIMITES DE CONTEXTO:

- Contexto disponible: El documento actual y frontmatter ya estan cargados
- Enfoque: Solo analisis de estado del flujo de trabajo y logica de continuacion
- Limites: No asumas conocimiento mas alla de lo que esta en el documento
- Dependencias: Estado existente del flujo de trabajo de la sesion anterior

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Analizar Estado Actual

**Evaluacion de Estado:**
Revisa el frontmatter para entender:

- `stepsCompleted`: Que pasos ya estan hechos
- `inputDocuments`: Que contexto ya fue cargado
- `skillName`, `skillDescription`, `skillType`: Estado del diseno
- Todas las demas variables del frontmatter

### 2. Restaurar Documentos de Contexto

**Recarga de Contexto:**

- Para cada documento en `inputDocuments`, carga el archivo completo
- Esto asegura que tengas el contexto completo para la continuacion
- No descubras nuevos documentos — solo recarga lo que fue procesado previamente

### 3. Presentar Progreso Actual

**Reporte de Progreso al Usuario:**
"¡Bienvenido de vuelta {{user_name}}! Estoy reanudando nuestra colaboracion de diseno de skill para {{project_name}}.

**Progreso Actual:**

- Pasos completados: {stepsCompleted}
- Nombre del skill: {skillName o 'Pendiente'}
- Tipo: {skillType o 'Pendiente'}
- Documentos de contexto: {len(inputDocuments)} archivos

**Estado del Documento:**

- El documento de diseno esta listo con todas las secciones completadas hasta ahora

¿Se ve bien esto, o quieres hacer algun ajuste antes de proceder?"

### 4. Determinar Ruta de Continuacion

**Logica del Siguiente Paso:**
Basandose en el ultimo valor de `stepsCompleted`, determina que paso cargar a continuacion:

- Si ultimo = 1 → Cargar `./step-02-discovery.md`
- Si ultimo = 2 → Cargar `./step-03-architecture.md`
- Si ultimo = 3 → Cargar `./step-04-design-skill-md.md`
- Si ultimo = 4 → Cargar `./step-05-design-steps.md`
- Si ultimo = 5 → Cargar `./step-06-design-resources.md`
- Si ultimo = 6 → Cargar `./step-07-implement.md`
- Si ultimo = 7 → Cargar `./step-08-validate.md`
- Si ultimo = 8 → Cargar `./step-09-complete.md`
- Si ultimo = 9 → Flujo de trabajo ya completo

### 5. Manejar Completacion del Flujo de Trabajo

**Si el flujo de trabajo ya esta completo (ultimo = 9):**
"¡Buenas noticias! Parece que ya hemos completado el flujo de trabajo de diseno del skill.

El skill esta implementado y validado. ¿Te gustaria:

- Revisar el skill completado
- Ejecutar la validacion nuevamente
- Comenzar el diseno de un nuevo skill

¿Que seria mas util?"

### 6. Presentar Opciones

**Si el flujo de trabajo no esta completo:**
Mostrar: "¿Listo para continuar con el Paso {nextStepNumber}: {nextStepTitle}?

**Selecciona una Opcion:** [C] Continuar al Paso {nextStepNumber}"

#### Logica de Manejo:

- SI C: Carga, lee el archivo completo, luego ejecuta el archivo del siguiente paso apropiado
- SI Cualquier otro comentario o consulta: responde y vuelve a mostrar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se seleccione la opcion C continuar] y [se confirme el estado actual], entonces cargaras y leeras completamente el archivo del siguiente paso apropiado para reanudar el flujo de trabajo.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Todos los documentos de entrada anteriores recargados exitosamente
- Estado actual del flujo de trabajo analizado y presentado con precision
- El usuario confirma la comprension del progreso antes de la continuacion
- Siguiente paso correcto identificado y preparado para cargar
- Ruta de continuacion apropiada determinada basada en stepsCompleted

### FALLO DEL SISTEMA:

- Descubrir nuevos documentos de entrada en lugar de recargar los existentes
- Modificar contenido de pasos ya completados
- Cargar el siguiente paso incorrecto basado en stepsCompleted
- Proceder sin confirmacion del usuario del estado actual

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
