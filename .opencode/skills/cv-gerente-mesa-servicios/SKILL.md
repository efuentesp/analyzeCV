---
name: cv-gerente-mesa-servicios
description: Analiza CVs de Gerente de Mesa de Servicios y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor - Gerente de Mesa de Servicios

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

El resumen **debe iniciar obligatoriamente con una paráfrasis muy ligera** (variación aproximada de 10 palabras) de la siguiente redacción base:

# Frase inicial obligatoria
palabras) de la siguiente redacción base:
<!-- Experiencia del excel y definicion rol pdf -->
"Cuento con más de menos 5 años de experiencia en mesa de servicios. Soy responsable de asegurar el cumplimiento del desempeño del servicio, gestionando la satisfacción del cliente con base en los niveles de servicio y CTQs establecidos. Administro los cambios operativos y contractuales, y garantizo una adecuada gestión de riesgos y defectos que puedan impactar los compromisos adquiridos. Asimismo, impulso la optimización del servicio mediante la implementación de mejores prácticas y la mejora continua, asegurando una operación estable, eficiente y alineada a los objetivos del negocio."

Reglas para la paráfrasis:
- La estructura general debe mantenerse.
- Solo se permite una **variación ligera de vocabulario (aprox. 10 palabras)**.
- No debe agregar información que no exista en el CV.
- Esta frase funciona como **apertura del resumen profesional**.

# Desarrollo del resumen

Después de la frase inicial, el resumen debe continuar con **dos párrafos narrativos** que sinteticen la experiencia del perfil.

Reglas:
- Deben generarse **dos párrafos**.
- Cada párrafo debe tener **máximo 4 renglones**.
- El resumen completo **no debe superar 160 palabras**.
- Debe redactarse en **prosa continua**.

## Reglas de contenido

El resumen debe:
- Considerar la totalidad de la experiencia laboral descrita.
- Ser claro y comprensible para lectores no técnicos.
- Sintetizar el perfil resaltando el valor aportado en términos de continuidad de servicios y cumplimiento de procesos.
- Debe integrar de manera estratégica las capacidades clave asociadas a la gestión de continuidad operativa, demostrando coherencia con responsabilidades como dirección y coordinación de equipos para restaurar servicios ante fallas en la operación de los aplicativos.

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
<!-- funciones del rol el excel de perfiles -->
"Dirijo y coordino a los equipos de trabajo de las líneas de continuidad para restaurar un servicio ante fallas que se presenten en la operación de los aplicativos."

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

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Gerente de Mesa de Servicios")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Dirección o coordinación de equipos de trabajo para la restauración de servicios.  
- Gestión de la continuidad operativa ante fallas en aplicativos.  
- Supervisión de la resolución de incidentes en la operación de sistemas.  
- Planificación y asignación de actividades para asegurar la disponibilidad del servicio.  
- Monitoreo y seguimiento de la ejecución de acciones correctivas.  
- Interacción con áreas técnicas y operativas para garantizar la recuperación del servicio.

Si no hay evidencia explícita → OMITIR.

No reinterpretar soporte técnico o funciones administrativas como gerencia de mesa de servicios.

---

## Regla prioritaria: 5 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.
2. Agregar experiencias completas.
3. Detener cuando la suma alcance o supere ~5 años.
4. No recortar experiencias.
5. Si una es 3 años y otra 4 → incluir ambas.

**Si solo se agregó una experiencia, agregar las siguientes dos en orden cronológico, sin importar duración, para asegurar diversidad de experiencias.**

Si no hay experiencia relevante:

```json
"experiencia_laboral": []
```

# FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

Carga y lee completamente el archivo:

`./steps/02.1-resumen-consolidado.md`

Ejecuta todas las instrucciones definidas en ese archivo como parte de esta fase.
El resultado debe integrarse directamente en la salida final del JSON bajo los campos:
- `periodo_resumen_laboral`
- `resumen_laboral`

# REGLA ESPECIAL — PARÁFRASIS INICIAL DE LA PRIMERA EXPERIENCIA

Antes de listar cualquier actividad dentro de `actividades_principales` de la **primera experiencia laboral**, se debe agregar una **paráfrasis muy ligera** de la siguiente redacción base:

"Dirijo y coordino a los equipos de trabajo de las líneas de continuidad para restaurar un servicio ante fallas que se presenten en la operación de los aplicativos."

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
- Dirijo y coordino equipos de trabajo de múltiples líneas de continuidad para restaurar servicios ante fallas en la operación de aplicativos, asegurando una atención efectiva en entornos multi-equipo.
- Realizo revisiones mensuales de los servicios a mi cargo, dando seguimiento al desempeño operativo e impulsando acciones de mejora continua.
- Monitoreo y reporto KPIs operativos (SLA/OLA, TTA/TTR, % de cumplimiento y calidad), asegurando su actualización sistemática y el cumplimiento de objetivos del servicio.
- Opero bajo esquemas definidos para garantizar la continuidad del servicio en distintos niveles de demanda.
- Coordino mesas de servicio, asegurando la correcta ejecución de procesos y niveles de servicio.
- Domino y administro el ciclo de vida del ticket (Nuevo, Asignado, En curso, Pendiente, Resuelto, Cerrado/Cancelado), asegurando el cumplimiento de reglas de transición.
- Gestiono catálogos, categorías, prioridades y grupos de soporte para una correcta operación del servicio.
- Mantengo actualizada y vigente la matriz de escalamiento, definiendo niveles, horarios y criterios de atención.
- Gestiono incidentes de extremo a extremo, desde su registro hasta su cierre, asegurando comunicación efectiva con los involucrados.
- Administro la gestión de problemas mediante análisis de causa raíz (RCA), definición de workarounds y documentación en KEDB, garantizando trazabilidad con incidentes.
- Coordino la gestión de cambios (RFC, análisis de impacto/riesgo, CAB, implementación y revisión) alineada a los lineamientos del comité correspondiente.
- Mantengo la gestión de configuración (CMDB) asegurando la relación entre elementos de configuración, tickets, cambios y liberaciones.
- Fomento la gestión del conocimiento mediante la generación de artículos, FAQs y registro de errores conocidos a partir de incidentes y problemas.
- Soporto procesos de liberación desde la mesa mediante herramientas que gestionen, ventanas, freezes y comunicación.
- Genero reportes y dashboards periódicos de la operación de la mesa y gestiono planes de mejora derivados de auditorías.
- Identifico, evalúo y gestiono riesgos asociados a la prestación de servicios, implementando medidas de mitigación para asegurar la continuidad operativa.

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
> "Experiencia en coordinación de equipos de soporte, gestión integral de incidentes, problemas y cambios, administración de KPIs y procesos de mejora continua. Enfocado en asegurar la continuidad operativa, la calidad del servicio y la eficiencia en entornos multi-equipo, gestionando iniciativas con un esfuerzo que pueden estar entre 5,000 y 10,000 horas con equipos de entre 10 y 15 participantes, coordinando a líderes con menor seniority y asegurando la correcta ejecución de las actividades. Asimismo, reporto avances y resultados a niveles de gerencia media del cliente y de la organización."

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
- ISP: Defino la operación del servicio alineando objetivos, alcance, recursos, SLAs y equipo de trabajo.
- PTO: Doy seguimiento al desempeño del servicio, monitoreo KPIs y gestiono desviaciones operativas.
- FPT: Aseguro el cierre ordenado de servicios o etapas, validando entregables, reportes y lecciones aprendidas.
- CHM: Gestiono cambios operativos y de servicio, evaluando su impacto y asegurando su correcta implementación.
- SCM: Controlo configuraciones y versiones de componentes del servicio, garantizando trazabilidad y continuidad operativa.

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

# FASE 3 — GENERACIÓN Y CONSOLIDACIÓN DE ACTIVIDADES

Esta fase se aplica **únicamente a las experiencias seleccionadas en FASE 2**.
El objetivo es:
1. Generar `actividades_principales` para cada experiencia.
2. Consolidar todas las actividades dentro de la **primera experiencia (la más reciente)**.

# Reglas de redacción

Todas las actividades deben cumplir:
- Redacción clara y formal.
- Redacción **en primera persona**.
- No reinterpretar funciones ambiguas.
- No dividir, fusionar ni transformar actividades originales.

# Regla de consolidación

La **primera experiencia laboral (la más reciente)** funciona como **contenedor consolidado de actividades**.

Debe contener, en este orden:
1. **Paráfrasis inicial obligatoria**  
   (definida en `REGLA ESPECIAL — PARÁFRASIS INICIAL DE LA PRIMERA EXPERIENCIA`)
2. **Actividades originales de esa experiencia**
3. **Actividades de todas las demás experiencias seleccionadas**

Las actividades de las experiencias posteriores se agregan **sin modificar su redacción**.

# Procedimiento

### 1. Ordenar experiencias

Ordenar las experiencias seleccionadas **de la más reciente a la más antigua**.

### 2. Generar actividades por experiencia

Para cada experiencia:
- Extraer sus actividades del CV.
- Mantenerlas dentro de su experiencia correspondiente.

### 3. Construir actividades de la primera experiencia

La primera experiencia debe construirse así:
1. Insertar la **paráfrasis inicial**.
2. Agregar sus **actividades originales**.
3. Agregar **todas las actividades de las demás experiencias**, respetando el orden cronológico:
- experiencia 2  
- experiencia 3  
- experiencia 4  
- etc.

# Reglas de consistencia

Durante la consolidación:
- No eliminar actividades.
- No resumir actividades.
- No combinar actividades.
- No modificar el orden interno de las actividades de cada experiencia.
- No modificar la redacción.
- No duplicar actividades.

# Ejemplo conceptual

```json
{
  "experiencia_laboral": [
    {
      "empresa": "Empresa A",
      "puesto": "Líder Técnico",
      "fecha_inicio": "...",
      "fecha_fin": "...",
      "actividades_principales": [
        "Paráfrasis inicial de liderazgo técnico...",
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

```json
{
  "nombre": "",
  "mail":"",
  "genero":"",
  "fecha_nacimiento":"",
  "rfc":"",
  "curp":"",
  "no_cedula":"",
  "fecha_cedula":"",
  "rol_propuesto": "",
  "resumen_profesional": "",
  "experiencia_laboral": [
    {
      "empresa": "",
      "puesto": "",
      "fecha_inicio": "",
      "fecha_fin": "",
      "actividades_principales": []
    }
  ],
  "periodo_resumen_laboral": "",
  "resumen_laboral": "",
  "estudios": {
    "carrera": "",
    "lugar": "",
    "periodo": ""
  },
  "certificaciones": [
    {
      "nombre": "",
      "anio": ""
    }
  ],
  "cursos": [
    {
      "nombre": ""
    }
  ]
}
```