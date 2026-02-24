---
name: 'step-06-design-resources'
description: 'Disenar los recursos del skill: templates, archivos de referencia, datos estructurados y scripts de validacion'

# File References
nextStepFile: './step-07-implement.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'

# Reference Files
referenceFiles: '../references/output-patterns.md, ../references/workflow-patterns.md'
---

# Paso 6: Diseno de Recursos

## OBJETIVO DEL PASO:

Disenar todos los recursos que acompanan al skill: templates del documento de salida, archivos de referencia para consulta del agente, datos estructurados (CSV, tablas), y scripts de validacion o utilidad.

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
- ✅ Tu aportas conocimiento de patrones de salida y flujos de trabajo probados
- ✅ Manten un tono de co-creacion tecnica durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate en disenar recursos concretos — contenido real, no placeholders
- 🚫 PROHIBIDO dejar templates con solo placeholders genericos sin estructura
- 💬 Enfoque: Recursos listos para usar que el skill pueda consumir
- 📋 Cada recurso debe tener proposito claro y ser referenciado por al menos un paso

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis antes de tomar cualquier accion
- 💾 Genera el diseno de recursos colaborativamente con el usuario
- 📖 Actualiza el frontmatter `stepsCompleted: [1, 2, 3, 4, 5, 6]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO proceder sin confirmacion del usuario

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento de diseno completo hasta paso 5 (incluye diseno de todos los pasos)
- Enfoque: Recursos concretos — templates, referencias, datos, scripts
- Limites: No modificar el diseno de pasos — eso ya esta completo
- Dependencias: El diseno de pasos (paso 5) debe estar completo

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Cargar Referencias de Patrones

Carga `{referenceFiles}` para tener disponible:
- Patrones de salida (output-patterns.md) — como estructurar documentos de salida
- Patrones de flujo de trabajo (workflow-patterns.md) — patrones reutilizables

### 2. Revisar Inventario de Recursos

Revisa la seccion de Arquitectura del documento para recordar:
- Lista de recursos definidos con tipo, nombre y proposito
- Que paso usa cada recurso

### 3. Disenar Templates

**Para cada template identificado en la arquitectura:**

"Vamos a disenar el template `{nombre-del-template}`.

**Proposito:** {para que se usa este template}
**Usado por:** {que paso(s) lo consumen}

**Estructura propuesta:**
[Propuesta de estructura markdown con frontmatter de estado y secciones]

¿Que secciones necesita? ¿Que campos de frontmatter?"

**Criterios para templates:**
- Incluir frontmatter de estado (`stepsCompleted: []`, campos relevantes)
- Secciones vacias con nombres descriptivos
- Comentarios HTML indicando donde se anade contenido
- Seguir el patron append-only (el agente anade, nunca reemplaza)

### 4. Disenar Archivos de Referencia

**Para cada archivo de referencia identificado:**

"Vamos a disenar la referencia `{nombre-de-referencia}`.

**Proposito:** {que conocimiento provee al agente}
**Usado por:** {que paso(s) lo cargan}

**Contenido propuesto:**
[Propuesta del contenido del archivo de referencia]

¿Que informacion necesita incluir?"

**Criterios para referencias:**
- Contenido que el agente NO sabe por defecto (conocimiento del dominio)
- Estructurado para consulta rapida (tablas, listas, secciones claras)
- Maximo necesario — no incluir informacion que el agente ya conoce

### 5. Disenar Datos Estructurados

**Para cada archivo de datos (CSV, tablas):**

"Vamos a disenar los datos `{nombre-de-datos}`.

**Proposito:** {que decision o clasificacion soporta}
**Usado por:** {que paso(s) lo cargan}

**Estructura propuesta:**
[Propuesta de columnas y filas de ejemplo]

¿Que categorias o valores necesita?"

### 6. Disenar Scripts

**Para cada script identificado:**

"Vamos a disenar el script `{nombre-de-script}`.

**Proposito:** {que valida, genera o transforma}
**Ejecutado por:** {que paso lo invoca}

**Funcionalidad propuesta:**
[Lista de validaciones o funciones que el script realizara]

¿Que validaciones son criticas?"

**Criterios para scripts:**
- Sin dependencias externas pesadas (solo libreria estandar de Python)
- Salida clara y legible (PASS/FAIL por validacion)
- Codigo de salida 0 = exito, 1 = fallo

### 7. Generar Diseno de Recursos

**Contenido a Anadir al Documento:**

```markdown
## Diseno de Recursos

### Templates

#### {nombre-template-1}
Ubicacion: `templates/{nombre}.md`
Usado por: paso {N}
\`\`\`markdown
[Contenido completo del template]
\`\`\`

### Referencias

#### {nombre-referencia-1}
Ubicacion: `references/{nombre}.md`
Usado por: paso {N}
\`\`\`markdown
[Contenido completo de la referencia]
\`\`\`

### Datos

#### {nombre-datos-1}
Ubicacion: `data/{nombre}.csv`
Usado por: paso {N}
\`\`\`csv
[Contenido completo de los datos]
\`\`\`

### Scripts

#### {nombre-script-1}
Ubicacion: `scripts/{nombre}.py`
Usado por: paso {N}
\`\`\`python
[Descripcion funcional del script — el codigo real se genera en la implementacion]
\`\`\`
```

### 8. Presentar Contenido y Confirmar

**Presentacion de Contenido:**
"He disenado todos los recursos del skill basandome en nuestra conversacion.

**Esto es lo que anadire al documento de diseno:**
[Muestra el contenido markdown completo del paso 7]

**Selecciona una Opcion:** [C] Confirmar y continuar al siguiente paso"

#### Logica de Manejo:

- SI C: Guarda el contenido en {outputFile}, actualiza el frontmatter con stepsCompleted: [1, 2, 3, 4, 5, 6], luego carga, lee el archivo completo, luego ejecuta {nextStepFile}
- SI Cualquier comentario, ajuste o consulta: incorpora el feedback, regenera el contenido, y vuelve a presentar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se seleccione la opcion C confirmar] y [el diseno de TODOS los recursos este finalizado y guardado en el documento con el frontmatter actualizado], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar y comenzar la implementacion.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Todos los recursos del inventario tienen diseno completo con contenido real
- Templates incluyen frontmatter de estado y estructura append-only
- Referencias contienen conocimiento que el agente no tiene por defecto
- Datos estructurados tienen formato correcto y valores reales
- Scripts tienen funcionalidad definida sin dependencias externas pesadas
- Cada recurso es referenciado por al menos un paso
- Contenido anadido correctamente al documento cuando se selecciona C

### FALLO DEL SISTEMA:

- Templates con solo placeholders genericos sin estructura real
- Referencias con informacion que el agente ya conoce
- Recursos huerfanos que ningun paso referencia
- Scripts con dependencias externas no estandar
- No definir contenido concreto para los recursos

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
