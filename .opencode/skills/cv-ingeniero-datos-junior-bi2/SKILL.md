---
name: cv-ingeniero-datos-junior-bi2
description: Analiza CVs y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor — Ingeniero de Datos Junior BI

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
"Cuento con al menos 2 años de experiencia en el análisis de grandes volúmenes de datos y en el desarrollo de soluciones de Inteligencia de Negocio.
Responsable de la construcción de soluciones de datos, asegurando la implementación y uso de arquitecturas de datos para la recolección, almacenamiento y procesamiento de grandes volúmenes de información, participando en la toma de decisiones tecnológicas mediante el uso y/o adaptación de herramientas, frameworks y estándares, así como brindar apoyo al equipo técnico en la optimización y gestión eficiente de los datos para soluciones de Inteligencia de Negocio."

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
- Considerar la totalidad de la experiencia laboral descrita.
- Ser claro y comprensible para lectores no técnicos.
- Sintetizar el perfil resaltando el valor aportado en términos de continuidad de servicios y cumplimiento de procesos.
- Debe integrar de manera estratégica las capacidades clave asociadas al rol, demostrando coherencia con responsabilidades como diseño de soluciones de datos, modelado, procesos ETL.

El resumen **no debe**:
- Incluir certificaciones, cursos ni formación académica.
- Inventar información.
- Redactarse como lista de funciones o actividades.
- Estructurarse como enumeración explícita o implícita.
- Separar ideas en líneas independientes por actividad.
- Repetir la misma estructura gramatical en oraciones consecutivas.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Ingeniero de Datos BI Junior")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Diseño y construcción de soluciones de datos  
- Desarrollo y mantenimiento de infraestructuras de datos  
- Procesamiento y manejo de grandes volúmenes de datos  
- Diseño e implementación de procesos ETL/ELT  
- Integración y transformación de datos  
- Construcción y mantenimiento de data warehouses o data lakes  
- Optimización de carga, procesamiento y consulta de datos  
- Aseguramiento de eficiencia, escalabilidad y seguridad en soluciones de datos  
- Modelado de datos para soluciones de Inteligencia de Negocio  
- Acceso y disponibilidad de datos para análisis  

Si no hay evidencia explícita → OMITIR.

No reinterpretar soporte técnico o funciones administrativas como ingeniería de datos.

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
> "Diseño, construyo, optimizo y mantengo infraestructuras y soluciones tecnológicas que recolectan, almacenan, procesan y permiten acceder a grandes volúmenes de datos de manera eficiente, segura y escalable.
Cuento con habilidades en el diseño e implementación de procesos Extraer, Transformar y Cargar (ETL/ELT) para el procesamiento de grandes volúmenes de información, así como en la definición, construcción y mantenimiento de estructuras de almacenamiento que aseguran la eficiencia de las soluciones de Inteligencia de Negocio. Además, optimizo la carga, el procesamiento y la consulta de grandes volúmenes de datos."

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
- Apoyo en el diseño y construcción de procesos de integración de datos (ETL/ELT).  
- Desarrollo y mantengo pipelines de datos para la ingesta, transformación y carga de información.  
- Colaboro en la definición y mantenimiento de estructuras de almacenamiento (Data Warehouse, Data Lake).  
- Aseguro la calidad, integridad y consistencia de los datos procesados.  
- Optimizo consultas y procesos de carga para mejorar el rendimiento de las soluciones.  
- Apoyo en la documentación de flujos, procesos y modelos de datos.  
- Monitoreo la ejecución de procesos de datos y atiendo incidencias básicas.  
- Colaboro con equipos de BI y analítica para la correcta disponibilidad de la información.  
- Aplico buenas prácticas en el manejo, seguridad y gobierno de datos.  

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
> "Resuelvo problemas relacionados con la integración, procesamiento y calidad de datos, analizando posibles soluciones mediante el uso de procedimientos y buenas prácticas estandarizadas. Trabajo bajo un nivel de supervisión frecuente y reconozco que los tiempos de entrega pueden presentar cierta variabilidad mientras consolido experiencia en soluciones de Ingeniería de Datos para Inteligencia de Negocio."

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
