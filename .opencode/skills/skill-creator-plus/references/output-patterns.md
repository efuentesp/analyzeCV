# Patrones de Output para Skills

Referencia de patrones para producir output consistente en los skills generados.

---

## 1. Patron de Templates

### Template Estricto (para estructuras obligatorias)

Usar cuando el formato de salida debe ser exacto y repetible. El skill generado incluye un template con la estructura completa y variables placeholder.

```markdown
---
stepsCompleted: []
inputDocuments: []
---

# {{project_name}} - Titulo del Documento

## Seccion 1: Nombre Fijo

{{contenido_seccion_1}}

## Seccion 2: Nombre Fijo

{{contenido_seccion_2}}

<!-- Repetir para cada elemento en lista (N = 1, 2, 3...) -->

### Elemento {{N}}: {{titulo_elemento_N}}

{{descripcion_elemento_N}}

<!-- Fin repeticion -->
```

**Cuando usar**: Documentos con estructura normada (PRDs, briefs, reportes de validacion).

### Template Semilla (para documentos que crecen incrementalmente)

Usar cuando el documento se construye paso a paso durante el flujo de trabajo. El template define solo el encabezado y el frontmatter de estado.

```markdown
---
stepsCompleted: []
inputDocuments: []
---

# Titulo del Documento: {{project_name}}

**Autor:** {{user_name}}
**Fecha:** {{date}}

---

<!-- El contenido se anadira secuencialmente a traves de los pasos del flujo -->
```

**Cuando usar**: La mayoria de skills de flujo de trabajo. Es el patron recomendado por defecto.

---

## 2. Patron de Variables

### Variables de config.yaml (llaves simples con prefijo)
Resueltas automaticamente desde la configuracion del proyecto:
- `{project_name}` - nombre del proyecto
- `{user_name}` - nombre del usuario
- `{output_folder}` - carpeta de salida
- `{communication_language}` - idioma de comunicacion
- `{document_output_language}` - idioma del documento
- `{project-root}` - raiz del proyecto

### Variables de template (doble llave)
Reemplazadas durante la creacion del documento:
- `{{project_name}}` - nombre del proyecto en el documento
- `{{user_name}}` - autor del documento
- `{{date}}` - fecha de creacion
- `{{contenido_seccion}}` - contenido generado colaborativamente

### Variables de frontmatter de estado
Gestionadas automaticamente por el flujo de trabajo:
- `stepsCompleted: []` - array de nombres de archivos de steps completados
- `inputDocuments: []` - array de rutas de documentos de entrada
- `lastStep: ''` - ultimo step completado (opcional, derivable de stepsCompleted)

---

## 3. Patron de Ejemplos (Input/Output)

Incluir pares de ejemplo para que el agente entienda el estilo y nivel de detalle esperado.

### Formato
```markdown
## Ejemplo

**Entrada del usuario:**
"Necesito un sistema de autenticacion con OAuth2 y 2FA"

**Salida esperada:**
### RF-001: Autenticacion OAuth2
El sistema DEBE permitir autenticacion mediante proveedores OAuth2 (Google, GitHub, Microsoft).

**Criterios de aceptacion:**
- Dado un usuario no autenticado, cuando selecciona un proveedor OAuth2, entonces se redirige al flujo de autorizacion del proveedor
- Dado un flujo de autorizacion exitoso, cuando el proveedor retorna el token, entonces el sistema crea una sesion activa
```

**Cuando usar**: Steps que generan contenido con formato especifico (requisitos funcionales, historias de usuario, criterios de aceptacion).

---

## 4. Patron de Construccion Append-Only

El documento se construye solo por adicion. Cada step agrega contenido al final del documento sin modificar secciones anteriores.

### Reglas
- NUNCA modificar contenido de secciones ya completadas
- SIEMPRE agregar nuevo contenido al final del documento
- Si se necesita corregir contenido anterior, el usuario debe solicitarlo explicitamente
- El frontmatter de estado (`stepsCompleted`) se actualiza en cada step

### Flujo
```
Step 2: Agrega "## Seccion A" al documento
Step 3: Agrega "## Seccion B" despues de Seccion A
Step 4: Agrega "## Seccion C" despues de Seccion B
...
Step N: Agrega "## Seccion Final" y marca el flujo como completado
```
