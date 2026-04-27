---
name: cv-desarrollador-junior
description: Analiza CVs y devuelve únicamente un JSON estructurado para un puesto de Desarrollador Junior. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor — Desarrollador Junior

Analizar todo el CV y devolver únicamente un JSON válido con la estructura definida sin agregar texto fuera del JSON y sin comentar o explicar líneas.

---

## REGLAS GENERALES DE PROCESAMIENTO

Carga y lee completamente el archivo:
`./steps/01-reglas-generales.md`

Estas reglas son **obligatorias y prioritarias**.
Posteriormente:
- Continúa con la ejecución de este documento.
- Aplica ambas fuentes de instrucciones de forma conjunta.
- En caso de conflicto, las reglas generales tienen prioridad.

# FASE 1 — GENERACIÓN DEL RESUMEN PROFESIONAL

El campo **resumen_profesional** debe generarse bajo las siguientes reglas obligatorias:

# Frase inicial obligatoria

El resumen **debe iniciar obligatoriamente con una paráfrasis muy ligera** (variación aproximada de 5 palabras) de la siguiente redacción base:
<!-- Experiencia del excel y definicion rol pdf -->
"Tengo más de 2 años de experiencia en programación en tecnologías de la Arquitectura de Referencia (AR) y/o tecnologías de código abierto.
Desarrollo y construyo componentes de software conforme a especificaciones técnicas definidas, participo en la implementación de sistemas y su puesta en funcionamiento mediante el uso de lenguajes de programación y fundamentos de desarrollo, colaboro activamente en equipo y sigo estándares, lineamientos y tiempos establecidos dentro del plan de trabajo."

Reglas para la paráfrasis:
- La estructura general debe mantenerse.
- Solo se permite una **variación ligera de vocabulario (aprox. 5 palabras)**.
- No debe agregar información que no exista en el CV.
- Esta frase funciona como **apertura del resumen profesional**.

# Desarrollo del resumen

Después de la frase inicial, el resumen debe continuar con **dos párrafos narrativos** que sinteticen la experiencia del perfil.

Reglas:
- Deben generarse **dos párrafos** cada uno con **máximo 4 renglones**.
- El resumen completo **no debe superar 180 palabras**.
- Debe redactarse en **prosa continua**.

## Reglas de contenido
El resumen debe:
- Ser claro y comprensible para lectores no técnicos.
- Sintetizar el perfil resaltando el valor aportado en términos de continuidad de servicios y cumplimiento de procesos
- Considerar la totalidad de la experiencia laboral descrita.
- Debe integrar de manera estratégica las capacidades clave asociadas al desarrollo de software, demostrando coherencia con responsabilidades como la creación, implementación y puesta a punto de sistemas mediante el uso de lenguajes de programación, así como la aplicación de fundamentos de programación y trabajo colaborativo en equipo.

El resumen **no debe**:
- Incluir certificaciones, cursos ni formación académica.
- Inventar información.
- Redactarse como lista de funciones o actividades.
- Estructurarse como enumeración explícita o implícita.
- Separar ideas en líneas independientes por actividad.
- Repetir la misma estructura gramatical en oraciones consecutivas.

---

# FASE 1.5 — FUNCIONES

El campo **funciones** debe generarse bajo las siguientes reglas obligatorias:

## Estructura obligatoria

La sección debe construirse en el siguiente orden:

## Primer párrafo (fijo)

Debe utilizarse exactamente la siguiente redacción:
<!-- funciones de las perfiles excel -->
"Creo sistemas (paquetes de software), los implemento y realizo su puesta a punto para asegurar su correcto funcionamiento, utilizando diversos lenguajes de programación. Cuento con sólidos conocimientos en conceptos de programación y trabajo en equipo, lo que me permite colaborar de manera efectiva en el desarrollo de soluciones tecnológicas."

- No modificar redacción.
- No parafrasear.
- No dividir.

## Segundo párrafo (paráfrasis controlada)

Debe generarse exclusivamente a partir del **segundo párrafo construido en FASE 1 (es decir, el párrafo generado como resumen posterior al párrafo inicial obligatorio)**.

Reglas:
- Debe ser una **paráfrasis ligera**, permitiendo modificar **máximo 10 palabras** respecto al texto original.
- Debe **conservar íntegramente el significado, intención y alcance** del párrafo base.
- Debe redactarse en **primera persona**, manteniendo coherencia gramatical y narrativa.
- **No debe agregar, omitir ni reinterpretar información**.
- Debe mantenerse como **un solo párrafo continuo**, sin fragmentaciones, listas ni reestructuración del contenido.
- Debe respetar el **orden lógico de las ideas** del texto original.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Desarrollador Junior")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Desarrollo o creación de sistemas o aplicaciones de software.
- Implementación o despliegue de soluciones tecnológicas.
- Uso de lenguajes de programación en actividades de desarrollo.
- Corrección de errores o mejoras en funcionalidades existentes.
- Trabajo colaborativo con equipos de desarrollo.
- Aplicación de conceptos fundamentales de programación.

Si no hay evidencia explícita → OMITIR.

No reinterpretar tareas administrativas o de soporte sin evidencia de desarrollo.

---

## Regla prioritaria: 2 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.
2. Agregar experiencias completas.
3. Detener cuando la suma alcance o supere ~2 años.
4. No recortar experiencias.
5. Si una es 1 año y otra 3 → incluir ambas.

**Si solo se agregó una experiencia, agregar las siguientes dos en orden cronológico, sin importar duración, para asegurar diversidad de experiencias.**

Si no hay experiencia relevante:

```json
"experiencia_laboral": []
```

---

# FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

Carga y lee completamente el archivo:

`./steps/02.1-resumen-consolidado.md`

Ejecuta todas las instrucciones definidas en ese archivo como parte de esta fase.
El resultado debe integrarse directamente en la salida final del JSON bajo los campos:
- `periodo_resumen_laboral`
- `resumen_laboral`

# REGLA ESPECIAL — PARÁFRASIS INICIAL DE LA PRIMERA EXPERIENCIA

Antes de listar cualquier actividad dentro de `actividades_principales` de la **primera experiencia laboral**, se debe ejecutar obligatoriamente la siguiente secuencia:

### 1. Paráfrasis obligatoria inicial

Se debe agregar como **primera actividad** una **paráfrasis muy ligera** de la siguiente redacción base:
<!-- funciones del rol del excel -->
> "Creo sistemas (paquetes de software), los implemento y hago una puesta a punto para que puedan ser funcionales, todo ello a través de lenguajes de programación.
Habilidades en; Conceptos de programación, Trabajo en equipo."

#### Reglas de la paráfrasis:
- Debe ser una **paráfrasis ligera** (máximo ~5 palabras modificadas).
- Debe **mantener el mismo significado**.
- Debe estar en **primera persona**.
- No debe **inventar ni agregar información**.
- Debe colocarse **como la primera actividad** dentro de `actividades_principales`.

---

### 2. Inserción de actividades base adicionales

**Inmediatamente después de la paráfrasis**, se deben agregar una parafrasis de **cada uno de los siguientes puntos como actividades independientes**:
<!-- actividades del rol del pdf path carrera -->
- Desarrollo y codifico componentes de software a partir de especificaciones técnicas definidas, aplicando fundamentos de programación.
- Participo en la implementación y puesta en funcionamiento de sistemas, asegurando su correcta operación en los entornos establecidos.
- Aplico de forma adecuada los estándares, lineamientos, frameworks y componentes definidos por la arquitectura del proyecto.
- Valido que las especificaciones técnicas asignadas sean claras y completas, solicitando apoyo en caso de dudas o inconsistencias.
- Cumplo con los tiempos, esfuerzo y calidad comprometidos en mis tareas, reportando avances de manera oportuna.
- Colaboro activamente con el equipo de trabajo, fomentando la comunicación y el aprendizaje continuo.
- Identifico, comunico y escalo oportunamente impedimentos, incidencias o riesgos en mis actividades.
- Acato las políticas, lineamientos y acuerdos del proyecto y de la organización (horarios, registro de actividades, estándares y buenas prácticas).

#### Reglas:
- Cada punto debe ser parafraseado de manera ligera (máximo ~3 palabras modificadas).
- Cada punto debe ser una **actividad separada**.
- Todas deben estar en **primera persona**.
- No deben **fusionarse ni agruparse**.
- Deben colocarse **antes de cualquier otra actividad existente** en la primera experiencia laboral.

---

### 3. Inserción de descripción de nivel de experiencia

**Después de los puntos de la sección 2**, se debe agregar como **una actividad adicional independiente** el siguiente texto:
<!-- seniority del rol del pdf path carrera -->
> "Resuelvo problemas técnicos sencillos y claramente definidos dentro del desarrollo de software, analizando alternativas mediante el uso de prácticas y procedimientos estandarizados; desempeño mis actividades bajo supervisión frecuente, fortaleciendo mi aprendizaje continuo, con posibles variaciones en los tiempos de entrega mientras consolido mi experiencia."

#### Reglas:
- Debe mantenerse **exactamente el mismo contenido** (sin paráfrasis).
- Debe respetarse como **una sola actividad**.
- Debe colocarse **antes de cualquier otra actividad original** de la experiencia.

---

### 4. Inserción de certificaciones y cursos

Agregar como **actividades independientes** cada certificación o curso identificado en:
`@cv/templates_input/certificaciones_cursos.txt`
Para cada elemento, se debe buscar su descripción correspondiente en:
`@cv/templates_input/herramientas_perfil.txt`

#### Formato obligatorio:

> "He usado la certificación [NOMBRE] {conector} [DESCRIPCIÓN]"

#### Reglas:

- Sustituye {conector} por unenlace natural, por ejemplo:
  - como, para, que me ha permitido, etc.
- Generar **una actividad por cada certificación y curso** identificado en `certificaciones_cursos.txt`.
- Para cada elemento, realizar una **búsqueda por coincidencia de nombre** en `certificaciones.txt`.
- La **descripción debe obtenerse del archivo de descripciones**, pero puede ajustarse mínimamente para integrarse de forma natural en la oración.
- No inventar descripciones si no existe coincidencia.
- Si **no se encuentra descripción**, no generar la actividad.
- Mantener siempre la redacción en **primera persona**.
- No duplicar certificaciones o cursos.
- Insertar estas actividades **antes de cualquier actividad original**.
- Mantener un orden consistente (orden de aparición en `certificaciones_cursos.txt`).

#### Regla de correspondencia (muy importante):

- La coincidencia debe ser por **nombre semánticamente equivalente**, por ejemplo:
  - "Scrum Alliance" ↔ "Scrum Foundation (2020)"
- Se permite normalizar:
  - eliminar años  
  - eliminar sufijos como "Foundation", "Certification", etc.  
- No usar coincidencias ambiguas o dudosas.

#### Ejemplo esperado:

Entrada:
- Scrum Alliance

Definición encontrada:
- Scrum Foundation (2020) → Fundamentos de metodologías ágiles basadas en Scrum, roles, eventos y artefactos

Salida:

> "He usado la certificación Scrum Alliance como fundamento para aplicar metodologías ágiles basadas en Scrum, considerando roles, eventos y artefactos."

### 5. Inserción de procesos en los que participo

**Después del punto 4**, se debe agregar el siguiente bloque como **actividades independientes**, respetando el orden:
<!-- procesos del pdf -->
- Participo en los siguientes procesos definidos por la metodología PDSS3 de atención de proyectos tradicionales de Softtek:
- CIS: Elaboro la especificación detallada de componentes.  
- CTR: Realizo la construcción de componentes.  
- DOC: Genero la documentación técnica.

#### Reglas:
- Cada elemento debe representarse como una **actividad separada**.
- Debe respetarse **exactamente el orden**.
- Debe colocarse **antes de cualquier otra actividad original**.

---

# FASE 3 — GENERACIÓN Y CONSOLIDACIÓN DE ACTIVIDADES

Esta fase se aplica **únicamente a las experiencias seleccionadas en FASE 2**.

## Objetivo
1. Generar `actividades_principales` para cada experiencia.
2. Consolidar todas las actividades dentro de la **primera experiencia (la más reciente)**.

---

## Reglas de redacción

Todas las actividades deben cumplir:
- Redacción clara y formal.
- Redacción **en primera persona**.
- No reinterpretar funciones ambiguas.
- No dividir, fusionar ni transformar actividades originales.
- Respetar la redacción original de las actividades extraídas del CV.

---

## Regla de consolidación

La **primera experiencia laboral (la más reciente)** funciona como **contenedor consolidado de actividades**.

Debe construirse respetando estrictamente el siguiente orden:

1. **Bloque obligatorio inicial completo**  
   (definido en `REGLA ESPECIAL — PARÁFRASIS INICIAL DE LA PRIMERA EXPERIENCIA`, incluye):
   - Paráfrasis inicial  
   - Actividades base (parafraseadas)  
   - Descripción de nivel de experiencia  
   - Certificaciones y cursos  
   - Procesos en los que participo  

2. **Actividades originales de la primera experiencia**

3. **Actividades de todas las demás experiencias seleccionadas**

---

## Procedimiento

### 1. Ordenar experiencias

Ordenar las experiencias seleccionadas **de la más reciente a la más antigua**.

### 2. Generar actividades por experiencia

Para cada experiencia:
- Extraer sus actividades del CV.
- Mantenerlas dentro de su experiencia correspondiente.
- No modificar su redacción.

### 3. Construcción de la primera experiencia (consolidación)

La primera experiencia debe construirse de la siguiente manera:

1. Insertar el **bloque obligatorio completo** definido en la REGLA ESPECIAL (en el orden exacto).
2. Agregar sus **actividades originales**.
3. Agregar **todas las actividades de las demás experiencias**, respetando el orden cronológico:

- experiencia 2  
- experiencia 3  
- experiencia 4  
- etc.

## Reglas de consistencia

Durante la consolidación:
- No eliminar actividades.
- No resumir actividades.
- No combinar actividades.
- No modificar el orden interno de las actividades de cada experiencia.
- No modificar la redacción de las actividades originales.
- No duplicar actividades.
- El bloque definido en la REGLA ESPECIAL es **obligatorio y no puede alterarse ni reordenarse**.

## Regla de prioridad

En caso de conflicto:
- La **REGLA ESPECIAL — PARÁFRASIS INICIAL DE LA PRIMERA EXPERIENCIA** tiene **prioridad absoluta** sobre cualquier otra instrucción de esta fase.

## Ejemplo conceptual

```json
{
  "experiencia_laboral": [
    {
      "empresa": "Empresa A",
      "puesto": "Líder Técnico",
      "fecha_inicio": "...",
      "fecha_fin": "...",
      "actividades_principales": [
        "Paráfrasis inicial...",
        "Actividad base 1...",
        "Actividad base 2...",
        "Actividad base 3...",
        "Nivel de experiencia...",
        "He usado la certificación X ...",
        "He usado la certificación Y ...",
        "ENG: ...",
        "ISP: ...",
        "PTO: ...",
        "FPT: ...",
        "PCR: ...",
        "Actividad propia experiencia A",
        "Actividad propia experiencia A",
        "Actividad experiencia B",
        "Actividad experiencia B",
        "Actividad experiencia C"
      ]
    },
    {
      "empresa": "Empresa B",
      "puesto": "Desarrollador",
      "fecha_inicio": "...",
      "fecha_fin": "...",
      "actividades_principales": [
        "Actividad experiencia B",
        "Actividad experiencia B"
      ]
    }
  ]
}
```

# FORMATO DE SALIDA

El resultado final debe cumplir exactamente con lo definido en `./steps/03-formato-salida.md`.
Cualquier desviación en estructura o campos se considera inválida.
