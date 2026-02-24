# Arquitectura de Micro-archivos de Steps

Referencia detallada del patron de micro-archivos utilizado en skills de flujo de trabajo.

---

## 1. Principio Fundamental

Cada paso del flujo de trabajo vive en un archivo independiente dentro del directorio `steps/`. Los archivos se cargan uno a la vez siguiendo el principio de Just-In-Time. Nunca se cargan multiples steps simultaneamente.

---

## 2. Convenciones de Nombres

```
steps/step-01-init.md              # Siempre: inicializacion
steps/step-01b-continue.md         # Siempre: continuacion de flujo existente
steps/step-02-<nombre>.md          # Primer paso de contenido
steps/step-03-<nombre>.md          # Siguientes pasos de contenido
...
steps/step-NN-complete.md          # Siempre: completacion del flujo
```

- Usar numeros de dos digitos con padding cero (01, 02, ... 12)
- Nombres descriptivos en kebab-case despues del numero
- El primer step siempre es `step-01-init.md`
- El step de continuacion siempre es `step-01b-continue.md`
- El ultimo step siempre termina en `-complete.md`

---

## 3. Frontmatter YAML de Steps

### Campos obligatorios
```yaml
---
name: nombre-del-paso
description: Descripcion breve del proposito del paso
---
```

### Campos comunes opcionales
```yaml
---
name: nombre-del-paso
description: Descripcion breve

# Navegacion
nextStepFile: './step-03-siguiente.md'

# Archivo de salida
outputFile: '{output_folder}/{{project_name}}-documento.md'

# Plantillas (solo en step-01-init)
template: '../templates/nombre-template.md'

# Archivos de datos (cuando se necesitan)
dataFile: '../data/nombre-datos.csv'

# Referencias (cuando se necesitan)
referenceFile: '../references/nombre-referencia.md'
---
```

### Reglas del frontmatter
- El ultimo step NO tiene `nextStepFile`
- El step-01b-continue NO tiene `nextStepFile` (lo determina dinamicamente)
- Las rutas usan `./` para rutas relativas dentro de `steps/`
- Las rutas usan `../` para acceder a directorios hermanos (templates/, references/, etc.)
- Las variables `{output_folder}`, `{project-root}` se resuelven desde config.yaml

---

## 4. Esqueleto Canonico de un Step Intermedio

```markdown
---
name: paso-N-nombre
description: Descripcion del paso
nextStepFile: './step-NN-siguiente.md'
outputFile: '{output_folder}/documento.md'
---

# Paso N: Titulo del Paso

**Progreso: Paso N de M**

## OBJETIVO DEL PASO

[Descripcion clara de que debe lograr este paso]

## REGLAS DE EJECUCION OBLIGATORIAS (LEER PRIMERO)

### Reglas Universales
- NUNCA generes contenido sin entrada del usuario
- CRITICO: Lee el archivo de paso completo antes de tomar cualquier accion
- ERES UN FACILITADOR, no un generador de contenido
- DEBES HABLAR SIEMPRE en {communication_language}

### Refuerzo del Rol
Recuerda: Eres [ROL ESPECIFICO]. Mantenes una asociacion colaborativa con el usuario.

### Reglas Especificas del Paso
[Reglas particulares de este paso]

## PROTOCOLOS DE EJECUCION

- Todo contenido generado DEBE ser revisado y aprobado por el usuario antes de guardarse
- Ante cualquier duda, PREGUNTA al usuario en lugar de asumir
- Si el usuario solicita cambios, incorporalos ANTES de continuar

## LIMITES DE CONTEXTO

- NO accedas a archivos de pasos futuros
- NO anticipes decisiones de pasos posteriores
- Mantente enfocado EXCLUSIVAMENTE en el objetivo de este paso

## Secuencia de Instrucciones

### 1. [Primer sub-paso]
[Instrucciones detalladas]

### 2. [Segundo sub-paso]
[Instrucciones detalladas]

### N. Presentar contenido y confirmar
1. Mostrar al usuario un resumen del contenido generado/decidido
2. Preguntar si desea ajustar algo
3. Incorporar cambios si los hay
4. Presentar: **[C] Confirmar y continuar al siguiente paso**
5. SI el usuario confirma con C:
   - Guardar contenido en {outputFile}
   - Actualizar frontmatter: agregar 'step-NN-nombre.md' a stepsCompleted
   - Cargar, leer completo y ejecutar {nextStepFile}

## NOTA CRITICA DE COMPLETACION DEL PASO

Al recibir [C], cargaras, leeras el archivo completo y ejecutaras {nextStepFile}.
Saltarse pasos o no leer el archivo completo esta PROHIBIDO y constituye FALLO DEL SISTEMA.

---

## METRICAS DE EXITO/FALLO DEL SISTEMA

### EXITO:
- Contenido generado colaborativamente con el usuario
- Usuario confirmo el contenido antes de continuar
- Documento actualizado correctamente con el nuevo contenido
- Frontmatter actualizado con el paso completado

### FALLO DEL SISTEMA:
- Generar contenido sin entrada del usuario
- Continuar sin confirmacion del usuario
- No guardar el contenido en el documento
- Saltar al siguiente paso sin completar este
- No leer el archivo del siguiente paso completo antes de ejecutarlo
```

---

## 5. Patron de Inicializacion (step-01-init)

El step de inicializacion tiene responsabilidades unicas:

1. **Detectar continuacion**: Verificar si existe documento previo en {outputFile}
   - Si existe: redirigir a step-01b-continue
   - Si no existe: continuar con inicializacion nueva
2. **Buscar documentos de entrada**: Localizar documentos relevantes en {output_folder}
3. **Confirmar con el usuario** los documentos encontrados
4. **Crear documento de salida** desde la plantilla, reemplazando variables
5. **Reportar configuracion** al usuario

### Variables a resolver desde config.yaml
- `{project_name}` -> nombre del proyecto
- `{user_name}` -> nombre del usuario
- `{output_folder}` -> carpeta de salida (normalmente `{project-root}/_pdss-output`)
- `{communication_language}` -> idioma de comunicacion
- `{document_output_language}` -> idioma del documento de salida
- `{date}` -> fecha actual del sistema

---

## 6. Patron de Continuacion (step-01b-continue)

El step de continuacion retoma un flujo interrumpido:

1. **Leer documento existente**: Obtener frontmatter con `stepsCompleted`
2. **Determinar siguiente paso**: Obtener el ultimo step completado, leer su frontmatter, extraer `nextStepFile`
3. **Recargar contexto**: Leer documentos de entrada referenciados en `inputDocuments`
4. **Presentar progreso** al usuario con bienvenida
5. **Manejar flujo ya completado**: Si todos los pasos estan completos, informar al usuario
6. **Presentar [C]** para confirmar continuacion

---

## 7. Patron de Completacion (step-NN-complete)

El ultimo step cierra el flujo:

1. **Anunciar completacion** del flujo
2. **Actualizar estado** en frontmatter del documento
3. **Verificar calidad** con checklist de items criticos
4. **Sugerir proximos pasos** o flujos de trabajo relacionados
5. **NO cargar pasos adicionales**: Es el final del flujo

---

## 8. Reglas Universales (incluir en CADA step)

Estas 4 reglas deben aparecer literalmente en cada archivo de step:

1. `NUNCA generes contenido sin entrada del usuario`
2. `CRITICO: Lee el archivo de paso completo antes de tomar cualquier accion`
3. `ERES UN FACILITADOR, no un generador de contenido`
4. `DEBES HABLAR SIEMPRE en {communication_language}`
