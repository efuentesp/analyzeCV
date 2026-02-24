---
name: cv-tester
description: Analiza CVs y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "3.1.0"
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

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Tester")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:
- Planeación o ejecución de pruebas
- Pruebas funcionales, integrales, regresión o UAT
- Matrices de prueba / RDP
- Verificación de requerimientos
- Identificación o gestión de defectos
- Datos de prueba
- Criterios de salida

Si no hay evidencia explícita → OMITIR.

No reinterpretar soporte, análisis o desarrollo como testing.

---

## Regla prioritaria: 2 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.
2. Agregar experiencias completas.
3. Detener cuando la suma alcance o supere ~2 años.
4. No recortar experiencias.
5. Si una es 1 año y otra 3 → incluir ambas.
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

Si dentro de `experiencia_laboral` (resultado de FASE 2) la experiencia más reciente tiene un puesto que denote nivel superior a tester, tales como:

- Líder de Pruebas
- QA Manager
- Coordinador de QA
- Líder de Calidad
- Jefe de QA
- O cualquier puesto que implique liderazgo o supervisión

Entonces debe ejecutarse la siguiente validación adicional.

---

## Validación adicional

1. Revisar las experiencias excluidas.
2. Buscar la experiencia más cercana a la actualidad cuyo puesto sea de nivel operativo, tales como:
   - Tester
   - Analista de Pruebas
   - Ingeniero de Pruebas
   - QA Analyst
   - O cualquier puesto que no implique liderazgo.

3. Si existe:
   - No modificar `experiencia_laboral`.
   - No alterar la regla de 2 años.
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
   - Generar:

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
- No reinterpretar funciones ambiguas como testing.

## Límites

### Por puesto
- Máximo 10 actividades.
- No hay mínimo por puesto.
- Si hay más de 10 → priorizar:
  1. Más relacionadas con testing.
  2. Más concretas.
  3. Más recientes.

### Global obligatorio
Total de actividades (todas las experiencias):
- Mínimo 10
- Máximo 14
- No crear actividades para cumplir el mínimo.

## Distribución
- Si hay 1 sola experiencia → hasta 10 actividades.
- Si hay 2 o más experiencias → cualquier distribución es válida.
- Solo debe cumplirse que el total final esté entre 10 y 14.

## Procedimiento
1. Aplicar regla de 2 años (FASE 2).
2. Aplicar máximo 10 por puesto.
3. Verificar total global.
   - Si >14 → reducir por relevancia y recencia.
   - Si 10–14 → mantener.
   - Si <10 → mantener sin crear nuevas.

## Jerarquía
1️⃣ Regla 2 años  
2️⃣ Total global 10–14  
3️⃣ Máximo 10 por puesto  

---

# FASE 4 — RESUMEN PROFESIONAL

Generar únicamente si existe experiencia relevante seleccionada.

Si `experiencia_laboral` está vacío → devolver `""`.

## Alineación obligatoria

Debe estar directamente relacionado con la función Tester:

- Planeación y ejecución de pruebas
- Validación contra requerimientos funcionales
- Uso de matriz o RDP
- Identificación o gestión de defectos
- Validación de calidad del software

Si no existe evidencia explícita → devolver `""`.

## Estructura obligatoria

- Exactamente 2 párrafos
- Cada párrafo de 4 renglones.
- Texto continuo (sin listas)
- Redacción formal e impersonal
- No listar tecnologías
- No incluir certificaciones
- No copiar textualmente la función de referencia

---

# FUNCIÓN DE REFERENCIA (Tester)

Supervisar el cumplimiento de requerimientos funcionales y validar la calidad del producto mediante la planeación y ejecución de pruebas usando una matriz RDP.

Usar únicamente como guía conceptual.
No copiar textualmente.

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

