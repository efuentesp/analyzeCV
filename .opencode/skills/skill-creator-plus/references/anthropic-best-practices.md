# Mejores Practicas de Anthropic para Skills

Referencia consolidada de los principios de la guia oficial de Anthropic para construir skills efectivos.

---

## 1. Progressive Disclosure (Divulgacion Progresiva)

El principio de diseno central. Funciona como un manual bien organizado:

| Nivel | Contenido | Cuando se carga | Tamano recomendado |
|-------|-----------|-----------------|-------------------|
| **Nivel 1**: Frontmatter YAML | Metadata minima (name + description) | Siempre en el system prompt | ~100 palabras |
| **Nivel 2**: Cuerpo de SKILL.md | Instrucciones completas del orquestador | Cuando el agente determina que el skill es relevante | <500 lineas |
| **Nivel 3**: Archivos vinculados | Steps, references, templates, scripts | Solo cuando el agente los necesita | Sin limite fijo |

### Reglas practicas
- El SKILL.md es un orquestador liviano que carga steps bajo demanda
- Cada step es un archivo autocontenido que se carga solo cuando le toca ejecutarse
- Los archivos de referencia se cargan solo cuando un step los necesita
- Los scripts se ejecutan sin cargarse en la ventana de contexto

---

## 2. Gestion de la Ventana de Contexto

La ventana de contexto es un bien publico compartido entre el system prompt, historial de conversacion, metadata de skills y la solicitud del usuario.

### Principios
- **Solo agregar lo que el agente no sabe**: Cuestionar cada pieza de informacion
- **SKILL.md bajo 500 lineas**: Para rendimiento optimo
- **Dividir contenido extenso** en archivos de referencia separados
- **Mantener referencias a un nivel de profundidad** desde SKILL.md (evitar encadenamiento)
- **Incluir tabla de contenidos** en referencias de mas de 100 lineas

### Ejemplo de concision

**Bueno** (~50 tokens):
```markdown
## Extraer texto de PDF
Usar pdfplumber para extraccion:
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

**Malo** (~150 tokens): Explicar que es un PDF, por que usar pdfplumber, etc.

---

## 3. Grados de Libertad

Ajustar la especificidad segun la fragilidad de la tarea:

### Alta libertad (instrucciones textuales)
- Multiples enfoques son validos
- Las decisiones dependen del contexto
- Usar cuando: conversaciones de descubrimiento, generacion de ideas, analisis

### Libertad media (pseudocodigo o patrones con parametros)
- Existe un patron preferido pero se acepta variacion
- Usar cuando: generacion de documentos, estructuras de datos, templates

### Baja libertad (scripts especificos, sin parametros variables)
- Operaciones fragiles y propensas a errores
- La consistencia es critica
- Usar cuando: validaciones, migraciones, operaciones de archivos

---

## 4. Estilo de Escritura

- Usar **forma imperativa/infinitiva** (verb-first)
- No usar segunda persona ("You should..."), usar instrucciones directas
- Usar lenguaje objetivo e instruccional
- Mantener terminologia consistente
- Evitar informacion que se desactualice con el tiempo

---

## 5. Frontmatter YAML

### Campo `name`
- Maximo 64 caracteres
- Solo minusculas, numeros y guiones (kebab-case)
- Sin XML tags, sin "claude" o "anthropic"
- Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`

### Campo `description`
- Maximo 1024 caracteres
- Debe incluir QUE hace Y CUANDO usarlo
- Incluir frases trigger especificas
- Mencionar tipos de archivo si aplica

---

## 6. Testing e Iteracion

### Tres areas de testing
1. **Tests de triggering**: El skill se carga en el momento correcto (y no cuando no debe)
2. **Tests funcionales**: El skill produce outputs correctos
3. **Comparacion de rendimiento**: El skill mejora resultados vs. baseline

### Senales de iteracion
- **Undertriggering**: Agregar mas detalle y palabras clave al description
- **Overtriggering**: Ser mas especifico en el description
- **Problemas de ejecucion**: Mejorar instrucciones, agregar manejo de errores
