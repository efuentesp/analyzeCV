---
name: 'step-03-architecture'
description: 'Disenar la arquitectura del skill: estructura de directorios, numero de pasos, recursos necesarios y flujo de navegacion'

# File References
nextStepFile: './step-04-design-skill-md.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'

# Reference Files
referenceFiles: '../references/skill-anatomy.md, ../references/step-file-architecture.md'
---

# Paso 3: Diseno de la Arquitectura

## OBJETIVO DEL PASO:

Disenar la arquitectura completa del skill: estructura de directorios, numero y secuencia de pasos, recursos necesarios (templates, referencias, datos, scripts), y el flujo de navegacion entre pasos.

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
- ✅ Manten un tono de diseno colaborativo durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate en la estructura y arquitectura — no en el contenido de cada paso aun
- 🚫 PROHIBIDO escribir el contenido detallado de los pasos — eso es el paso 5
- 💬 Enfoque: Decisiones arquitectonicas fundamentales del skill
- 📋 Usa las referencias para guiar las decisiones de arquitectura

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis antes de tomar cualquier accion
- 💾 Genera el diseno arquitectonico colaborativamente con el usuario
- 📖 Actualiza el frontmatter `stepsCompleted: [1, 2, 3]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO proceder sin confirmacion del usuario

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento de diseno con seccion de descubrimiento del paso 2
- Enfoque: Arquitectura y estructura, no contenido detallado de pasos
- Limites: Define QUE pasos habra y QUE recursos, no COMO sera cada paso
- Dependencias: El descubrimiento del paso-02 debe estar completo

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Cargar Referencias Arquitectonicas

Carga `{referenceFiles}` para tener disponible:
- La anatomia completa de un skill (skill-anatomy.md)
- La arquitectura de archivos de step (step-file-architecture.md)

### 2. Revisar el Descubrimiento

Revisa la seccion de Descubrimiento del documento para recordar:
- Proposito y problema del skill
- Tipo de skill seleccionado
- Alcance definido
- Salida esperada

### 3. Disenar la Secuencia de Pasos

**Conversacion de Diseno:**
"Basandonos en el descubrimiento, vamos a definir la estructura del skill. Segun las mejores practicas:

**Pasos obligatorios del patron:**
- `step-01-init.md` — Inicializacion y deteccion de continuacion
- `step-01b-continue.md` — Logica de reanudacion
- `step-NN-complete.md` — Validacion final y cierre (ultimo paso)

**Pasos de contenido (a disenar):**
Basandome en el alcance que definimos, sugiero los siguientes pasos intermedios:
[Presenta propuesta de pasos basada en el tipo y alcance del skill]

¿Que te parece esta estructura? ¿Anadimos, quitamos o reordenamos algun paso?"

**Criterios para definir pasos:**
- Cada paso debe tener un objetivo unico y claro
- Un paso no deberia tener mas de 3-4 actividades principales
- El numero total de pasos (sin init/continue/complete) deberia ser entre 3 y 7
- Considerar el patron: descubrimiento → diseno → implementacion → validacion

### 4. Definir Recursos Necesarios

**Inventario de Recursos:**
Para cada tipo de recurso, determina que se necesita:

- **Templates:** ¿Que plantillas necesita el documento de salida?
- **Referencias:** ¿Que documentos de referencia consultara el agente?
- **Datos:** ¿Hay datos estructurados (CSV, tablas) que el skill necesita?
- **Scripts:** ¿Se necesita un script de validacion? ¿Otros scripts?

### 5. Disenar el Flujo de Navegacion

**Mapa de Navegacion:**
Define la cadena de `nextStepFile` para cada paso:

```
step-01-init → (si existe doc) → step-01b-continue → (paso correspondiente)
step-01-init → (si nuevo) → step-02-xxx → step-03-xxx → ... → step-NN-complete
```

Incluir tambien que `outputFile` usa cada paso y que recursos (`referenceFile`, `templateFile`, `dataFile`) carga cada paso.

### 6. Generar Diseno Arquitectonico

**Contenido a Anadir al Documento:**

```markdown
## Arquitectura del Skill

### Estructura de Directorios
[Arbol de directorios completo con todos los archivos]

### Secuencia de Pasos
| # | Archivo | Nombre | Objetivo | nextStepFile |
|---|---------|--------|----------|--------------|
[Tabla completa de todos los pasos]

### Inventario de Recursos
| Tipo | Archivo | Descripcion | Usado por |
|------|---------|-------------|-----------|
[Tabla de todos los recursos]

### Flujo de Navegacion
[Diagrama textual del flujo entre pasos]
```

### 7. Presentar Contenido y Confirmar

**Presentacion de Contenido:**
"He disenado la arquitectura completa del skill basandome en nuestra conversacion.

**Esto es lo que anadire al documento de diseno:**
[Muestra el contenido markdown completo del paso 6]

**Selecciona una Opcion:** [C] Confirmar y continuar al siguiente paso"

#### Logica de Manejo:

- SI C: Guarda el contenido en {outputFile}, actualiza el frontmatter con stepsCompleted: [1, 2, 3], luego carga, lee el archivo completo, luego ejecuta {nextStepFile}
- SI Cualquier comentario, ajuste o consulta: incorpora el feedback, regenera el contenido, y vuelve a presentar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se seleccione la opcion C confirmar] y [el diseno arquitectonico este finalizado y guardado en el documento con el frontmatter actualizado], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar y comenzar el diseno del SKILL.md.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Secuencia de pasos coherente con el alcance definido
- Cada paso tiene objetivo unico y claro
- Recursos necesarios identificados con ubicacion y proposito
- Flujo de navegacion completo y sin ciclos
- Patron init/continue/complete respetado
- Contenido anadido correctamente al documento cuando se selecciona C

### FALLO DEL SISTEMA:

- Disenar demasiados pasos (mas de 10 incluyendo init/continue)
- No incluir step-01-init, step-01b-continue o step-complete
- Dejar pasos sin nextStepFile (excepto el ultimo)
- No identificar recursos necesarios
- Crear flujos circulares o con pasos huerfanos

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
