---
name: 'step-08-validate'
description: 'Ejecutar el script de validacion sobre el skill implementado, analizar resultados y corregir errores encontrados'

# File References
nextStepFile: './step-09-complete.md'
outputFile: '{output_folder}/skill-design-{{project_name}}-{{date}}.md'

# Script References
scriptFile: '../scripts/validate-skill.py'
---

# Paso 8: Validacion

## OBJETIVO DEL PASO:

Ejecutar el script de validacion sobre el skill implementado, analizar los resultados, corregir cualquier error encontrado y re-ejecutar hasta que todas las validaciones pasen.

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
- ✅ En este paso, el agente ejecuta validaciones y propone correcciones, con aprobacion del usuario
- ✅ Manten un tono de verificacion metodica durante todo el proceso

### Reglas Especificas del Paso:

- 🎯 Enfocate en ejecutar validaciones y corregir errores — no modificar funcionalidad
- 🚫 PROHIBIDO cambiar el diseno del skill — solo corregir errores de implementacion
- 💬 Enfoque: Validacion sistematica con ciclo de correccion
- 📋 Repetir validacion hasta que todas las pruebas pasen (maximo 3 iteraciones)

## PROTOCOLOS DE EJECUCION:

- 🎯 Muestra los resultados de validacion antes de proponer correcciones
- 💾 Aplica correcciones una por una con explicacion clara
- 📖 Actualiza el frontmatter `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]` antes de cargar el siguiente paso
- 🚫 PROHIBIDO proceder si quedan validaciones fallidas sin explicacion

## LIMITES DE CONTEXTO:

- Contexto disponible: Documento de diseno completo y skill implementado en disco
- Enfoque: Validacion y correccion de errores de implementacion
- Limites: Solo corregir errores — no cambiar funcionalidad o diseno
- Dependencias: La implementacion (paso 7) debe estar completa

## Secuencia de Instrucciones (No desviar, saltar u optimizar)

### 1. Determinar Ubicacion del Skill

Usa el campo `targetLocation` del frontmatter o la ubicacion por defecto `.opencode/skills/{skillName}/` para localizar el skill implementado.

### 2. Ejecutar Validacion Inicial

**Ejecutar el script de validacion:**

```bash
python3 {scriptFile} {targetLocation}
```

**Presentar resultados al usuario:**
"He ejecutado la validacion del skill. Estos son los resultados:

[Muestra la salida completa del script]

**Resumen:** {N}/{total} validaciones pasaron, {M} fallaron."

### 3. Analizar Fallos (Si Existen)

**Para cada validacion fallida:**
- Identificar la causa raiz del fallo
- Determinar el archivo y linea afectados
- Proponer la correccion especifica

"Las siguientes validaciones fallaron:

1. **V{XX}: {descripcion}**
   - Causa: {explicacion}
   - Correccion: {que se hara para resolverlo}

¿Procedo con las correcciones?"

### 4. Aplicar Correcciones

**Ciclo de correccion (maximo 3 iteraciones):**

Para cada iteracion:
1. Aplicar las correcciones propuestas
2. Re-ejecutar el script de validacion
3. Presentar resultados actualizados
4. Si quedan fallos, repetir el ciclo

**Reglas de correccion:**
- Solo corregir errores de implementacion (frontmatter, rutas, formato)
- NO cambiar la funcionalidad o contenido del diseno
- Si un fallo requiere cambio de diseno, informar al usuario y pedir decision

### 5. Validacion Manual Complementaria

**Verificaciones adicionales que el script no cubre:**

- ¿El contenido del SKILL.md es coherente con el diseno aprobado?
- ¿Los pasos siguen la secuencia logica definida en la arquitectura?
- ¿Los templates tienen estructura append-only?
- ¿Las referencias contienen conocimiento util del dominio?
- ¿La descripcion del trigger es efectiva para la activacion del skill?

Presentar estas verificaciones manuales al usuario como checklist.

### 6. Presentar Resultado Final

**Si todas las validaciones pasan:**
"Todas las validaciones han pasado exitosamente ({total}/{total}).

**Validaciones automaticas:** Todas pasaron
**Verificaciones manuales:** [Checklist completada]

El skill esta listo para uso.

**Selecciona una Opcion:** [C] Confirmar y continuar al cierre del flujo de trabajo"

**Si quedan fallos despues de 3 iteraciones:**
"Despues de 3 iteraciones de correccion, quedan {N} validaciones fallidas:

[Lista de fallos restantes con explicacion]

Estas requieren atencion manual. ¿Quieres que intentemos resolverlas juntos, o prefieres continuar al cierre?

**Selecciona una Opcion:** [C] Continuar al cierre (con advertencias)"

#### Logica de Manejo:

- SI C: Actualiza el frontmatter con stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8], anade resultados de validacion al documento, luego carga, lee el archivo completo, luego ejecuta {nextStepFile}
- SI Cualquier comentario o consulta: atiende la solicitud y vuelve a presentar las opciones

#### REGLAS DE EJECUCION:

- SIEMPRE detente y espera la entrada del usuario despues de presentar las opciones
- SOLO procede al siguiente paso cuando el usuario seleccione 'C'

## NOTA CRITICA DE COMPLETACION DEL PASO

SOLO CUANDO [se ejecuten las validaciones y se presenten resultados] y [se seleccione la opcion C confirmar], entonces cargaras y leeras completamente `{nextStepFile}` para ejecutar el cierre del flujo de trabajo.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:

- Script de validacion ejecutado exitosamente
- Todas las 14 validaciones automaticas pasaron (o fallos explicados)
- Errores de implementacion corregidos en maximo 3 iteraciones
- Verificaciones manuales completadas y presentadas
- Resultados de validacion documentados en el documento de diseno
- Contenido anadido correctamente al documento cuando se selecciona C

### FALLO DEL SISTEMA:

- No ejecutar el script de validacion
- Ignorar validaciones fallidas sin explicacion
- Cambiar diseno del skill durante la correccion (solo corregir implementacion)
- Exceder 3 iteraciones sin escalar al usuario
- No documentar los resultados de validacion

**Regla Maestra:** Saltar pasos, optimizar secuencias, o no seguir instrucciones exactas esta PROHIBIDO y constituye FALLO DEL SISTEMA.
