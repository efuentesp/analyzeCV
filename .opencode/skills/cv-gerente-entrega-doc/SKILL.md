---
name: cv-gerente-entrega-doc
description: Analiza CVs de Gerente de Entrega Documental y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor - Gerente de Entrega Documental

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

El campo **resumen_profesional** debe generarse bajo las siguientes reglas obligatorias.

# Frase inicial obligatoria

El resumen **debe iniciar obligatoriamente con una paráfrasis muy ligera** (variación aproximada de 5 palabras) de la siguiente redacción base:
<!-- Experiencia del excel y definicion rol pdf -->
"Cuento con más de 5 años de experiencia en entrega documental. Realizo labores de mentoría y acompañamiento para que los responsables de la entrega documental a mi cargo ejecuten correctamente el proceso, asegurando el cumplimiento de calendarios, lineamientos, calidad de la documentación y compromisos acordados con el cliente."

Reglas para la paráfrasis:
- La estructura general debe mantenerse.
- Solo se permite una **variación ligera de vocabulario (aprox. 5 palabras)**.
- No debe agregar información que no exista en el CV.
- Esta frase funciona como **apertura del resumen profesional**.

---

# Desarrollo del resumen

Después de la frase inicial, el resumen debe continuar con **dos párrafos narrativos** que sinteticen la experiencia del perfil.

Reglas:
- Deben generarse **dos párrafos**.
- Cada párrafo debe tener **máximo 4 renglones**.
- El resumen completo **no debe superar 160 palabras**.
- Debe redactarse en **prosa continua**.

---

## Reglas de contenido

El resumen debe:
- Considerar la totalidad de la experiencia laboral descrita.
- Ser claro y comprensible para lectores no técnicos.
- Sintetizar el perfil resaltando el valor aportado en términos de continuidad de servicios y cumplimiento de procesos.
- Debe integrar de manera estratégica las capacidades clave asociadas a la gestión documental, demostrando coherencia con responsabilidades como entrega de documentación, recopilación de firmas y resguardo de evidencias de los servicios prestados.

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
"Doy seguimiento y realizo la entrega documental y la recopilación de firmas que sustentan las evidencias de los servicios prestados."

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

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Gerente de Entrega Documental")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Entrega y gestión de documentación relacionada con los servicios prestados.
- Recopilación y validación de firmas que respalden evidencias de servicio.
- Seguimiento al cumplimiento de requerimientos documentales.
- Coordinación con áreas internas o externas para formalizar la documentación.
- Control, resguardo y trazabilidad de evidencias documentales.
- Verificación de integridad, consistencia y calidad de la documentación antes de su entrega.

Si no hay evidencia explícita → OMITIR.

No reinterpretar soporte técnico o funciones administrativas como gerencia de entrega documental.

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

"Doy seguimiento y realizo la entrega documental, así como la recopilación de firmas que sustentan las evidencias de los servicios prestados."

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
- Coordino la elaboración y entrega de la Carpeta Consolidada de Servicios y la Carpeta Consolidada de Niveles de Servicio mensual, asegurando el cumplimiento de los plazos establecidos.
- Consolido oportunamente los insumos de evidencia (actas, reportes, tableros, métricas) que alimentan el dictamen mensual y el proceso de pago.
- Gestiono la calidad documental de los paquetes mensuales, asegurando formato, numerales, control de versiones, firmas y trazabilidad.
- Integro los documentos EUHE (3-puntos), PT (WBS) y PSE como parte de la CAPA, asegurando su correcto registro en la herramienta institucional.
- Coordino la recopilación de artefactos por fase (Análisis, Diseño, Desarrollo, Pruebas, Liberación) para soportar CAES y el cierre de iniciativas.
- Reúno y normalizo reportes de seguridad (SAST/DAST y VoBo sin bloqueantes, críticos o altos) como evidencia previa a liberación.
- Documento entregas a AVL/Monitor (paquetes, bitácoras, ventanas) y aseguro su correcta integración en la evidencia mensual.
- Coordino la capacitación a la Mesa del SAT y la transferencia de conocimiento como parte del proceso de liberación y cierre.
- Alineo el contenido de las carpetas a los requisitos del RFP (estructura, anexos y evidencias), maximizando la aceptación y evitando deducciones.
- Gestiono aclaraciones y correcciones dentro de los plazos de dictamen, asegurando la trazabilidad de los cambios realizados.
- Consolido indicadores (SLA/OLA, TTA/TTR, backlog, porcentaje de liberaciones a tiempo y CAES on-time) en el reporte ejecutivo mensual.
- Coordino la documentación de Toma de Operación (accesos, enlace, conectividad y acta de entrega-recepción) para su integración como evidencia.
- Verifico la consistencia de datos (nombres, folios, fechas y versiones) entre carpetas, CAPA y documentos soporte.
- Coordino la logística de cierre (CAES, plan final, capacitación) para su correcta integración en la carpeta del mes de liberación.
- Documento y estandarizo plantillas para reducir reprocesos y tiempos de dictamen.
- Participo en la elaboración de propuestas relacionadas con los servicios y procesos documentales.
- Reviso y autorizo propuestas que posteriormente estaré a cargo de operar.
- Selecciono y asigno responsables para la ejecución de actividades de entrega documental.
- Gestiono y autorizo la asignación y desasignación de recursos humanos, materiales y financieros para la operación documental.
- Respaldo y autorizo la toma de decisiones de los responsables a mi cargo.
- Reporto información operativa y de avance relacionada con la gestión documental.
- Supervisto las actividades de gestión documental, dirigiendo y corrigiendo cuando es necesario.
- Establezco lineamientos de operación y la estrategia global para la entrega documental.
- Informo de manera periódica y consolidada los resultados a niveles directivos y equipos de trabajo.
- Comunico a los equipos la información relevante para la correcta operación documental.
- Mantengo la relación con el cliente como punto de contacto y escalación en temas de entrega documental.

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
> "Gestiono entre 1 y 3 proyectos con un esfuerzo total que oscila entre más de 5,000 y hasta 10,000 horas. Coordino equipos de entre 10 y 15 participantes y administro a un conjunto de líderes con menor seniority. Asimismo, reporto avances y resultados a PM (integrador), DM y cliente, a nivel de gerencia media."

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
- ISP: Defino el proyecto alineando objetivos, alcance, recursos y equipo.
- PTO: Doy seguimiento al avance y gestiono desviaciones.
- FPT: Aseguro un cierre ordenado con entregables y lecciones aprendidas.
- CHM: Gestiono cambios evaluando impacto e implementación.
- SCM: Controlo versiones y configuraciones, garantizando trazabilidad.

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