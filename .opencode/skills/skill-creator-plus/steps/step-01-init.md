---
name: 'step-01-init'
description: 'Inicializar el flujo de trabajo de creacion de skill detectando estado de continuacion y configurando el documento de diseno'

# File References
nextStepFile: './step-02-discovery.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'

# Template References
templateFile: '../templates/skill-design-template.md'
---

# Paso 1: Inicializacion del Flujo de Trabajo

## OBJETIVO DEL PASO:

Inicializar el flujo de trabajo de creacion de skill detectando si existe un documento de diseno previo (continuacion) o configurando uno nuevo desde la plantilla.

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
- ✅ Manten un tono de colaboracion tecnica durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate solo en inicializacion y configuracion — no generar contenido de diseno aun
- 🚫 PROHIBIDO mirar hacia adelante a pasos futuros o asumir conocimiento de ellos
- 💬 Enfoque: Configuracion sistematica con reporte claro al usuario
- 📋 Detecta el estado del flujo de trabajo existente y maneja la continuacion apropiadamente

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis del estado actual antes de tomar cualquier accion
- 💾 Inicializa la estructura del documento y actualiza el frontmatter apropiadamente
- 📖 Configura el frontmatter `stepsCompleted: [1]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO cargar el siguiente paso hasta que la configuracion este completa

## LIMITES DE CONTEXTO:

- Contexto disponible: Las variables de config.yaml estan disponibles en memoria
- Enfoque: Solo inicializacion del flujo de trabajo y configuracion del documento
- Limites: No asumas conocimiento de otros pasos ni crees contenido todavia
- Dependencias: Configuracion cargada desde config.yaml

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Verificar Estado Existente del Flujo de Trabajo

Primero, verifica si el documento de salida ya existe:

**Deteccion de Estado del Flujo de Trabajo:**

- Busca el archivo `{outputFile}`
- Si existe, lee el archivo completo incluyendo el frontmatter
- Si no existe, este es un flujo de trabajo nuevo

### 2. Manejar Continuacion (Si el Documento Existe)

Si el documento existe y tiene frontmatter con `stepsCompleted`:

**Protocolo de Continuacion:**

- **DETENTE inmediatamente** y carga `./step-01b-continue.md`
- No procedas con ninguna tarea de inicializacion
- Deja que el paso-01b maneje toda la logica de continuacion
- Esta es una situacion de auto-proceder — no se necesita eleccion del usuario

### 3. Configuracion de Flujo de Trabajo Nuevo (Si No Hay Documento)

Si no existe documento o no hay `stepsCompleted` en el frontmatter:

#### A. Crear Documento Inicial

**Configuracion del Documento:**

- Copia la plantilla de `{templateFile}` a `{outputFile}`, y actualiza los campos del frontmatter con los valores de config.yaml

#### B. Descubrimiento de Documentos de Entrada

Busca documentos de contexto existentes que puedan informar el diseno del skill:
- `{output_folder}/**` — documentos generados por otros skills
- `docs/**` — documentacion del proyecto

Intenta descubrir:
- Documentos de requisitos (`*prd*`, `*requirements*`, `*brief*`)
- Documentacion existente del proyecto

<critical>Confirma lo que has encontrado con el usuario, junto con preguntar si el usuario quiere proporcionar algo mas. Solo despues de esta confirmacion procederas.</critical>

**Reglas de Carga:**

- Carga TODOS los archivos descubiertos que el usuario confirmo
- Rastrea todos los archivos cargados en el array `inputDocuments` del frontmatter

#### C. Presentar Resultados de Inicializacion

**Reporte de Configuracion al Usuario:**
"¡Bienvenido {{user_name}}! He configurado tu espacio de trabajo para disenar un nuevo skill de OpenCode para {{project_name}}.

**Configuracion del Documento:**

- Creado: `{outputFile}` desde plantilla
- Frontmatter inicializado con estado del flujo de trabajo

**Documentos de Entrada Descubiertos:**

- {lista de archivos descubiertos o "Ninguno encontrado"}

¿Tienes otros documentos que te gustaria que incluya, o continuamos al siguiente paso?"

### 4. Proceder al Siguiente Paso

Mostrar: "**Procediendo al descubrimiento del proposito del skill...**"

#### Logica de Manejo:

- Despues de presentar el reporte de configuracion y obtener confirmacion del usuario, carga inmediatamente, lee el archivo completo, luego ejecuta {nextStepFile}

#### REGLAS DE EJECUCION:

- Este es un paso de inicializacion con auto-proceder despues de completar la configuracion
- Procede directamente al siguiente paso despues de la configuracion del documento y el reporte

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se logre la completacion de la configuracion y el frontmatter este actualizado correctamente], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar y comenzar el descubrimiento del skill.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Flujo de trabajo existente detectado y correctamente transferido al paso-01b
- Flujo de trabajo nuevo inicializado con plantilla y frontmatter apropiado
- Documentos de entrada descubiertos y cargados
- Todos los archivos descubiertos rastreados en el frontmatter `inputDocuments`
- Frontmatter actualizado con `stepsCompleted: [1]` antes de proceder

### FALLO DEL SISTEMA:

- Proceder con inicializacion nueva cuando existe un flujo de trabajo existente
- No actualizar el frontmatter con los documentos de entrada descubiertos
- Crear documento sin estructura de plantilla apropiada
- No reportar claramente los documentos descubiertos al usuario

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
