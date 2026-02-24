---
name: 'step-09-complete'
description: 'Completar el flujo de trabajo de creacion de skill, presentar checklist final y sugerir proximos pasos'

# File References
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'
---

# Paso 9: Completacion del Flujo de Trabajo

## OBJETIVO DEL PASO:

Completar el flujo de trabajo de creacion del skill, presentar un checklist final de todo lo logrado, documentar el resultado y sugerir proximos pasos.

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
- ✅ Manten un tono de completacion colaborativa y celebracion del logro

### Reglas Especificas del Paso:

- 🎯 Enfocate solo en completacion, resumen y proximos pasos
- 🚫 PROHIBIDO generar nuevo contenido para el skill
- 💬 Enfoque: Completacion sistematica con validacion de calidad y recomendaciones
- 📋 FINALIZA el documento y actualiza el estado del flujo de trabajo

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra tu analisis antes de tomar cualquier accion
- 💾 Actualiza el documento de diseno con informacion de completacion
- 📖 NO cargues pasos adicionales despues de este (este es el final)
- 🚫 NO hay nextStepFile — este es el paso terminal

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento de diseno completo y skill implementado y validado
- Enfoque: Validacion de completacion, resumen y orientacion de proximos pasos
- Limites: No hay generacion de nuevo contenido, solo actividades de cierre
- Dependencias: Todos los pasos anteriores deben estar completados

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Anunciar Completacion del Flujo de Trabajo

**Anuncio de Completacion:**
"**¡Skill Completado, {{user_name}}!**

Hemos disenado e implementado exitosamente un skill de flujo de trabajo completo para OpenCode.

**Lo que hemos logrado:**

- Descubrimiento del proposito y alcance del skill
- Diseno de la arquitectura completa
- Co-creacion del SKILL.md como orquestador
- Diseno detallado de cada paso del flujo de trabajo
- Diseno de todos los recursos (templates, referencias, datos, scripts)
- Implementacion de todos los archivos al disco
- Validacion exitosa del skill

**El skill esta disponible en:** `{targetLocation}`
**El documento de diseno esta en:** `{outputFile}`"

### 2. Checklist Final

**Verificacion de Completitud:**

- [ ] SKILL.md creado con frontmatter valido y < 500 lineas
- [ ] Todos los pasos escritos con estructura correcta
- [ ] Patron init/continue/complete implementado
- [ ] Cadena de nextStepFile completa y sin ciclos
- [ ] Templates con frontmatter de estado y estructura append-only
- [ ] Referencias con conocimiento del dominio
- [ ] Script de validacion pasando todas las pruebas
- [ ] Nombre del directorio = name del frontmatter
- [ ] Descripcion del trigger efectiva para activacion

### 3. Resumen del Skill Creado

**Ficha Tecnica:**

| Campo | Valor |
|-------|-------|
| Nombre | {skillName} |
| Tipo | {skillType} |
| Ubicacion | {targetLocation} |
| Pasos | {numero total de pasos} |
| Templates | {numero de templates} |
| Referencias | {numero de referencias} |
| Scripts | {numero de scripts} |
| Validacion | {resultado: PASS/FAIL con detalles} |

### 4. Sugerir Proximos Pasos

**Proximos Pasos Recomendados:**

1. **Probar el skill** — Activa el skill con el trigger definido y recorre el flujo completo
2. **Iterar** — Basado en la prueba, ajusta instrucciones o preguntas de descubrimiento
3. **Documentar** — Si el skill es para distribucion, agregar LICENSE.txt

**Consejos para pruebas:**
- Prueba el trigger con variaciones de frase para verificar la activacion
- Recorre el flujo completo al menos una vez para verificar la cadena de pasos
- Verifica que la continuacion (step-01b) funciona correctamente
- Revisa que el documento de salida tiene estructura coherente

### 5. Actualizar Documento de Diseno

**Contenido a Anadir al Documento:**

```markdown
## Completacion

### Checklist Final
[Checklist del paso 2 marcada]

### Ficha Tecnica
[Tabla del paso 3]

### Estado Final
- Flujo de trabajo: COMPLETADO
- Fecha: {{date}}
- Validacion: {resultado}
```

Actualiza el frontmatter con `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9]`.

### 6. Cierre del Flujo de Trabajo

**Mensaje Final:**
"**Tu skill `{skillName}` esta listo para usar en OpenCode.**

El documento de diseno completo esta disponible en `{outputFile}` como referencia para futuras iteraciones.

Para activar el skill, usa el trigger natural que definimos o invocalo directamente.

¡Excelente trabajo de colaboracion, {{user_name}}!"

#### Logica de Manejo:

- No hay continuacion a otros pasos del flujo de trabajo
- El usuario puede hacer preguntas o solicitar revision del skill completado
- Proporciona orientacion adicional cuando sea solicitado
- Finaliza la sesion del flujo de trabajo

#### REGLAS DE EJECUCION:

- Este es un paso final — no hay pasos adicionales
- El usuario puede solicitar revision o aclaracion
- Proporciona orientacion clara sobre como probar y usar el skill

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se proporcione confirmacion de completacion y se actualice el estado del flujo de trabajo], entonces marcaras el flujo de trabajo como completo y finalizaras la sesion. No se cargan pasos adicionales despues de este paso final.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Checklist final completada con todos los items verificados
- Ficha tecnica del skill presentada con datos precisos
- Proximos pasos claros y accionables proporcionados
- Documento de diseno actualizado con informacion de completacion
- Frontmatter actualizado con todos los pasos completados
- El usuario tiene claridad sobre como probar y usar el skill

### FALLO DEL SISTEMA:

- No presentar checklist de completacion
- Falta de orientacion sobre como probar el skill
- Documento de diseno sin seccion de completacion
- No actualizar el frontmatter con el paso final
- Usuario sin claridad sobre proximos pasos

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.

## COMPLETACION FINAL DEL FLUJO DE TRABAJO

Este skill ha sido disenado, implementado y validado siguiendo las mejores practicas de Anthropic y los patrones arquitectonicos probados de OpenCode. El skill esta listo para uso productivo.
