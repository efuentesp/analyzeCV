---
name: cv-desarrollador-bi-atencion-in2
description: Analiza CVs y devuelve únicamente un JSON estructurado para el rol de Desarrollador BI de atención de incidentes.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor — Desarrollador BI de atención de incidentes

Analizar todo el CV y devolver únicamente un JSON válido con la estructura definida sin agregar texto fuera del JSON y sin comentar o explicar líneas.

---

# REGLAS GENERALES

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
"Cuento con al menos 3 años en desarrollo de soluciones de BI, en servicios y aplicaciones web (frontend y backend), dashboards interactivos, tableros, informes automáticos y reportes. 
Domino tecnologías de la Arquitectura de Referencia (AR) y/o tecnologías de código abierto aplicadas a entornos de Inteligencia de Negocio. Analizo, corrijo y doy mantenimiento a procesos y componentes BI para la atención de incidentes, generando y ajustando código conforme a la especificación técnica. Ejecuto las actividades de soporte y desarrollo de acuerdo con lo establecido, apegándome a estándares, arquitectura y frameworks definidos, asegurando la calidad de la información, la continuidad operativa y el cumplimiento de los tiempos establecidos."

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
- Integrar de manera estratégica las capacidades clave asociadas al mantenimiento y soporte de aplicativos de Inteligencia de Negocio, demostrando coherencia con responsabilidades como la gestión de bases de datos relacionales y no relacionales, modelado de datos, desarrollo de procesos de Extraer, Transformar y Cargar (ETL) y uso de herramientas de versionamiento de código.

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

"Analizo las propuestas de requerimientos de mejora tecnológica y de procesos, participando en el levantamiento y documentación de requerimientos complejos, así como en la coordinación con desarrolladores, testers y áreas de negocio. Realizo validaciones funcionales mediante pruebas de aceptación y seguimiento a Pruebas, mantengo interlocución constante con usuarios y coordino las actividades de analistas junior, asegurando un conocimiento integral de los requerimientos del proyecto asignado. Cuento con habilidades de liderazgo, identificación de problemas y propuesta de soluciones, así como dominio en el uso de herramientas y metodologías de análisis como Design Thinking y UML. Además, me comunico eficazmente con diferentes audiencias y elaboro documentación bajo marcos de trabajo tradicionales y ágiles."

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

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Desarrollador BI de atención de incidentes")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Mantenimiento y soporte de aplicativos de Inteligencia de Negocio  
- Resolución de problemas técnicos en soluciones de BI  
- Manejo de bases de datos relacionales y no relacionales  
- Diseño y modelado de datos  
- Desarrollo y mantenimiento de procesos Extraer, Transformar y Cargar (ETL) 
- Integración y procesamiento de datos  
- Uso de herramientas de versionamiento de código (Git)  
- Aseguramiento del correcto funcionamiento de soluciones de BI

Si no hay evidencia explícita → OMITIR.

No reinterpretar soporte técnico básico o tareas operativas como mantenimiento o desarrollo de soluciones de Inteligencia de Negocio.

---

## Regla prioritaria: 3 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.
2. Agregar experiencias completas.
3. Detener cuando la suma alcance o supere ~3 años.
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

Se debe agregar como **primera actividad** una **paráfrasis muy ligera** de la siguiente redacción base:
<!-- funciones del rol del excel -->
"Mantengo y doy soporte a los aplicativos de Inteligencia de Negocio dominando varios lenguajes de programación.
Habilidades en; Dominio de Bases de Datos relacionales y no relacionales., Técnicas de diseño para el Modelado de Datos, Versionamiento del código (Git), Dominio en el diseño y desarrollo de procesos de Extraer, Transformar y Cargar (ETL)"

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
- Diseño, desarrollo y doy mantenimiento a soluciones de BI (dashboards, reportes, tableros automáticos y servicios web frontend/backend), asegurando al menos 2 años de experiencia en este tipo de implementaciones.
- Construyo, implemento y pongo en operación componentes y sistemas BI mediante lenguajes de programación, garantizando su correcto funcionamiento en ambientes productivos.
- Implemento user stories cumpliendo estándares de codificación y ejecuto pruebas unitarias para asegurar la calidad de los desarrollos.
- Analizo y corrijo hallazgos de seguridad (SAST/DAST), documentando las remediaciones aplicadas en los componentes BI.
- Preparo artefactos técnicos (manuales de instalación/configuración) y doy soporte a la integración y entrega de paquetes a AVL.
- Registro y gestiono tareas e incidencias en GitLab, siguiendo flujos de ramas, versionamiento y etiquetado definidos.
- Documento evidencias de cada fase del desarrollo y soporte para su integración en carpetas y VoBo.
- Participo en ambientes INT, UAT y PROD, atendiendo y resolviendo defectos hasta obtener VoBo.
- Mantengo una trayectoria laboral consistente, acumulando al menos 2 años de experiencia en desarrollo BI y atención de incidentes, con fechas claras y sin traslapes.
- Aplico conocimientos en bases de datos relacionales y no relacionales, modelado de datos, versionamiento con Git, desarrollo de aplicaciones web y procesos ETL/ELT.
- Cumplo con tiempos, esfuerzo y calidad comprometidos, generando métricas de ejecución como tickets/historias cerradas por sprint, cobertura de pruebas y cumplimiento en tiempos de atención de incidentes.
- Atiendo incidentes en entornos productivos de BI, analizando, reproduciendo y corrigiendo fallas mediante bugfix, hotfix y parches.
- Participo en la resolución de incidentes según su severidad/prioridad, asegurando continuidad operativa y estabilidad de la información.
- Realizo validaciones técnicas posteriores a cada corrección para garantizar la solución definitiva del incidente.
- Colaboro con equipos de soporte, pruebas y usuarios técnicos durante la atención de incidentes, asegurando una comunicación efectiva.
- Documento soluciones técnicas, lecciones aprendidas y contribuyo a bases de conocimiento para mejora continua.
- Identifico, gestiono y escalo riesgos e issues técnicos que puedan afectar la operación de soluciones BI.
- Aseguro el cumplimiento de estándares, lineamientos del proyecto y buenas prácticas de desarrollo, calidad y operación.

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
> "Cuento con sólidos conocimientos en soluciones de BI que me permiten analizar y resolver incidentes complejos mediante el uso de herramientas y procesos establecidos, aplicando mejores prácticas en todo momento. Identifico, notifico y prevengo riesgos que puedan afectar la calidad de la información y la continuidad operativa; además, valido correcciones, ejecuto pruebas y documento evidencias durante la atención de incidentes. Trabajo de forma autónoma con mínima supervisión, cumpliendo los tiempos comprometidos y manteniendo un alto nivel de especialización en entornos BI."

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
- CIS: Elaboro especificaciones detalladas de componentes y servicios, asegurando su alineación con los requerimientos operativos, los niveles de servicio (SLAs) y los estándares definidos.
- CTR: Coordino y superviso la construcción e implementación de componentes y soluciones, garantizando su correcta integración dentro del modelo de operación del servicio.
- DOC: Genero y mantengo la documentación técnica y operativa, asegurando la trazabilidad, estandarización y soporte a la continuidad y mejora del servicio.

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
