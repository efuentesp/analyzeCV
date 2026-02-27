---
name: cv-desarrollador-junior-BI
description: description: Analiza CVs y devuelve únicamente un JSON estructurado para el rol de Desarrollador Junior BI.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor — Ingeniero de Datos Junior BI

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
- Debe considerar la totalidad de la experiencia laboral descrita.
- Debe estar redactado en narración impersonal, con tono objetivo y formal.
- No utilizar pronombres personales.
- No incluir certificaciones ni formación académica.
- No mencionar grados académicos explícitamente.
- No iniciar con “Profesional con…”, “Ingeniero con…”, etc.
- No inventar información.
- No agregar métricas no explícitas.

## Alineación con el rol

El resumen debe reflejar experiencia en:

  - Desarrollo de soluciones BI mediante lenguajes de programación.
  - Construcción e implementación de componentes funcionales.
  - Desarrollo, mantenimiento o soporte de procesos ETL.
  - Modelado de datos.
  - Manejo de bases de datos relacionales y no relacionales.
  - Uso de herramientas de BI (como Databricks o Fabric).
  - Participación en soluciones analíticas o de inteligencia de negocio.

Debe proyectar:
  - Perfil junior con base técnica sólida
  - Enfoque en ejecución
  - Participación activa en construcción de soluciones

## Estructura obligatoria

- Dos párrafos de 4 reglones cada uno,
- Máximo de 140 palabras en total.
- Prosa continua.
- No formato de lista.
- No múltiples oraciones consecutivas iniciadas en infinitivo.
- Redacción ejecutiva, no operativa.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Ingeniero de Datos BI Junior")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:

- Desarrollo de soluciones tecnológicas o componentes BI
- Programación orientada al manejo o procesamiento de datos
- Desarrollo o mantenimiento de procesos ETL
- Implementación de soluciones de datos
- Modelado de datos
- Manejo de bases de datos relacionales o no relacionales
- Construcción de estructuras para análisis de información
- Uso de herramientas BI (Databricks, Fabric u otras)
- Participación en proyectos de analítica o BI

Si no hay evidencia explícita → OMITIR.

No reinterpretar:

- Soporte técnico general  
- Testing  
- Funciones administrativas  
- Soporte funcional  

como desarrollo BI.

---

## Regla prioritaria: 2 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.
2. Agregar experiencias completas.
3. Detener cuando la suma alcance o supere ~2 años.
4. No recortar experiencias.
5. No agregar más después de superar el umbral.

Si no hay experiencia relevante:

```json
"experiencia_laboral": []
```

# FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

## Regla general

Si existen experiencias laborales que:

- No fueron incluidas en `experiencia_laboral` tras aplicar la regla de filtrado de FASE 2.
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
- Expresar el mes en texto y el año en formato numérico (ejemplo: diciembre de 2021).
- Si alguna fecha está incompleta → usar solo el año.
- No calcular duración en este campo.
- No agregar texto adicional.
- No modificar el formato de la frase.

---

## resumen_laboral

Redactar un párrafo en prosa que:

- Sea claro y fácil de entender para un lector no técnico.
- Use lenguaje sencillo y natural.
- Sea formal y objetivo.
- No use primera persona.
- No incluya actividades técnicas detalladas.
- No incluya métricas.
- No invente información.
- No amplíe funciones.

Debe:

- Explicar de manera general qué tipo de responsabilidades se asumieron.
- Mencionar los roles desempeñados (solo nombres de puesto).
- Mencionar la empresa solo si es la misma en todas las experiencias; si no, omitirla.
- No iniciar con "Profesional" o "Especialista".
- Iniciar obligatoriamente con:
  - "Durante este período..."  
  o  
  - "En este periodo se desempeñaron funciones como..."

Formato obligatorio:

- Texto continuo (sin listas).
- Mínimo 60 palabras.
- Máximo 110 palabras.
- No incluir fechas específicas dentro del párrafo.
- No repetir el texto de `periodo_resumen_laboral`.

---

## Caso sin experiencias excluidas

Si no existen experiencias fuera de `experiencia_laboral`:

```json
"periodo_resumen_laboral": "",
"resumen_laboral": ""
```

# FASE 3 — ACTIVIDADES

Aplicar únicamente sobre las experiencias seleccionadas en FASE 2.

---

## Reglas de redacción

- Narración impersonal.
- Verbos en infinitivo.
- Redacción formal y objetiva.
- No usar primera persona.
- No inventar ni ampliar información.
- No dividir ni combinar actividades.
- No reinterpretar funciones ambiguas como ingeniería de datos.

---

## Límites

### Por puesto

- Máximo 10 actividades.
- No hay mínimo por puesto.
- Si hay más de 10, priorizar:
  1. Más relacionadas con ingeniería de datos.
  2. Más técnicas.
  3. Más recientes.

### Global obligatorio

Total de actividades (todas las experiencias seleccionadas):
- Mínimo 10.
- Máximo 14.
- No crear actividades para cumplir el mínimo.

---

## Distribución

- Si hay 1 sola experiencia → hasta 10 actividades.
- Si hay 2 o más experiencias → cualquier distribución es válida.
- Solo debe cumplirse que el total final esté entre 10 y 14.

---

## Procedimiento (orden obligatorio)

1. Aplicar regla de 2 años (FASE 2).
2. Aplicar máximo 10 actividades por puesto.
3. Verificar total global.
   - Si >14 → reducir por relevancia y recencia.
   - Si 10–14 → mantener.
   - Si <10 → mantener sin crear nuevas.

---

## Jerarquía

1️⃣ Regla 2 años  
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