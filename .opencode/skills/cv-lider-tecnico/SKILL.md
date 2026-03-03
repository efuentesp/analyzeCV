---
name: cv-lider-tecnico
description: Analiza CVs de Gerente de Operación y devuelve únicamente un JSON estructurado. No inferir ni agregar información no explícita.
metadata:
  author: raquelizue
  version: "1.0.0"
---

# SAT CV Extractor - Gerente de Operación

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
- No debe utilizar pronombres personales.
- Debe enfocarse en liderazgo técnico, coordinación de equipos y entrega de soluciones.
- No debe incluir certificaciones, cursos ni formación académica.
- No debe iniciar con “Profesional con…”, “Ingeniero con…”, etc.
- No debe inventar información.

## Reglas de alineación con el rol

El resumen debe reflejar capacidades relacionadas con:

- Dirección y coordinación de equipos técnicos  
- Implementación de soluciones tecnológicas  
- Aseguramiento de calidad del software  
- Integración de componentes técnicos  
- Alineación con arquitectura y seguridad  
- Gestión de proyectos  
- Comunicación entre áreas técnicas y no técnicas  

Debe proyectar al perfil como facilitador técnico y estratégico.

## Reglas de estructura obligatorias

- Debe tener una extensión total de dos párrafos con 4 renglones cada uno con un máximo de 140 palabras en total.
- Debe estar redactado en prosa continua.
- Cada párrafo debe ser un bloque narrativo fluido.
- No debe redactarse como lista de funciones o actividades.
- No debe estructurarse como enumeración explícita ni implícita.
- No debe separar ideas en líneas independientes por actividad.
- No debe presentar múltiples oraciones consecutivas iniciadas en infinitivo (ej. "Coordinar", "Supervisar", "Gestionar").
- No debe repetir la misma estructura gramatical en oraciones consecutivas.
- Las responsabilidades deben integrarse dentro de una narrativa ejecutiva, no en formato descriptivo operativo.
- Debe leerse como una introducción ejecutiva del perfil profesional, no como detalle operativo de tareas.

## Criterios de claridad

- Debe ser claro y comprensible para lectores no técnicos.
- Debe sintetizar el perfil profesional resaltando el valor aportado en términos de continuidad de servicios y cumplimiento de procesos.
- Debe proyectar seniority cuando la experiencia lo respalde.

---

# FASE 2 — FILTRADO (SOLO SI rol_propuesto = "Lider Tecnico")

## Criterio de relevancia

Una experiencia es válida solo si contiene evidencia explícita de:

- Dirección o coordinación de equipos técnicos  
- Liderazgo en desarrollo o implementación  
- Supervisión técnica  
- Aseguramiento de calidad del software  
- Gestión de proyectos tecnológicos  
- Integración de soluciones  
- Interacción con áreas no técnicas  
- Toma de decisiones técnicas  
- Alineación con arquitectura o seguridad  
- Uso de metodologías de desarrollo  
- Participación en desarrollo tecnológico  

Si no hay evidencia → OMITIR

No reinterpretar liderazgo administrativo sin componente técnico.

## Regla prioritaria: 5 años acumulados

1. Ordenar experiencias relevantes de la más reciente a la más antigua.  
2. Agregar experiencias completas.  
3. Detener cuando la suma alcance o supere ~5 años.  
4. No recortar experiencias.  
5. No agregar más después de superar el umbral.

Si no hay experiencia relevante:

```json
"experiencia_laboral": []
```

# FASE 2.1 — RESUMEN CONSOLIDADO DE EXPERIENCIA NO SELECCIONADA

Aplica cuando existan experiencias excluidas.

Generar:

- `periodo_resumen_laboral`
- `resumen_laboral`

## Reglas

- No listar experiencias individualmente.
- No incluir actividades técnicas detalladas.
- Explicar responsabilidades de forma general.
- Redacción clara y formal.
- 60–110 palabras.
- No usar primera persona.

Debe iniciar con:

"Durante este período..."  
o  
"En este periodo se desempeñaron funciones como..."

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
     - puesto
     - fecha_inicio
     - fecha_fin
   - Generar exactamente 5 actividades en `actividades_principales`.  
   - Aplicar reglas de redacción de FASE 3.  
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

