---
name: cv-analista-senior
description: Analiza CVs de Analista Senior y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor - Analista Senior

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

El resumen **debe iniciar obligatoriamente con una paráfrasis muy ligera** (variación aproximada de 10 palabras) de la siguiente redacción base:
<!-- Experiencia del excel y definicion rol pdf -->
"Cuento con más de 5 años de experiencia en el análisis de sistemas, aplicaciones, servicios, procesos y soluciones de Inteligencia de Negocio, así como en la gestión y coordinación de equipos de trabajo.
Como analista de negocio, soy responsable de descubrir, sintetizar y analizar información proveniente de diversas fuentes, incluyendo herramientas, procesos, documentación y stakeholders."

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
- Debe integrar de manera estratégica las capacidades clave asociadas al análisis de requerimientos, demostrando coherencia con responsabilidades como levantamiento y documentación de requerimientos complejos, coordinación con equipos de desarrollo, QA y negocio, validación funcional, interlocución con usuarios, liderazgo de analistas junior y gestión integral de los requerimientos del proyecto.

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

"Analizo las propuestas de requerimientos de mejora tecnológica y de procesos, participando en el levantamiento y documentación de requerimientos complejos, así como en la coordinación con desarrolladores, testers y áreas de negocio. Realizo validaciones funcionales mediante pruebas de aceptación y seguimiento a QA, mantengo interlocución constante con usuarios y coordino las actividades de analistas junior, asegurando un conocimiento integral de los requerimientos del proyecto asignado. Cuento con habilidades de liderazgo, identificación de problemas y propuesta de soluciones, así como dominio en el uso de herramientas y metodologías de análisis como Design Thinking y UML. Además, me comunico eficazmente con diferentes audiencias y elaboro documentación bajo marcos de trabajo tradicionales y ágiles."

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

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Analista Senior")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Levantamiento y documentación de requerimientos funcionales o de negocio.
- Análisis y validación de requerimientos con usuarios o áreas de negocio.
- Coordinación con equipos de desarrollo, QA o testers.
- Ejecución o seguimiento de validación funcional (pruebas de aceptación, QA).
- Interlocución directa con usuarios o stakeholders.
- Liderazgo o coordinación de analistas junior.
- Gestión integral o seguimiento de requerimientos dentro de un proyecto.
- Uso de metodologías o herramientas de análisis (Design Thinking, UML, metodologías ágiles o tradicionales).

Si no hay evidencia explícita → OMITIR.

No reinterpretar actividades administrativas generales sin responsabilidad sobre control o entrega documental.

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

"Analicé propuestas de mejora tecnológica y de procesos, participando en el levantamiento y documentación de requerimientos complejos. Coordiné actividades con desarrolladores, testers y áreas de negocio, realicé validación funcional mediante pruebas de aceptación y seguimiento a QA, y mantuve interlocución directa con usuarios. Además, coordiné a analistas junior y aseguré un entendimiento integral de los requerimientos del proyecto asignado. Apliqué habilidades de liderazgo, identificación de problemas y propuesta de soluciones, utilizando herramientas y metodologías de análisis como Design Thinking y UML, así como comunicación efectiva con distintas audiencias y elaboración de documentación en marcos de trabajo tradicionales y ágiles."

## Reglas de la paráfrasis
- Debe ser una **paráfrasis ligera** con un cambio aproximado de **15 a 20 palabras como máximo**.
- Debe **mantener el mismo significado**.
- Debe estar en **primera persona**.
- No debe **inventar ni agregar información**.
- Debe colocarse **como la primera actividad** dentro de `actividades_principales`.

---

### 2. Inserción de actividades base adicionales

**Inmediatamente después de la paráfrasis**, se deben agregar una parafrasis de **cada uno de los siguientes puntos como actividades independientes**:
<!-- actividades del rol del pdf path carrera -->

 Entiendo las verdaderas necesidades mediante el uso de un conjunto de técnicas de análisis.
- Involucro a los stakeholders para descubrir los requerimientos funcionales, no funcionales y de transición, documentándolos de manera completa, clara, correcta, consistente, factible y libre de ambigüedad.
- Genero las especificaciones de los requerimientos no funcionales, describiendo las cualidades y restricciones que deben considerarse para su implementación.
- Identifico patrones funcionales para diseñar soluciones que se conviertan en herramientas efectivas, permitiendo a los stakeholders ejecutar sus procesos de negocio con eficacia y facilidad.
- Diseño la solución funcional que satisface los requerimientos de los stakeholders, junto con la estrategia de implementación necesaria para generar valor al negocio.
- Aseguro que la solución sea aprobada conscientemente por los stakeholders, que cumpla con los objetivos planteados y que su implementación se lleve a cabo sin percances.
- Expreso los resultados del análisis y comunico claramente los requerimientos a los equipos implementadores.
- Administro y doy seguimiento a los cambios de alcance durante el ciclo de vida de la solución.

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
> "Participó en el entendimiento de las capacidades tecnológicas y evalúo la viabilidad de soluciones para grandes aplicaciones. Colaboro en sesiones de trabajo con usuarios, sponsors técnicos y de negocio, donde lidero el diseño del modelo de datos y defino el patrón de diseño de pantallas de usuario. Asimismo, identifico capacidades tecnológicas y de implementación, y facilito evidencia al líder de proyecto sobre cambios de alcance, contribuyendo a negociaciones exitosas en costo y calendario."

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
- REQ: Encabezo las actividades de generación de los requerimientos y produzco los entregables correspondientes.
- SFD: Encabezo las actividades de diseño funcional de la solución, asegurando la correcta generación de los entregables.
- ARC: Proveo las entradas necesarias al proceso, principalmente los requerimientos funcionales.
- DBI: Proveo el modelo lógico de base de datos (modelo de dominio) y las especificaciones de los componentes funcionales.
- CIS: Proveo entradas al proceso y valido la precisión de los entregables.
- GUI: Proveo entradas y valido la precisión del diseño de la interfaz gráfica de usuario.
- INT: Proveo las entradas necesarias para la integración de sistemas.
- STD: Participo en las actividades de diseño de pruebas de sistema.
- STE: Participo en la ejecución de las pruebas de sistema.
- DOC: Proveo entradas y valido la precisión de los entregables de documentación.
- UAT: Apoyo en las actividades de usuario según lo solicitado durante las pruebas de aceptación.

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