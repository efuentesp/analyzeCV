# Patrones de Workflow para Skills

Referencia de patrones de flujo de trabajo utilizados en skills.

---

## 1. Flujo Secuencial Simple

El patron mas comun. Los pasos se ejecutan en orden fijo, uno tras otro.

```
step-01-init → step-02 → step-03 → ... → step-NN-complete
```

### Cuando usar
- El flujo tiene un orden natural y logico
- Cada paso depende de la informacion del paso anterior
- No hay ramificaciones ni saltos condicionales

### Ejemplo
El skill `create-product-brief` sigue este patron: Init → Vision → Usuarios → Metricas → Alcance → Complete.

---

## 2. Flujo Secuencial con Continuacion

Extension del flujo secuencial que permite retomar un flujo interrumpido.

```
step-01-init ──→ step-02 → step-03 → ... → step-NN-complete
     │
     └──(si existe documento previo)──→ step-01b-continue ──→ step-{siguiente}
```

### Cuando usar
- Flujos largos que pueden interrumpirse por limites de contexto
- Siempre recomendado cuando el flujo tiene 4+ pasos

### Implementacion
- `step-01-init` verifica si existe documento con `stepsCompleted` no vacio
- Si existe, redirige a `step-01b-continue`
- `step-01b-continue` lee el ultimo step completado y determina el siguiente

---

## 3. Flujo Multi-Modal

Un SKILL.md que enruta a diferentes secuencias de steps segun el modo seleccionado.

```
SKILL.md ──→ Determinar modo
                │
                ├──(Modo A)──→ steps-a/step-01-init → ... → step-NN-complete
                ├──(Modo B)──→ steps-b/step-01-init → ... → step-NN-complete
                └──(Modo C)──→ steps-c/step-01-init → ... → step-NN-complete
```

### Cuando usar
- Un mismo skill tiene multiples flujos de trabajo distintos
- Los flujos comparten el mismo dominio pero difieren en proposito

### Implementacion
- Cada modo tiene su propio directorio de steps: `steps-a/`, `steps-b/`, `steps-c/`
- El SKILL.md incluye una seccion `DETERMINACION DE MODO` que detecta o pregunta el modo
- Las rutas de cada modo se almacenan en el frontmatter del SKILL.md

### Ejemplo
El skill `prd` es tri-modal: Crear (`steps-c/`), Validar (`steps-v/`), Editar (`steps-e/`).

---

## 4. Flujo con Loop de Validacion

Un paso que se repite hasta que la validacion es exitosa.

```
step-07-implement → step-08-validate ──→ (errores?) ──→ corregir → re-validar
                                          │
                                          └──(sin errores)──→ step-09-complete
```

### Cuando usar
- Pasos que producen artefactos verificables (codigo, documentos estructurados)
- Cuando la calidad del output es critica

### Implementacion
- El step de validacion ejecuta verificaciones
- Si hay errores, los lista y solicita correccion
- Despues de corregir, re-ejecuta la validacion
- Solo avanza cuando todas las validaciones pasan

---

## 5. Flujo con Datos de Clasificacion

Un step que carga datos CSV para clasificar o adaptar el flujo.

```
step-02-discovery ──→ Cargar datos CSV
                      │
                      ├── Clasificar input del usuario contra datos
                      ├── Adaptar preguntas segun clasificacion
                      └── Continuar con contexto enriquecido
```

### Cuando usar
- El skill necesita adaptarse segun el dominio o tipo de proyecto
- Hay categorias predefinidas con comportamientos diferenciados

### Implementacion
- Los datos CSV se almacenan en `data/`
- Se referencian en el frontmatter del step: `dataFile: '../data/nombre.csv'`
- El step carga el CSV y lo usa para clasificacion
- Degradacion elegante: si no se puede cargar, continuar con defaults

### Ejemplo
El skill `prd` usa `domain-complexity.csv` y `project-types.csv` para adaptar el flujo segun el tipo de proyecto y dominio.

---

## 6. Patron de Checklist de Completacion

El ultimo step incluye una checklist de verificacion final.

```markdown
## Lista de Verificacion de Completacion

- [ ] Documento tiene todas las secciones requeridas
- [ ] Frontmatter actualizado con todos los pasos completados
- [ ] Sin secciones con contenido placeholder
- [ ] Formato y estructura consistentes
- [ ] Revisado y aprobado por el usuario
```

### Cuando usar
- Siempre en el step final (`step-NN-complete.md`)
- Proporciona una verificacion sistematica antes de cerrar el flujo
