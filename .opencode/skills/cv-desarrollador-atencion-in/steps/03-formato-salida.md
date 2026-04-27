---
title: Formato de salida JSON
order: 3
---

Salida final estricta (solo JSON):

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
  "herramientas": [
    {
      "nombre": "",
    }
  ],
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

Regla: el skill solo debe devolver este JSON; no debe incluir texto adicional ni comentarios.
