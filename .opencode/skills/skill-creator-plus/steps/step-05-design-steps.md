---
name: 'step-05-design-steps'
description: 'Disenar el contenido detallado de cada archivo de paso: frontmatter, estructura interna, secuencia de instrucciones y metricas'

# File References
nextStepFile: './step-06-design-resources.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'

# Reference Files
referenceFile: '../references/step-file-architecture.md'
---

# Paso 5: Diseno de los Pasos

## OBJETIVO DEL PASO:

Disenar el contenido detallado de cada archivo de paso definido en la arquitectura: su frontmatter completo, estructura interna, secuencia de instrucciones especifica, protocolo de presentacion/confirmacion, y metricas de exito/fallo.

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
- ✅ Tu aportas conocimiento de la arquitectura de archivos de step probada
- ✅ Manten un tono de co-creacion tecnica durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate en el contenido de cada paso — instrucciones especificas, no genericas
- 🚫 PROHIBIDO usar instrucciones genericas copiadas entre pasos — cada paso es unico
- 💬 Enfoque: Secuencias de instrucciones concretas que guien al agente paso a paso
- 📋 Seguir la estructura interna documentada en la referencia de arquitectura de steps

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis antes de tomar cualquier accion
- 💾 Genera el diseno de cada paso colaborativamente con el usuario
- 📖 Actualiza el frontmatter `stepsCompleted: [1, 2, 3, 4, 5]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO proceder sin confirmacion del usuario

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento de diseno con descubrimiento, arquitectura y SKILL.md
- Enfoque: Contenido detallado de cada archivo de paso
- Limites: No disenar recursos (templates, datos) — eso es paso 6
- Dependencias: La arquitectura (paso 3) y el SKILL.md (paso 4) deben estar completos

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Cargar Referencia de Arquitectura de Steps

Carga `{referenceFile}` para tener disponible la estructura interna de un archivo de paso:
- Frontmatter con campos requeridos
- Secciones obligatorias (Objetivo, Reglas, Protocolos, Limites, Instrucciones, Menu, Metricas)
- Patron de presentacion y confirmacion

### 2. Revisar la Arquitectura Definida

Revisa la seccion de Arquitectura del documento para recordar:
- Lista completa de pasos con sus objetivos
- Flujo de navegacion (nextStepFile de cada paso)
- Recursos asignados a cada paso

### 3. Disenar Cada Paso Secuencialmente

**Para cada paso de contenido (excluyendo init, continue, complete que ya tienen patron fijo):**

Presenta el diseno del paso al usuario para colaboracion:

"Vamos a disenar el **Paso {N}: {nombre}**.

**Objetivo del paso:** {objetivo definido en la arquitectura}

**Secuencia de instrucciones propuesta:**
[Lista numerada de instrucciones especificas para este paso]

**Preguntas de descubrimiento que el agente hara:**
[Las preguntas especificas del dominio que el agente usara]

**Contenido que se anadira al documento de salida:**
[Estructura markdown del contenido que este paso genera]

¿Que ajustes quieres hacer?"

**Para cada paso, definir:**

a) **Frontmatter completo:**
   - name, description
   - nextStepFile (ruta al siguiente paso)
   - outputFile (ruta al documento de salida)
   - Referencias a recursos (referenceFile, templateFile, dataFile)

b) **Reglas especificas del paso:**
   - Que esta permitido y que esta prohibido en este paso
   - Enfoque unico de este paso

c) **Secuencia de instrucciones:**
   - Pasos concretos numerados
   - Preguntas de descubrimiento para el usuario
   - Logica de generacion de contenido

d) **Estructura del contenido de salida:**
   - Markdown exacto que se anadira al documento
   - Secciones y subsecciones

e) **Protocolo de presentacion y confirmacion:**
   - Presentar contenido generado
   - `[C] Confirmar y continuar`
   - Logica de manejo de feedback

f) **Metricas de exito/fallo:**
   - Criterios de exito especificos para este paso
   - Modos de fallo especificos

### 4. Disenar Pasos Especiales

**step-01-init.md:**
- Usar el patron fijo de inicializacion (deteccion de continuacion, creacion desde template)
- Adaptar los documentos de entrada a descubrir segun el dominio del skill

**step-01b-continue.md:**
- Usar el patron fijo de continuacion (leer stepsCompleted, cargar paso correspondiente)
- Adaptar la tabla de mapeo de pasos

**step-NN-complete.md:**
- Usar el patron fijo de completacion (checklist, no nextStepFile)
- Incluir sugerencias de proximos pasos relevantes al dominio

### 5. Generar Diseno Completo de Pasos

**Contenido a Anadir al Documento:**

```markdown
## Diseno de los Pasos

### step-01-init.md
[Contenido completo del paso tal como sera escrito]

### step-01b-continue.md
[Contenido completo del paso tal como sera escrito]

### step-02-xxx.md
[Contenido completo del paso tal como sera escrito]

... [repetir para cada paso]

### step-NN-complete.md
[Contenido completo del paso tal como sera escrito]
```

### 6. Presentar Contenido y Confirmar

**Presentacion de Contenido:**
"He disenado todos los pasos del skill basandome en nuestra conversacion. Cada paso tiene su estructura completa lista para implementar.

**Esto es lo que anadire al documento de diseno:**
[Muestra el contenido markdown completo — puede ser extenso, mostrar paso por paso si es necesario]

**Selecciona una Opcion:** [C] Confirmar y continuar al siguiente paso"

#### Logica de Manejo:

- SI C: Guarda el contenido en {outputFile}, actualiza el frontmatter con stepsCompleted: [1, 2, 3, 4, 5], luego carga, lee el archivo completo, luego ejecuta {nextStepFile}
- SI Cualquier comentario, ajuste o consulta: incorpora el feedback, regenera el contenido del paso afectado, y vuelve a presentar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'
- Dado que este paso puede generar mucho contenido, esta permitido presentar paso por paso y confirmar cada uno individualmente antes de la confirmacion final

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se seleccione la opcion C confirmar] y [el diseno de TODOS los pasos este finalizado y guardado en el documento con el frontmatter actualizado], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar y comenzar el diseno de recursos.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Todos los pasos definidos en la arquitectura tienen diseno detallado
- Cada paso tiene frontmatter completo con nextStepFile correcto
- Secuencias de instrucciones son especificas al dominio, no genericas
- Patron de presentacion/confirmacion presente en cada paso intermedio
- Metricas de exito/fallo especificas en cada paso
- Pasos especiales (init, continue, complete) siguen el patron fijo
- Contenido anadido correctamente al documento cuando se selecciona C

### FALLO DEL SISTEMA:

- Pasos con instrucciones genericas copiadas entre si
- Falta frontmatter en algun paso
- nextStepFile que no corresponde al flujo definido en la arquitectura
- Pasos sin secuencia de instrucciones concreta
- Pasos sin metricas de exito/fallo
- No incluir protocolo de presentacion/confirmacion

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
