---
title: "step-05 - Ajuste por liderazgo"
step: 5
stepsCompleted: []
---


LEE COMPLETAMENTE este archivo antes de ejecutar acciones. Seguir la secuencia del paso y confirmar para continuar.

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

# File References
nextStepFile: './step-06-actividades.md'
