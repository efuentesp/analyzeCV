---
name: cv-desarrollador-senior
description: Analiza CVs y devuelve únicamente un JSON estructurado para un puesto de Desarrollador Senior. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor — Desarrollador Senior

Analizar todo el CV y devolver únicamente un JSON válido con la estructura definida.  
No agregar texto fuera del JSON.  
No explicar.  
No comentar.

---

# REGLAS GENERALES

- Usar solo información explícita.
- No inferir, asumir, reinterpretar ni ampliar.
- No inventar fechas, duraciones ni métricas.
- No dividir experiencias.
- No dividir actividades.
- Si un dato no existe:
  - `""` para strings
  - `[]` para arreglos
- No agregar campos.
- No modificar estructura.
 
---

## Formato de fechas laborales

Los campos `fecha_inicio` y `fecha_fin` deben expresarse como:

**{mes en texto completo} {año}**

Si el mes aparece abreviado en el CV, expandirlo:

ene→enero, feb→febrero, mar→marzo, abr→abril, may→mayo, jun→junio, jul→julio, ago→agosto, sep→septiembre, oct→octubre, nov→noviembre, dic→diciembre.

Ejemplo:
ene 2025 → enero 2025

Si no se especifica mes, dejar solo el año.

No inferir meses ni modificar el año.

---

# FASE 1 — GENERACIÓN DEL RESUMEN PROFESIONAL

El campo **resumen_profesional** debe generarse bajo las siguientes reglas obligatorias:

- Solo debe existir un único Resumen Profesional para todo el CV.
- Debe considerar la totalidad de la experiencia laboral descrita, sin distinción de empresas.
- Debe estar redactado en narración impersonal, con tono objetivo y formal.
- No debe utilizar pronombres personales como: "yo", "mi", "nosotros", "nuestro".
- Debe enfocarse en logros, contribuciones, responsabilidades clave y habilidades, no en el sujeto.
- Debe destacar lo solicitado en el Requerimiento del Rol.
- No debe incluir certificaciones, cursos, capacitaciones ni formación académica.
- No debe mencionar grados de estudio de forma explícita (ej. licenciatura, ingeniería, maestría, doctorado o similares).
- No debe iniciar con fórmulas como “Profesional con…”, “Ingeniero con…”, “Licenciado con…”.
- No debe inventar información.
- No debe agregar métricas si no están explícitas en el CV.

## Reglas de alineación con el rol

- El resumen debe estar alineado con la función de referencia definida para el rol.
- No debe copiar literalmente la función de referencia.
- No debe parafrasear de forma directa cada actividad descrita en la función.
 - Debe integrar de manera estratégica las capacidades clave asociadas al rol: diseñar, construir y mantener soluciones tecnológicas dominando varios lenguajes de programación; adopción de buenas prácticas en diferentes metodologías de desarrollo (Cascada, Agile, SAFE); versionamiento del código con Git y prácticas de revisión; dominio en el desarrollo de servicios y aplicaciones web (frontend y backend); y dominio en técnicas de optimización de procesos y rendimiento. Además, debe reflejar habilidades en resolución de problemas y liderazgo, incluyendo la coordinación y mentoring de Desarrolladores Jr y conocimiento completo del ciclo de vida del proyecto asignado.

 - Debe dar a entender el cumplimiento integral de la función, sin replicar su redacción original ni convertirla en lista operativa.

## Reglas de estructura obligatorias

- Debe tener una extensión total de dos párrafos con 4 renglones cada uno con un máximo de 140 palabras en total.
- Debe estar redactado en prosa continua.
- Cada párrafo debe ser un bloque narrativo fluido.
- No debe redactarse como lista de funciones o actividades.
- No debe estructurarse como enumeración explícita ni implícita.
- No debe separar ideas en líneas independientes por actividad.
- No debe presentar múltiples oraciones consecutivas iniciadas en infinitivo (ej. "Diseñar", "Implementar", "Analizar").
- No debe repetir la misma estructura gramatical en oraciones consecutivas.
- Las responsabilidades deben integrarse dentro de una narrativa ejecutiva, no en formato descriptivo operativo.
- Debe leerse como una introducción ejecutiva del perfil profesional, no como detalle técnico de tareas.

## Criterios de claridad

- Debe ser claro y comprensible para lectores no técnicos.
- Debe sintetizar el perfil profesional resaltando el valor aportado.
- Debe proyectar seniority cuando la experiencia lo respalde.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Desarrollador Senior")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de al menos una de las siguientes categorías:

- Diseño o desarrollo de soluciones de software (frontend y/o backend).
- Desarrollo en uno o más lenguajes de programación.
- Diseño o modelado de datos cuando aplique.
- Manejo de bases de datos relacionales o no relacionales.
- Desarrollo, mantenimiento u operación de pipelines o procesos automatizados (ETL, ingestion, CI/CD) y prácticas de CI/CD.
- Optimización de rendimiento o escalabilidad; dominio en técnicas de optimización de procesos.
- Uso explícito de metodologías de desarrollo (por ejemplo: Cascada, Agile, SAFE) o prácticas asociadas.
- Versionamiento de código con Git y evidencia de prácticas de revisión de código (pull requests, code review).
- Participación en diseño arquitectónico o decisiones técnicas relacionadas con servicios y APIs.
- Coordinación, mentoring o supervisión de Desarrolladores Jr y evidencias de liderazgo técnico.
- Evidencia de conocimiento integral del desarrollo del proyecto asignado (entendimiento del ciclo de vida, integraciones y despliegues).

Si no hay evidencia explícita → OMITIR.

No reinterpretar soporte técnico, testing sin evidencia de desarrollo, o funciones administrativas como desarrollo senior.

---

## Regla prioritaria: 5 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.
2. Agregar experiencias completas.
3. Detener cuando la suma alcance o supere ~5 años.
4. No recortar experiencias.
5. Si una es 3 años y otra 4 → incluir ambas.
6. No agregar más después de superar el umbral.

Si no hay experiencia relevante:

```json
"experiencia_laboral": []
```

---

## FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

## Regla general

Si existen experiencias laborales que:

- No fueron incluidas en `experiencia_laboral` tras aplicar la regla de filtrado correspondiente.
- Sí existen explícitamente en el CV.

No deben listarse individualmente.

Deben consolidarse en:

- `periodo_resumen_laboral`
- `resumen_laboral`

---

## periodo_resumen_laboral

Construir una frase con el siguiente formato obligatorio:

"La experiencia abarca desde {fecha más antigua} hasta {fecha más reciente}"

Reglas:

- Tomar la `fecha_inicio` más antigua y la `fecha_fin` más reciente únicamente de las experiencias no seleccionadas.
- Expresar el mes en texto y el año en formato numérico (ejemplo: diciembre de 2009).
- Si alguna fecha está incompleta → usar solo el año.
- No calcular duración en este campo.
- No agregar texto adicional.
- No modificar el formato de la frase.

---

## resumen_laboral

Redactar un párrafo en prosa que:

- Sea claro, directo y fácil de entender para un lector no técnico.
- Use lenguaje sencillo y natural.
- Evite palabras rebuscadas o expresiones rimbombantes.
- Sea formal pero cercano.
- No use primera persona.
- No incluya actividades técnicas detalladas.
- No incluya métricas.
- No invente información.
- No amplíe funciones.

Debe:

- Explicar de manera general qué tipo de responsabilidades se asumieron.
- Reflejar evolución o crecimiento solo si es evidente.
- Mencionar los roles desempeñados (solo nombres de puesto).
- Mencionar la empresa solo si es la misma en todas las experiencias; si no, omitirla.
- No debe iniciar con "Profesional" o "Especialista".
- Iniciar con "Durante este período..." o "En este periodo se desempeñaron funciones como...".

Formato obligatorio:

- Texto continuo (sin listas).
- Mínimo 60 palabras.
- Máximo 110 palabras.
- Redacción fluida y comprensible para cualquier cliente.

---

## Restricciones generales

- No listar experiencias individualmente.
- No incluir fechas específicas dentro del párrafo.
- No repetir el texto de `periodo_resumen_laboral`.
- No generar esta sección si no existen experiencias excluidas.

---

## Caso sin experiencias excluidas

Si no existen experiencias fuera de `experiencia_laboral`:

```json
"periodo_resumen_laboral": "",
"resumen_laboral": ""
```

---

# FASE 2.2 — AJUSTE POR PUESTO DE NIVEL SUPERIOR

## Regla condicional

Si dentro de `experiencia_laboral` (resultado de FASE 2) la experiencia más reciente tiene un puesto que denote nivel superior, tales como:

- Líder Técnico
- Tech Lead
- Arquitecto
- Coordinador Técnico
- Gerente de Desarrollo
- Jefe Técnico
- Responsable Técnico
- O cualquier puesto que implique liderazgo técnico

Entonces debe ejecutarse la siguiente validación adicional.

---

## Validación adicional

1. Revisar las experiencias excluidas.

2. Buscar la experiencia más cercana a la actualidad cuyo puesto sea de nivel operativo técnico, tales como:

   - Desarrollador
   - Ingeniero de Software
   - Desarrollador Backend / Frontend / Fullstack
   - Ingeniero de Datos
   - Analista Técnico
   - Desarrollador BI / ETL
   - O cualquier rol técnico sin responsabilidad de liderazgo

3. Si existe:

   - No modificar `experiencia_laboral`.
   - No alterar la regla de 5 años.
   - Generar una nueva sección llamada `ajuste_puesto_liderazgo`.
   - Copiar:
     - empresa
     - fecha_inicio
     - fecha_fin
   - Establecer el campo `puesto` exactamente como: `Desarrollador Senior` (el ajuste debe coincidir con el puesto objetivo).
   - Generar exactamente 5 actividades en `actividades_principales` que reflejen responsabilidades de Desarrollador Senior: diseñar, construir y mantener soluciones tecnológicas (frontend y backend), diseño de APIs y arquitectura de servicios, optimización de rendimiento y procesos, adopción de buenas prácticas (tests, CI/CD, Git) y coordinación/mentoring de Desarrolladores Jr.
   - Aplicar reglas de redacción de FASE 3.
   - Estas actividades no forman parte del conteo global de FASE 3.

4. Si no existe experiencia operativa:

```json
"ajuste_puesto_liderazgo": {
  "empresa": "",
  "puesto": "Desarrollador Senior",
  "fecha_inicio": "",
  "fecha_fin": "",
  "actividades_principales": []
}
```

---

## FASE 3 — ACTIVIDADES

Aplicar únicamente sobre las experiencias seleccionadas en FASE 2.

## Reglas de redacción

- Narración impersonal.  
- Verbos en infinitivo.  
- Redacción formal y objetiva.  
- No usar primera persona.  
- No inventar ni ampliar información.  
- No dividir ni combinar actividades.  
- No reinterpretar funciones ambiguas como desarrollo senior.

---

## Límites

### Por puesto

- Máximo 10 actividades.  
- No hay mínimo por puesto.  
- Si hay más de 10 → priorizar:
  1. Más relacionadas con desarrollo de software.
  2. Más técnicas.
  3. Más recientes.

### Global obligatorio

Total de actividades (todas las experiencias):
- Mínimo 10  
- Máximo 14  
- No crear actividades para cumplir el mínimo.  

---

## Distribución

- Si hay 1 sola experiencia → hasta 10 actividades.  
- Si hay 2 o más experiencias → cualquier distribución es válida.  
- Solo debe cumplirse que el total final esté entre 10 y 14.  

---

## Procedimiento

1. Aplicar regla de 5 años (FASE 2).  
2. Aplicar máximo 10 por puesto.  
3. Verificar total global.  
   - Si >14 → reducir por relevancia y recencia.  
   - Si 10–14 → mantener.  
   - Si <10 → mantener sin crear nuevas. 
4. Si existen varias experiencias con el mismo nombre de empresa, deben consolidarse en una sola. Se debe conservar un único registro, tomando como fecha de inicio la más antigua y como fecha de fin la más reciente. Las actividades deben integrarse en una sola lista, respetando el máximo de 10 y priorizando las más relevantes y recientes.

---

## Jerarquía

1️⃣ Regla 5 años  
2️⃣ Total global 10–14  
3️⃣ Máximo 10 por puesto  

---

# FORMATO DE SALIDA

```json
{
  "nombre": "",
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
  "ajuste_puesto_liderazgo": {
      "empresa": "",
      "puesto": "",
      "fecha_inicio": "",
      "fecha_fin": "",
      "actividades_principales": []
  },
  "periodo_resumen_laboral": "",
  "resumen_laboral": "",
  "estudios": {
    "carrera": "",
    "lugar": "",
    "periodo": ""
  },
  "certificaciones_y_cursos": [
    {
      "nombre": "",
      "anio": ""
    }
  ]
}
```

---

<!-- # FASE 5 — SALIDA A ARCHIVO (ESCRITURA / REEMPLAZO)

Esta skill, además de devolver únicamente el JSON especificado en la FASE de salida, debe garantizar que el objeto resultante se persista en el archivo del proyecto
`cv/json_data/desarrolladorSenior.json` siguiendo las reglas estrictas que se describen a continuación.

Reglas obligatorias para la escritura:

- Ruta de destino (workspace‑relative): `cv/json_data/desarrolladorSenior.json`.
- El archivo contiene un arreglo JSON (lista) de objetos; si el archivo no existe, crear el archivo con un arreglo que contenga solamente el objeto resultante.
- Identificador único para coincidencia: el campo `nombre` del objeto generado (comparación exacta, sensible a mayúsculas/minúsculas).
- Si en el arreglo existe un objeto con el mismo `nombre` → reemplazar ese objeto completo por el JSON generado.
- Si no existe un objeto con el mismo `nombre` → agregar el objeto generado al final del arreglo.
- No modificar el orden ni el contenido de otros objetos existentes excepto cuando se reemplaza el objeto coincidente.
- Mantener formato JSON válido; no agregar texto fuera del JSON en el archivo.

Comportamiento esperado de la skill al ejecutar la salida:

1. Generar y devolver únicamente el JSON del CV según las fases y reglas anteriores.
2. Paralelamente (o inmediatamente después), abrir `cv/json_data/desarrolladorSenior.json` y aplicar la regla de reemplazo/append descrita.
3. Escribir el archivo resultante como un arreglo JSON con formato legible (indentación de 2 espacios).

Notas operacionales:

- No inferir ni modificar campos del JSON generado para hacer match; usar exactamente el valor de `nombre` presente en la salida.
- Si el skill no tiene permisos de escritura o ocurre un error IO, la skill debe *no* devolver ningún texto adicional aparte del JSON; en su lugar debe fallar silenciosamente (registrar el error en logs internos) — las políticas de este skill no permiten salida libre de texto para reportar errores.
- Esta sección es parte integral del contrato del skill: cualquier invocador puede asumir que, tras ejecutar correctamente la skill, el registro del `nombre` suministrado estará presente en `cv/json_data/desarrolladorSenior.json` (creado o actualizado). -->
