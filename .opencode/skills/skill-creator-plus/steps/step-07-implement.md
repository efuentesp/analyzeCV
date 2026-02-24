---
name: 'step-07-implement'
description: 'Implementar el skill escribiendo todos los archivos al disco: SKILL.md, pasos, templates, referencias, datos y scripts'

# File References
nextStepFile: './step-08-validate.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'
---

# Paso 7: Implementacion

## OBJETIVO DEL PASO:

Implementar el skill completo escribiendo todos los archivos diseñados al disco: crear la estructura de directorios, escribir el SKILL.md, todos los archivos de paso, templates, referencias, datos y scripts.

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
- ✅ En este paso especifico, el agente toma un rol mas activo escribiendo archivos, pero SIEMPRE con confirmacion del usuario
- ✅ Manten un tono de implementacion metodica durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate en escribir archivos fieles al diseno — no improvisar ni modificar el diseno
- 🚫 PROHIBIDO desviarse del diseno aprobado en los pasos anteriores
- 💬 Enfoque: Implementacion fiel y sistematica del diseno
- 📋 Verificar cada archivo escrito antes de pasar al siguiente

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra el plan de implementacion antes de escribir ningun archivo
- 💾 Escribe archivos en orden: directorio → SKILL.md → pasos → recursos
- 📖 Actualiza el frontmatter `stepsCompleted: [1, 2, 3, 4, 5, 6, 7]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO proceder sin confirmacion del usuario

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento de diseno completo con SKILL.md, pasos y recursos disenados
- Enfoque: Escritura de archivos al disco
- Limites: Implementar fiel al diseno — no agregar ni quitar funcionalidad
- Dependencias: El diseno de recursos (paso 6) debe estar completo

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Determinar Ubicacion del Skill

**Ubicacion del Skill:**
Basandose en el campo `targetLocation` del frontmatter del documento de diseno:

- Si `targetLocation` esta definido, usar esa ruta
- Si no, la ubicacion por defecto es: `.opencode/skills/{skillName}/`

Confirma la ubicacion con el usuario:
"Voy a crear el skill en `{targetLocation}`. ¿Es correcto?"

### 2. Presentar Plan de Implementacion

**Plan de Escritura:**
"Voy a crear los siguientes archivos:

**Estructura de Directorios:**
```
{targetLocation}/
├── SKILL.md
├── steps/
│   ├── step-01-init.md
│   ├── step-01b-continue.md
│   ├── ... [listar todos los pasos]
│   └── step-NN-complete.md
├── templates/
│   └── ... [listar templates]
├── references/
│   └── ... [listar referencias]
├── data/
│   └── ... [listar datos]
└── scripts/
    └── ... [listar scripts]
```

**Total:** {N} archivos a crear

¿Procedo con la implementacion?"

### 3. Crear Estructura de Directorios

Crear los directorios necesarios:
- `{targetLocation}/`
- `{targetLocation}/steps/`
- `{targetLocation}/templates/` (si hay templates)
- `{targetLocation}/references/` (si hay referencias)
- `{targetLocation}/data/` (si hay datos)
- `{targetLocation}/scripts/` (si hay scripts)

### 4. Escribir SKILL.md

Tomar el contenido del SKILL.md disenado en el paso 4 y escribirlo como archivo:
- Usar el contenido exacto del diseno, sin modificaciones
- Verificar que el frontmatter es YAML valido
- Verificar que el archivo tiene < 500 lineas

### 5. Escribir Archivos de Pasos

Para cada paso disenado en el paso 5:
- Tomar el contenido exacto del diseno
- Escribir el archivo en `{targetLocation}/steps/{nombre-del-paso}.md`
- Verificar que el frontmatter contiene name, description y nextStepFile (excepto el ultimo)

### 6. Escribir Recursos

Para cada recurso disenado en el paso 6:
- **Templates:** Escribir en `{targetLocation}/templates/`
- **Referencias:** Escribir en `{targetLocation}/references/`
- **Datos:** Escribir en `{targetLocation}/data/`
- **Scripts:** Escribir en `{targetLocation}/scripts/` y marcar como ejecutables

### 7. Verificacion Post-Escritura

**Verificacion basica:**
Para cada archivo escrito:
- Confirmar que el archivo existe y no esta vacio
- Verificar que archivos markdown tienen frontmatter valido (si aplica)
- Verificar que scripts Python tienen sintaxis valida

**Reporte de implementacion:**
"He creado {N} archivos exitosamente:

- SKILL.md: {lineas} lineas
- Pasos: {N} archivos
- Templates: {N} archivos
- Referencias: {N} archivos
- Datos: {N} archivos
- Scripts: {N} archivos

Todos los archivos han sido verificados."

### 8. Presentar Resultados y Confirmar

**Presentacion de Resultados:**
"La implementacion esta completa. Todos los archivos del skill han sido escritos al disco.

**Resumen:**
[Reporte de implementacion del paso 7]

El siguiente paso ejecutara el script de validacion para verificar la integridad del skill.

**Selecciona una Opcion:** [C] Confirmar y continuar a la validacion"

#### Logica de Manejo:

- SI C: Actualiza el frontmatter con stepsCompleted: [1, 2, 3, 4, 5, 6, 7], luego carga, lee el archivo completo, luego ejecuta {nextStepFile}
- SI Cualquier comentario, ajuste o consulta: atiende la solicitud y vuelve a presentar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [todos los archivos esten escritos y verificados] y [se seleccione la opcion C confirmar], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar la validacion.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Todos los archivos del diseno escritos al disco sin omisiones
- Contenido fiel al diseno aprobado en pasos anteriores
- Estructura de directorios correcta
- Frontmatter YAML valido en todos los archivos markdown
- Scripts con sintaxis Python valida
- Verificacion post-escritura exitosa para todos los archivos
- Contenido anadido correctamente al documento cuando se selecciona C

### FALLO DEL SISTEMA:

- Archivos omitidos de la implementacion
- Contenido que difiere del diseno aprobado
- Archivos escritos en ubicacion incorrecta
- Frontmatter invalido o ausente
- Scripts con errores de sintaxis
- No verificar los archivos despues de escribirlos

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
