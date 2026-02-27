---
name: cv-desarrollador-senior-BI
description: Analiza CVs y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "4.0.0"
---

# SAT CV Extractor

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
- Debe integrar de manera estratégica las capacidades clave asociadas al rol, demostrando coherencia con responsabilidades como diseño de soluciones de datos, modelado, procesos ETL, aseguramiento de calidad, integración, análisis y liderazgo técnico.
- Debe dar a entender el cumplimiento integral de la función, sin replicar su redacción original ni convertirla en lista operativa.

## Reglas de estructura obligatorias

- Debe tener una extensión total de dos parrafos con 4 renglones cada uno.
- Debe estar redactado en prosa continua.
- Cada párrafo debe ser un bloque narrativo fluido.
- No debe redactarse como lista de funciones o actividades.
- No debe estructurarse como enumeración explícita ni implícita.
- No debe separar ideas en líneas independientes por actividad.
- No debe presentar múltiples oraciones consecutivas iniciadas en infinitivo (ej. "Diseñar", "Implementar", "Analizar").
- No debe repetir la misma estructura gramatical en oraciones consecutivas.
- Las responsabilidades deben integrarse dentro de una narrativa ejecutiva, no en formato descriptivo operativo.
- Debe leerse como una introducción ejecutiva del perfil profesional, no como detalle técnico de tareas.
- Si el contenido puede dividirse fácilmente en actividades independientes sin perder sentido, debe reescribirse en formato narrativo.

## Criterios de claridad

- Debe ser claro y comprensible para lectores no técnicos.
- Debe sintetizar el perfil profesional resaltando el valor aportado.
- Debe proyectar seniority cuando la experiencia lo respalde.agregar métricas si no están explícitas en el CV.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Desarrollador Senior BI")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:

- Diseño o desarrollo de soluciones tecnológicas
- Desarrollo en múltiples lenguajes de programación
- Diseño o modelado de datos
- Manejo de bases de datos relacionales o no relacionales
- Desarrollo o mantenimiento de procesos ETL (Extract, Transform, Load)
- Optimización de procesos
- Uso de metodologías de desarrollo (Cascada, Agile, SAFE)
- Versionamiento de código (Git)
- Coordinación o supervisión de desarrolladores
- Participación activa en desarrollo de proyectos tecnológicos

Si no hay evidencia explícita → OMITIR.

No reinterpretar soporte técnico, testing o funciones administrativas como desarrollo BI.

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

# FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

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
# FASE 2.2 — AJUSTE POR PUESTO DE NIVEL SUPERIOR

## Regla condicional

Si dentro de `experiencia_laboral` (resultado de FASE 2) la experiencia más reciente tiene un puesto que denote nivel superior, tales como:

- Arquitecto de Datos  
- Líder BI  
- Gerente de Desarrollo  
- Coordinador BI  
- Jefe de Desarrollo  
- Tech Lead  
- O cualquier puesto que implique liderazgo o la nomenclatura Sr, SR o Senior.

Entonces debe ejecutarse la siguiente validación adicional.

---

## Validación adicional

1. Revisar las experiencias excluidas.  
2. Buscar la experiencia más cercana a la actualidad cuyo puesto sea de nivel operativo, tales como:
   - Desarrollador BI  
   - Analista BI  
   - Desarrollador ETL  
   - Ingeniero de Datos  
   - O cualquier puesto que no implique liderazgo o que no tenga la nomenclatura Sr, SR o Senior. 

3. Si existe:
   - No modificar `experiencia_laboral`.
   - No alterar la regla de 5 años.
   - No alterar FASE 3.
   - Generar una nueva sección llamada `ajuste_puesto_liderazgo`.
   - Copiar:
     - empresa
     - puesto
     - fecha_inicio
     - fecha_fin
   - Generar exactamente 5 actividades en `actividades_principales`.
   - Aplicar reglas de redacción de FASE 3.
   - No generar más ni menos de 5 actividades.
   - Estas actividades no forman parte del conteo global de FASE 3.

4. Si no existe experiencia operativa:

```json
"ajuste_puesto_liderazgo": {
  "empresa": "",
  "puesto": "",
  "fecha_inicio": "",
  "fecha_fin": "",
  "actividades_principales": []
}
```
# FASE 3 — ACTIVIDADES

Aplicar únicamente sobre las experiencias seleccionadas en FASE 2.

## Reglas de redacción

- Narración impersonal.
- Verbos en infinitivo.
- Redacción formal y objetiva.
- No usar primera persona.
- No inventar ni ampliar información.
- No dividir ni combinar actividades.
- No reinterpretar funciones ambiguas como desarrollo BI.

## Límites

### Por puesto

- Máximo 10 actividades.
- No hay mínimo por puesto.
- Si hay más de 10, priorizar:
  1. Más relacionadas con desarrollo BI.
  2. Más técnicas.
  3. Más recientes.

### Global obligatorio

Total de actividades (todas las experiencias consolidadas):
- Mínimo 10.
- Máximo 14.
- No crear actividades para cumplir el mínimo

## Distribución

- Si hay 1 sola experiencia → hasta 10 actividades.
- Si hay 2 o más experiencias → cualquier distribución es válida.
- Solo debe cumplirse que el total final esté entre 10 y 14.

## Procedimiento (orden obligatorio)

1. Aplicar regla de 5 años (FASE 2).
2. Consolidar experiencias con el mismo `nombre_empresa` (ver regla 4).
3. Aplicar máximo 10 actividades por empresa consolidada.
4. Verificar total global:
   - Si >14 → reducir por relevancia y recencia.
   - Si 10–14 → mantener.
   - Si <10 → mantener sin crear nuevas.

## Consolidación por empresa

Si existen múltiples experiencias con el mismo `nombre_empresa` (coincidencia exacta y sensible a mayúsculas/minúsculas), deben consolidarse en un único registro antes de validar el total global.

La consolidación debe cumplir:

- Conservar la fecha de inicio más antigua.
- Conservar la fecha de fin más reciente.
- Unificar todas las actividades en una sola lista.
- Aplicar el máximo de 10 actividades para esa empresa, priorizando:
  1. Más relacionadas con desarrollo BI.
  2. Más técnicas.
  3. Más recientes.

Después de consolidar, continuar con la validación del total global (10–14).

## Jerarquía

1️⃣ Regla 5 años  
2️⃣ Total global 10–14  
3️⃣ Máximo 10 por puesto  

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
<!-- # FASE 5 — SALIDA A ARCHIVO (ESCRITURA / ACTUALIZACIÓN)

Además de devolver únicamente el JSON generado en la fase de salida, la skill debe persistir el objeto resultante en:

`cv/json_data/desarrolladorSeniorBI.json`

## Reglas de persistencia

- La ruta es relativa al workspace.
- El archivo debe contener un arreglo JSON (lista) de objetos.
- Si el archivo no existe, crearlo con un arreglo que contenga únicamente el objeto generado.
- El campo `nombre` es el identificador único (comparación exacta y sensible a mayúsculas/minúsculas).
- Si ya existe un objeto con el mismo `nombre`, reemplazar únicamente ese objeto.
- Si no existe, agregar el nuevo objeto al final del arreglo.
- No eliminar, modificar ni reordenar otros registros existentes.
- Mantener formato JSON válido con indentación de 2 espacios.
- No agregar texto fuera del JSON dentro del archivo.

## Comportamiento esperado

1. Generar y devolver únicamente el JSON del CV.
2. Actualizar el archivo aplicando la regla de reemplazo o agregado según corresponda.
3. Garantizar que los registros previos permanezcan intactos, excepto el que coincida por `nombre`.

## Restricciones operativas

- No alterar el valor de `nombre` para realizar coincidencias.
- Si ocurre un error de escritura, no devolver mensajes adicionales; la salida debe seguir siendo únicamente el JSON generado. -->
