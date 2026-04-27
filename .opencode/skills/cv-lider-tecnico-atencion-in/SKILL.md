---
name: cv-lider-tecnico-atencion-in
description: Analiza CVs de Líder Técnico de atención de incidentes y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor - Líder Técnico de atención de incidentes

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

El campo **resumen_profesional** debe generarse bajo las siguientes reglas obligatorias.

# Frase inicial obligatoria

El resumen **debe iniciar obligatoriamente con el siguiente parrafo**

"Cuento con más de 5 años de experiencia en desarrollo de software, liderazgo técnico y atención y resolución de problemas. Poseo dominio de tecnologías de la Arquitectura de Referencia (AR) y/o tecnologías open source. Adicionalmente, tengo 3 años de experiencia trabajando bajo metodologías ágiles."

Reglas para la paráfrasis:
- La estructura general debe mantenerse.
- Solo se permite una **variación ligera de vocabulario (aprox. 15 palabras)**.
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
- Enfocarse en liderazgo y coordinación de equipos para la restauración de servicios ante fallas en aplicativos.
- Destacar la toma de decisiones críticas, gestión de incidentes, comunicación efectiva y responsabilidades clave en la continuidad operativa del servicio.

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

"Dirijo y coordino equipos de trabajo para restaurar servicios ante fallas que se presentan en la operación de los aplicativos, evaluando la situación, tomando decisiones críticas y asegurando una comunicación efectiva para la resolución de incidentes. Cuento con habilidades en toma de decisiones y liderazgo."

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


# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Lider Técnico de atención de incidentes")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Dirección o coordinación de equipos de trabajo en la restauración de servicios
- Liderazgo en la gestión de incidentes operativos
- Supervisión de la operación de aplicativos
- Aseguramiento de la continuidad y disponibilidad del servicio
- Toma de decisiones críticas ante fallas
- Evaluación de incidentes y definición de acciones correctivas
- Interacción con áreas técnicas y operativas
- Comunicación efectiva durante la resolución de incidentes
- Coordinación para la recuperación de servicios afectados
- Seguimiento a la ejecución de acciones para restablecer la operación  

Si no hay evidencia → OMITIR

No reinterpretar liderazgo administrativo sin componente técnico.

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
<!-- Funciones del excel y definicion rol pdf -->
"Dirijo y coordino a equipos de trabajo para restaurar un servicio ante fallas que se presenten en la operación de los aplicativos.
Evalúo la situación, tomo decisiones críticas y aseguro la comunicación efectiva para resolver el incidente. Habilidades en: Toma de decisiones, Liderazgo. Como líder técnico de atención de incidentes, planifico, controlo y doy seguimiento a la fase de resolución y estabilización, asegurando la correcta implementación de soluciones alineadas a la arquitectura de software, incluyendo patrones de diseño y la cobertura general de la aplicación. Tomo decisiones tecnológicas y de implementación utilizando y/o adaptando frameworks y estándares, y brindo asesoría al equipo técnico en la atención de incidentes complejos para garantizar la continuidad operativa."

#### Reglas de la paráfrasis:
- Debe ser una **paráfrasis ligera** (máximo ~5 palabras modificadas).
- Debe **mantener el mismo significado**.
- Debe estar en **primera persona**.
- No debe **inventar ni agregar información**.
- Debe colocarse **como la primera actividad** dentro de `actividades_principales`.

---

### 2. Inserción de actividades base adicionales

**Inmediatamente después de la paráfrasis**, se deben agregar una parafrasis de **cada uno de los siguientes puntos como actividades independientes**:

- Comprendo la propuesta de negocio y las necesidades del cliente, aplicándolas en la atención y resolución de incidentes en entornos productivos, especialmente en servicios y plataformas críticas.
- Defino planes de trabajo detallados para la atención de incidentes, priorizando actividades conforme a su severidad (P1–P4) y asegurando el cumplimiento de SLA/OLA.
- Estimo y asigno tareas técnicas necesarias para la resolución de incidentes, coordinando esfuerzos entre desarrolladores, especialistas e infraestructura.
- Colaboro con el arquitecto en la definición de soluciones técnicas durante incidentes, asegurando alineación con la arquitectura y estándares establecidos.
- Aseguro la aplicación de estándares de codificación y bases de datos durante la implementación de soluciones correctivas.
- Asesoro y coordino a ingenieros de software en la atención de incidentes, especialmente en escenarios críticos o de alta complejidad.
- Garantizo el uso adecuado de frameworks y subsistemas de soporte para asegurar la correcta atención de requerimientos no funcionales como seguridad, disponibilidad, escalabilidad y desempeño.
- Administro la configuración de los componentes involucrados en la solución de incidentes, asegurando control y trazabilidad de cambios.
- Desarrollo y/o coordino implementaciones de solución (fixes, hotfixes) para restaurar servicios afectados.
- Aseguro la aplicación de checklists en la validación de soluciones antes de su liberación a producción.
- Coordino la integración de componentes técnicos dentro de la arquitectura para garantizar una recuperación estable del servicio.
- Defino prioridades en cada iteración de atención de incidentes, enfocándome en minimizar el impacto al negocio.
- Promuevo la aplicación de patrones de diseño en las soluciones implementadas para evitar recurrencias.
- Participo en la definición de esquemas de integración entre aplicaciones durante la resolución de incidentes.
- Coordino la atención de incidentes críticos (Major Incidents), liderando convocatorias, toma de decisiones técnicas y comunicación durante la contingencia.
- Identifico la causa raíz de incidentes y lidero análisis post-incidente (RCA), implementando acciones preventivas para evitar recurrencias.
- Trabajo en entornos de operación continua, asegurando la estabilidad y continuidad del servicio después de la resolución de incidentes.
- Actúo como punto de escalamiento técnico y enlace entre mesa de servicios, desarrollo, infraestructura y seguridad.
- Genero resultados medibles en la mejora de la operación, reduciendo tiempos de atención, reincidencias e impacto al negocio.
- Mantengo una trayectoria continua en roles de atención y gestión de incidentes, consolidando experiencia en entornos productivos.

#### Reglas:
- Cada punto debe ser parafraseado de manera ligera (máximo ~3 palabras modificadas).
- Cada punto debe ser una **actividad separada**.
- Todas deben estar en **primera persona**.
- No deben **fusionarse ni agruparse**.
- Deben colocarse **antes de cualquier otra actividad existente** en la primera experiencia laboral.

---

### 3. Inserción de descripción de nivel de experiencia

**Después de los puntos de la sección 2**, se debe agregar como **una actividad adicional independiente** el siguiente texto con una ligera paráfrasis:
<!-- seniority del rol del pdf path carrera -->
> "He participado en proyectos de más de 20 mil horas, donde lidero la atención de incidentes y defino soluciones para requerimientos no funcionales, asegurando la estabilidad y el correcto desempeño de los sistemas en producción. Además, planifico y coordino equipos de más de 15 ingenieros de software durante la resolución de incidentes, garantizando una ejecución eficiente y oportuna de las actividades."

#### Reglas:
- Debe ser parafraseado de manera ligera (máximo ~15 palabras modificadas).
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

- Participo en los siguientes procesos definidos por la metodología PDSS3 de atención de proyectos tradicionales de Softtek:
- CTR: Diseño y preparo testware, además de ejecutar pruebas independientes.
- STD: Diseño y preparo testware, así como generar scripts de pruebas de desempeño.
- STE: Ejecuto escenarios de prueba.
- INT: Diseño y preparo testware.
- UAT: Apoyo en las actividades de pruebas del usuario.

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
