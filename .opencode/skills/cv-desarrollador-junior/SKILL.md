---
name: cv-desarrollador-junior
description: Analiza CVs y devuelve únicamente un JSON estructurado para un puesto de Desarrollador Junior. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor — Desarrollador Junior

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

# FASE 1 — GENERACIÓN DEL RESUMEN PROFESIONAL

El campo **resumen_profesional** debe generarse bajo las siguientes reglas obligatorias:

- Solo debe existir un único Resumen Profesional para todo el CV.
- Debe considerar la totalidad de la experiencia laboral descrita, sin distinción de empresas.
- Debe estar redactado en narración impersonal, con tono objetivo y formal.
- No debe utilizar pronombres personales como: "yo", "mi", "nosotros", "nuestro".
- Debe enfocarse en habilidades básicas, aprendizajes, contribuciones y responsabilidades descriptas en el CV.
- No debe incluir certificaciones, cursos, capacitaciones ni formación académica.
- No debe mencionar grados de estudio de forma explícita.
- No debe inventar información.
- No debe agregar métricas si no están explícitas en el CV.

## Reglas de alineación con el rol

- El resumen debe estar alineado con la función de referencia definida para el rol.
- No debe copiar literalmente la función de referencia.
- Debe integrar de manera coherente capacidades relevantes para un perfil junior: fundamentos de desarrollo, aprendizaje rápido, participación en proyectos bajo supervisión, y exposición a buenas prácticas (control de versiones, testing básico, uso de frameworks relevantes).

## Reglas de estructura obligatorias

- Debe tener una extensión de hasta dos párrafos, preferiblemente uno.
- Debe estar redactado en prosa continua.
- No debe redactarse como lista de funciones o actividades.
- No debe estructurarse como enumeración explícita ni implícita.
- No debe usar primera persona.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Desarrollador Junior")

## Criterio de relevancia

Una experiencia es válida si contiene evidencia explícita de al menos una de las siguientes categorías:

- Participación en desarrollo o mantenimiento de software.
- Experiencia con uno o más lenguajes de programación.
- Uso básico de control de versiones (Git).
- Contribución a tareas de implementación, testing o fixes bajo supervisión.
- Manejo o uso de bases de datos a nivel de consultas o integración básica.
- Participación en proyectos con metodologías ágiles o en equipos de desarrollo.

Si no hay evidencia explícita → OMITIR.

No reinterpretar tareas administrativas o de soporte sin evidencia de desarrollo.

---

## Regla prioritaria: 2 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.
2. Agregar experiencias completas.
3. Detener cuando la suma alcance o supere ~2 años.
4. No recortar experiencias.
5. Si no se alcanza el umbral, incluir todas las experiencias relevantes.

Si no hay experiencia relevante:

```json
"experiencia_laboral": []
```

---

## FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

Las reglas de consolidación son equivalentes a las de la skill base: generar `periodo_resumen_laboral` y `resumen_laboral` si existen experiencias excluidas.

---

## FASE 3 — ACTIVIDADES

Aplicar únicamente sobre las experiencias seleccionadas en FASE 2.

## Reglas de redacción

- Narración impersonal.
- Verbos en infinitivo.
- No usar primera persona.
- No inventar ni ampliar información.

## Límites

- Máximo 8 actividades por puesto.
- Total global recomendado: 6–12 actividades.
- No crear actividades para cumplir números si no se justifican en el CV.

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

# FASE 5 — SALIDA A ARCHIVO (ESCRITURA / REEMPLAZO)

Esta skill, además de devolver únicamente el JSON especificado en la FASE de salida, debe garantizar que el objeto resultante se persista en el archivo del proyecto
`cv/json_data/desarrolladorJunior.json` siguiendo las reglas descritas a continuación.

Reglas obligatorias para la escritura:

- Ruta de destino (workspace‑relative): `cv/json_data/desarrolladorJunior.json`.
- El archivo contiene un arreglo JSON (lista) de objetos; si el archivo no existe, crear el archivo con un arreglo que contenga solamente el objeto resultante.
- Identificador único para coincidencia: el campo `nombre` del objeto generado (comparación exacta, sensible a mayúsculas/minúsculas).
- Si en el arreglo existe un objeto con el mismo `nombre` → reemplazar ese objeto completo por el JSON generado.
- Si no existe un objeto con el mismo `nombre` → agregar el objeto generado al final del arreglo.
- No modificar el orden ni el contenido de otros objetos existentes excepto cuando se reemplaza el objeto coincidente.
- Mantener formato JSON válido; no agregar texto fuera del JSON en el archivo.

Comportamiento esperado de la skill al ejecutar la salida:

1. Generar y devolver únicamente el JSON del CV según las fases y reglas anteriores.
2. Abrir `cv/json_data/desarrolladorJunior.json` y aplicar la regla de reemplazo/append descrita.
3. Escribir el archivo resultante como un arreglo JSON con formato legible (indentación de 2 espacios).

Notas operacionales:

- No inferir ni modificar campos del JSON generado para hacer match; usar exactamente el valor de `nombre` presente en la salida.
- Si el skill no tiene permisos de escritura o ocurre un error IO, la skill debe *no* devolver ningún texto adicional aparte del JSON; en su lugar debe fallar silenciosamente (registrar el error en logs internos).
