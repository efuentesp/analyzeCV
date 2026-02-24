---
name: 'step-04-design-skill-md'
description: 'Co-crear el archivo SKILL.md del skill: frontmatter, rol, principios, reglas e inicializacion'

# File References
nextStepFile: './step-05-design-steps.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'

# Reference Files
referenceFile: '../references/anthropic-best-practices.md'
---

# Paso 4: Diseno del SKILL.md

## OBJETIVO DEL PASO:

Co-crear el archivo SKILL.md — el orquestador ligero del skill. Definir el frontmatter (name, description), el rol del agente, los principios fundamentales, las reglas de procesamiento, las reglas criticas y la secuencia de inicializacion.

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
- ✅ Tu aportas conocimiento de mejores practicas de Anthropic y patrones de SKILL.md probados
- ✅ Manten un tono de co-creacion tecnica durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate en el SKILL.md como orquestador — maximo ~60 lineas de cuerpo
- 🚫 PROHIBIDO incluir contenido que pertenece a los pasos individuales
- 💬 Enfoque: Frontmatter preciso, rol memorable, reglas claras, inicializacion correcta
- 📋 El SKILL.md debe ser < 500 lineas incluyendo frontmatter (idealmente ~60 lineas de cuerpo)

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis antes de tomar cualquier accion
- 💾 Genera el diseno del SKILL.md colaborativamente con el usuario
- 📖 Actualiza el frontmatter `stepsCompleted: [1, 2, 3, 4]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO proceder sin confirmacion del usuario

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento de diseno con descubrimiento (paso 2) y arquitectura (paso 3)
- Enfoque: Solo el archivo SKILL.md — su estructura y contenido
- Limites: No disenar el contenido de los pasos individuales — eso es paso 5
- Dependencias: La arquitectura del paso-03 debe estar completa

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Cargar Referencia de Mejores Practicas

Carga `{referenceFile}` para tener disponible las mejores practicas de Anthropic sobre:
- Divulgacion progresiva (Progressive Disclosure)
- Gestion de ventana de contexto
- Grados de libertad
- Estilo de escritura

### 2. Disenar el Frontmatter del SKILL.md

**Co-creacion del Frontmatter:**
"Vamos a definir el frontmatter del SKILL.md. Este es lo primero que OpenCode lee para decidir si activar el skill.

**Campos a definir:**

1. **name:** `{skillName}` (ya definido en el descubrimiento — validar que cumple hyphen-case)
2. **description:** La descripcion para el trigger del skill. Debe:
   - Comenzar con 'Cuando el usuario...' o describir el trigger natural
   - Incluir sinonimos y frases alternativas que el usuario podria decir
   - Maximo 1024 caracteres
   - NO contener < o >

¿La descripcion del trigger que definimos es suficiente, o quieres refinarla?"

### 3. Definir el Rol del Agente

**Diseno del Rol:**
"El rol define la personalidad y expertise del agente durante el flujo de trabajo.

**Patron probado:**
- Titulo del rol (e.g., 'Arquitecto de Skills', 'Analista de Negocio')
- Relacion de colaboracion ('partnership, no relacion cliente-proveedor')
- Expertise especifico que el agente aporta
- Tono de comunicacion

¿Que rol deberia asumir el agente para este skill?"

### 4. Definir Principios Fundamentales

**Principios Arquitectonicos:**
"Cada SKILL.md define ~5 principios fundamentales que guian todo el flujo de trabajo. Estos son de alto nivel y aplican a todos los pasos.

**Patron estandar (ajustar segun el dominio):**
1. Facilitacion sobre generacion — contenido co-creado, no auto-generado
2. Calidad sobre velocidad — verificar antes de avanzar
3. Contexto primero — cargar informacion relevante antes de actuar
4. Transparencia — mostrar analisis y razonamiento al usuario
5. [Principio especifico del dominio]

¿Que principios aplican a este skill?"

### 5. Definir Reglas de Procesamiento y Criticas

**Reglas de Procesamiento (~6 reglas):**
Reglas operativas de como el agente procesa cada paso:
- Leer paso completo antes de actuar
- Presentar analisis antes de generar
- Esperar confirmacion antes de avanzar
- Actualizar frontmatter despues de cada paso
- [Reglas especificas del dominio]

**Reglas Criticas (~7 reglas con emojis):**
Las reglas de maxima prioridad:
- 🛑 Nunca generar sin entrada del usuario
- 📖 Leer paso completo antes de actuar
- 🔄 Cargar paso siguiente completo con 'C'
- 📋 Facilitador, no generador
- ✅ Hablar en {communication_language}
- [Reglas criticas del dominio]

### 6. Definir la Secuencia de Inicializacion

**Inicializacion:**
La secuencia de inicializacion del SKILL.md siempre sigue el patron:
1. Cargar config.yaml del proyecto (`{project-root}/.agents/core/config.yaml`)
2. Ejecutar el primer paso (`./steps/step-01-init.md`)

### 7. Generar el Diseno del SKILL.md

**Contenido a Anadir al Documento:**

```markdown
## Diseno del SKILL.md

### Frontmatter
\`\`\`yaml
---
name: '{skillName}'
description: '{descripcion refinada del trigger}'
---
\`\`\`

### Contenido del SKILL.md
[Contenido completo del SKILL.md tal como sera escrito en el archivo final, incluyendo titulo, objetivo, rol, principios, reglas e inicializacion]
```

### 8. Presentar Contenido y Confirmar

**Presentacion de Contenido:**
"He disenado el SKILL.md completo basandome en nuestra conversacion. Este archivo sera el orquestador de todo el skill.

**Esto es lo que anadire al documento de diseno:**
[Muestra el contenido markdown completo del paso 7]

Recuerda: el SKILL.md debe ser conciso (~60 lineas de cuerpo). ¿Se ve bien?

**Selecciona una Opcion:** [C] Confirmar y continuar al siguiente paso"

#### Logica de Manejo:

- SI C: Guarda el contenido en {outputFile}, actualiza el frontmatter con stepsCompleted: [1, 2, 3, 4], luego carga, lee el archivo completo, luego ejecuta {nextStepFile}
- SI Cualquier comentario, ajuste o consulta: incorpora el feedback, regenera el contenido, y vuelve a presentar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se seleccione la opcion C confirmar] y [el diseno del SKILL.md este finalizado y guardado en el documento con el frontmatter actualizado], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar y comenzar el diseno de los pasos individuales.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Frontmatter con name (hyphen-case) y description (trigger natural, < 1024 chars)
- Rol del agente definido con expertise claro y relacion colaborativa
- 5 principios fundamentales coherentes con el dominio
- ~6 reglas de procesamiento operativas
- ~7 reglas criticas con emojis
- Secuencia de inicializacion correcta (config.yaml → step-01-init)
- SKILL.md resultante < 500 lineas (idealmente ~60 lineas de cuerpo)
- Contenido anadido correctamente al documento cuando se selecciona C

### FALLO DEL SISTEMA:

- SKILL.md mayor a 500 lineas
- Frontmatter sin name o description
- Name que no cumple hyphen-case
- Incluir contenido que pertenece a pasos individuales
- No definir secuencia de inicializacion
- Rol generico sin expertise especifico

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
