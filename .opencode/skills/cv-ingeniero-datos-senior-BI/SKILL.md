---
name: cv-ingeniero-datos-senior-BI
description: Analiza CVs de Ingeniero de Datos Senior (BI) y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor - Ingeniero de Datos Senior (BI)

Analizar todo el CV y devolver únicamente un JSON válido con la estructura definida sin agregar texto fuera del JSON y sin comentar o explicar líneas.

---

# REGLAS GENERALES

- Usar solo información explícita.
- No inferir, asumir, reinterpretar ni ampliar información.
- No inventar fechas, duraciones ni métricas.
- No dividir experiencias.
- No dividir actividades.
- Si un dato no existe:
  - `""` para strings
  - `[]` para arreglos
- No agregar campos.
- No modificar estructura.
- **Debe redactarse todo estrictamente en primera persona.**

- Los campos `fecha_inicio` y `fecha_fin` deben expresarse como: 
**{día en número} {mes en texto completo} {año}**
- Ejemplo de formato final:  15 marzo 2024

## Normalización de meses

Si el mes aparece abreviado en el CV, expandirlo:
ene→enero, feb→febrero, mar→marzo, abr→abril, may→mayo, jun→junio, jul→julio, ago→agosto, sep→septiembre, oct→octubre, nov→noviembre, dic→diciembre.

Ejemplo:  
ene 2025 → enero 2025

## Regla cuando no se especifica el mes

Si el CV **solo indica el año**:

- Para `fecha_inicio` usar **enero**.
- Para `fecha_fin` usar **diciembre**.

Ejemplo:  
2021 →  
fecha_inicio: **2 enero 2021** *(primer día laborable disponible entre el 1 y el 4)*  
fecha_fin: **31 diciembre 2021**

## Regla para `fecha_inicio`

Si el CV **no especifica el día**, asignar un día **entre el 1 y el 4 del mes**, asegurando que sea **día laborable (lunes a viernes)**.

Reglas:
- Seleccionar el primer día laborable disponible entre el 1 y el 4.
- No modificar el mes ni el año indicados en el CV.

Ejemplo:  
marzo 2022 → **1 marzo 2022** *(si es laborable)*

## Regla para `fecha_fin`

Si el CV **no especifica el día**, asignar **siempre el último día del mes correspondiente**.

Ejemplos:

marzo 2024 → 31 marzo 2024  
abril 2023 → 30 abril 2023  
febrero 2025 → 28 febrero 2025

No inferir ni modificar el **año** indicado en el CV.

# REGLA DE SELECCIÓN DE ESTUDIOS

En el campo `estudios` se debe registrar **únicamente el grado de nivel licenciatura o equivalente**.

Reglas:
- Seleccionar únicamente estudios cuyo nivel sea **Licenciatura, Ingeniería o equivalente universitario**.
- No incluir **posgrados** como Maestrías, MBA, Doctorados, Especialidades o diplomados.
- Si el CV contiene licenciatura y posgrado: Registrar **solo la licenciatura**.

---

# FASE 1 — GENERACIÓN DEL RESUMEN PROFESIONAL

El campo **resumen_profesional** debe generarse bajo las siguientes reglas obligatorias:

# Frase inicial obligatoria

El resumen **debe iniciar obligatoriamente con una paráfrasis muy ligera** (variación aproximada de 5 palabras) de la siguiente redacción base:

"Al menos 5 años en el análisis de grandes volúmenes de datos y desarrollo de soluciones de Inteligencia de Negocio."

Reglas para la paráfrasis:
- La estructura general debe mantenerse.
- Solo se permite una **variación ligera de vocabulario (aprox. 5 palabras)**.
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
- Debe integrar de manera estratégica las capacidades clave asociadas al rol, demostrando coherencia con responsabilidades como diseño de soluciones de datos, modelado, procesos ETL, aseguramiento de calidad, integración, análisis y liderazgo técnico.

El resumen **no debe**:
- Incluir certificaciones, cursos ni formación académica.
- Inventar información.
- Redactarse como lista de funciones o actividades.
- Estructurarse como enumeración explícita o implícita.
- Separar ideas en líneas independientes por actividad.
- Repetir la misma estructura gramatical en oraciones consecutivas.

## Criterios de claridad

El resumen debe:
- Ser claro y comprensible para lectores no técnicos.
- Sintetizar el perfil resaltando el valor aportado en términos de continuidad de servicios y cumplimiento de procesos.
- Proyectar **seniority** cuando la experiencia lo respalde.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Ingeniero de Datos Senior BI")

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

No reinterpretar soporte técnico, testing o administración de sistemas como ingeniería de datos. 

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

---

# FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

## Regla general

Si existen experiencias laborales que:
- No fueron incluidas en `experiencia_laboral` tras aplicar la regla de filtrado de FASE 2.
- Sí existen explícitamente en el CV.

No deben listarse individualmente.
Deben consolidarse en:

- `periodo_resumen_laboral`
- `resumen_laboral`

## periodo_resumen_laboral

Construir una frase con el siguiente formato obligatorio:

"La experiencia abarca desde {fecha más antigua} hasta {fecha más reciente}"

Reglas:
- Usar las reglas de formato de fechas definidas en esta guía para determinar las fechas a usar.
- Tomar la `fecha_inicio` más antigua y la `fecha_fin` más reciente únicamente de las experiencias no seleccionadas.
- Expresar el mes en texto y el año y el día en formato numérico (ejemplo: 01 diciembre de 2021).
- No calcular duración en este campo.
- No agregar texto adicional.
- No modificar el formato de la frase.

## resumen_laboral

Redactar un párrafo en prosa que:
- Sea claro y fácil de entender para un lector no técnico.
- Use lenguaje sencillo y natural.
- Sea formal y objetivo.
- Usar primera persona.
- No incluya actividades técnicas detalladas o métricas.

Debe:
- Explicar de manera general qué tipo de responsabilidades se asumieron.
- Mencionar los roles desempeñados (solo nombres de puesto).
- Omitir nombres de empresas.
- No iniciar con "Profesional" o "Especialista".
- Iniciar obligatoriamente con:
  - "Durante este período..."  o  "En este periodo se desempeñaron funciones como..."

Formato obligatorio:
- Texto continuo (sin listas) con una extensión de **60 a 110 palabras**.
- No incluir fechas específicas dentro del párrafo.
- No repetir el texto de `periodo_resumen_laboral`.

## Caso sin experiencias excluidas

Si no existen experiencias fuera de `experiencia_laboral`:

```json
"periodo_resumen_laboral": "",
"resumen_laboral": ""
```

# REGLA ESPECIAL — PARÁFRASIS INICIAL DE LA PRIMERA EXPERIENCIA

Antes de listar cualquier actividad dentro de `actividades_principales` de la **primera experiencia laboral**, se debe agregar una **paráfrasis muy ligera** de la siguiente redacción base:

"Diseño, construyo, optimizo y mantengo infraestructuras y soluciones tecnológicas que recolectan, almacenan, procesan y permiten acceder a grandes volúmenes de datos de manera eficiente, segura y escalable.
Cuento con habilidades en el diseño e implementación de procesos ETL/ELT para el procesamiento de grandes volúmenes de información, así como en la definición, construcción y mantenimiento de estructuras de almacenamiento que aseguran la eficiencia de las soluciones de Inteligencia de Negocio. Además, optimizo la carga, el procesamiento y la consulta de grandes volúmenes de datos."

## Reglas de la paráfrasis
- Debe ser una **paráfrasis ligera** con un cambio aproximado de **15 palabras como máximo**.
- Debe **mantener el mismo significado general**.
- Debe **redactarse en primera persona**.
- No debe agregar información que no esté implícita en la redacción base.
- Debe colocarse **como la primera actividad dentro de `actividades_principales` de la primera experiencia laboral**.
- Esta redacción **debe aparecer antes de cualquier otra actividad**.

---

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