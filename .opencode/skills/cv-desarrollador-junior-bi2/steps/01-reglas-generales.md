---
title: Reglas Generales
order: 1
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

Si el mes aparece abreviado en el CV, expandirlo: ene→enero, feb→febrero, mar→marzo, abr→abril, may→mayo, jun→junio, jul→julio, ago→agosto, sep→septiembre, oct→octubre, nov→noviembre, dic→diciembre.

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

En el campo `estudios` se debe registrar **únicamente el grado de nivel licenciatura, ingeniería o equivalente**. No se deben incluir posgrados como maestrías, MBA, doctorados, especialidades o diplomados.

---
