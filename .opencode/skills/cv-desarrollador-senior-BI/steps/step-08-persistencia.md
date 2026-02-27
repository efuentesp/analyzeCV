---
title: "step-08 - Persistencia"
step: 8
stepsCompleted: []
---


LEE COMPLETAMENTE este archivo antes de ejecutar acciones. Seguir la secuencia del paso y confirmar para continuar.

# FASE 5 — SALIDA A ARCHIVO (ESCRITURA / ACTUALIZACIÓN)

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
- Si ocurre un error de escritura, no devolver mensajes adicionales; la salida debe seguir siendo únicamente el JSON generado.


# File References
nextStepFile: './step-09-complete.md'
