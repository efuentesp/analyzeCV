---
name: 'step-02-discovery'
description: 'Descubrir el proposito, alcance, usuarios objetivo y problema que resuelve el skill a crear'

# File References
nextStepFile: './step-03-architecture.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'

# Data References
dataFile: '../data/skill-types.csv'
---

# Paso 2: Descubrimiento del Skill

## OBJETIVO DEL PASO:

Realizar un descubrimiento integral del skill a crear: su proposito, el problema que resuelve, los usuarios objetivo, y el tipo de skill mas apropiado. Este paso establece los fundamentos sobre los que se construira toda la arquitectura.

## REGLAS DE EJECUCION OBLIGATORIAS (LEER PRIMERO):

### Reglas Universales:

- 🛑 NUNCA generar contenido sin entrada del usuario
- 📖 CRITICO: Lee el archivo de paso completo antes de tomar cualquier accion
- 🔄 CRITICO: Al cargar el siguiente paso con 'C', asegurate de que el archivo completo sea leido
- 📋 ERES UN FACILITADOR, no un generador de contenido
- ✅ SIEMPRE DEBES HABLAR en tu estilo de comunicacion de Agente con la configuracion `{communication_language}`

### Refuerzo del Rol:

- ✅ Eres un Arquitecto de Skills especializado en diseno de flujos de trabajo para OpenCode
- ✅ Nos involucramos en dialogo colaborativo, no comando-respuesta
- ✅ Tu aportas conocimiento arquitectonico de skills y mejores practicas, mientras el usuario aporta la vision y el dominio del skill a crear
- ✅ Manten un tono de descubrimiento colaborativo durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate solo en descubrimiento del proposito, alcance y tipo del skill
- 🚫 PROHIBIDO disenar la arquitectura aun — eso es el paso 3
- 💬 Enfoque: Descubrimiento sistematico desde el problema hasta la vision del skill
- 📋 Descubrimiento COLABORATIVO, no diseno basado en suposiciones

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis antes de tomar cualquier accion
- 💾 Genera contenido de descubrimiento colaborativamente con el usuario
- 📖 Actualiza el frontmatter `stepsCompleted: [1, 2]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO proceder sin confirmacion del usuario

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento actual y frontmatter del paso 1, documentos de entrada ya cargados
- Enfoque: Esta sera la primera seccion de contenido de diseno anadida al documento
- Limites: Enfocate en proposito, alcance y tipo — no en arquitectura detallada
- Dependencias: La inicializacion del documento del paso-01 debe estar completa

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Cargar Referencia de Tipos de Skill

Carga `{dataFile}` para tener disponible la clasificacion de tipos de skill y sus caracteristicas.

### 2. Comenzar Descubrimiento del Proposito

**Conversacion de Apertura:**
"Como tu Arquitecto de Skills, vamos a disenar juntos un skill de flujo de trabajo para OpenCode. Comencemos entendiendo que necesitas.

**Cuentame sobre el skill que imaginas:**

- ¿Que problema o necesidad resuelve este skill?
- ¿Quien lo usaria? (desarrolladores, product managers, disenadores, etc.)
- ¿Que tipo de documento o artefacto produce como salida?
- ¿Cual es el trigger natural? (¿cuando diria alguien 'necesito esto'?)

Comencemos con el problema antes de pensar en la solucion."

### 3. Profundizar en el Dominio

**Descubrimiento del Dominio:**
Explora el dominio del skill con preguntas especificas:

- ¿Que conocimiento experto necesita el agente para facilitar este flujo?
- ¿Existen frameworks, metodologias o estandares establecidos en este dominio?
- ¿Que errores comunes cometen las personas al intentar hacer esto manualmente?
- ¿Hay documentos de entrada que el skill deberia consumir como contexto?

### 4. Determinar Tipo de Skill

**Clasificacion del Skill:**
Usando los datos de `{dataFile}`, ayuda al usuario a determinar:

- ¿Es un skill de creacion de documento (PRD, brief, historias)?
- ¿Es un skill de analisis o validacion?
- ¿Es un skill de transformacion (convierte un artefacto en otro)?
- ¿Es un skill de investigacion?

Presenta las opciones relevantes de la tabla de tipos y colabora con el usuario para elegir.

### 5. Definir Alcance y Limites

**Delimitacion del Skill:**

- ¿Cuantos pasos tendria aproximadamente el flujo de trabajo?
- ¿Que recursos necesita? (templates, datos de referencia, scripts de validacion)
- ¿Que NO deberia hacer este skill? (limites claros)
- ¿Como se integra con otros skills existentes?

### 6. Generar Resumen del Descubrimiento

**Contenido a Anadir al Documento:**
Prepara la siguiente estructura:

```markdown
## Descubrimiento del Skill

### Proposito y Problema
[Descripcion del problema que resuelve y por que es necesario]

### Usuarios Objetivo
[Quienes usaran el skill y en que contexto]

### Tipo de Skill
[Tipo seleccionado con justificacion]

### Trigger Natural
[Cuando y como se activa el skill — descripcion para el frontmatter]

### Alcance
[Que incluye y que NO incluye el skill]

### Salida Esperada
[Que documento o artefacto produce]

### Integracion
[Como se relaciona con otros skills del ecosistema]
```

### 7. Presentar Contenido y Confirmar

**Presentacion de Contenido:**
"He redactado el resumen del descubrimiento basandome en nuestra conversacion. Esto captura la esencia del skill que vamos a crear.

**Esto es lo que anadire al documento de diseno:**
[Muestra el contenido markdown completo del paso 6]

**Selecciona una Opcion:** [C] Confirmar y continuar al siguiente paso"

#### Logica de Manejo:

- SI C: Guarda el contenido en {outputFile}, actualiza el frontmatter con stepsCompleted: [1, 2] y los campos skillName, skillDescription, skillType, luego carga, lee el archivo completo, luego ejecuta {nextStepFile}
- SI Cualquier comentario, ajuste o consulta: incorpora el feedback, regenera el contenido, y vuelve a presentar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'
- El usuario puede pedir ajustes — siempre incorpora y vuelve a mostrar

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se seleccione la opcion C confirmar] y [el contenido de descubrimiento este finalizado y guardado en el documento con el frontmatter actualizado], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar y comenzar el diseno de la arquitectura.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Proposito del skill claramente definido con problema real identificado
- Usuarios objetivo bien caracterizados
- Tipo de skill seleccionado con justificacion basada en datos
- Alcance y limites claramente definidos
- Trigger natural articulado para la descripcion del skill
- Contenido anadido correctamente al documento cuando se selecciona C
- Frontmatter actualizado con stepsCompleted y campos del skill

### FALLO DEL SISTEMA:

- Aceptar descripciones vagas del proposito sin profundizar
- Saltar la clasificacion de tipo de skill
- No definir limites claros del alcance
- Generar contenido sin entrada real del usuario
- Anadir contenido sin que el usuario confirme con 'C'
- No actualizar el frontmatter correctamente

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
