# Anatomia Completa de un Skill de Flujo de Trabajo

Referencia de la estructura completa de un skill que sigue la arquitectura de micro-archivos.

---

## 1. Estructura de Directorios

```
nombre-del-skill/
├── SKILL.md                    # OBLIGATORIO: Orquestador principal (~60 lineas)
├── steps/                      # OBLIGATORIO: Micro-archivos de pasos
│   ├── step-01-init.md         #   Inicializacion del flujo
│   ├── step-01b-continue.md    #   Continuacion de flujo existente
│   ├── step-02-<nombre>.md     #   Primer paso de contenido
│   ├── step-03-<nombre>.md     #   Siguientes pasos...
│   └── step-NN-complete.md     #   Completacion del flujo
├── templates/                  # RECOMENDADO: Plantillas de documentos de salida
│   └── <nombre>-template.md    #   Template semilla o completo
├── references/                 # OPCIONAL: Documentacion de referencia
│   └── <nombre>.md             #   Guias, patrones, criterios
├── data/                       # OPCIONAL: Datos de clasificacion
│   └── <nombre>.csv            #   Datos tabulares para adaptacion
└── scripts/                    # OPCIONAL: Codigo ejecutable
    └── <nombre>.py             #   Scripts de validacion, generacion, etc.
```

---

## 2. SKILL.md - El Orquestador

El SKILL.md es el punto de entrada del skill. Debe ser **liviano** (maximo ~60-80 lineas) y seguir esta estructura:

```markdown
---
name: nombre-del-skill
description: Descripcion que incluye QUE hace y CUANDO usarlo. Incluir frases trigger.
---

# Titulo del Flujo de Trabajo

**Objetivo:** [Descripcion del objetivo del flujo]

**Tu Rol:** Ademas de tu nombre, communication_style y persona, tambien eres [ROL ESPECIFICO]
colaborando con [TIPO DE USUARIO]. Esta es una asociacion, no una relacion cliente-proveedor.

---

## ARQUITECTURA DEL FLUJO DE TRABAJO

### Principios Fundamentales
1. **Diseno de Micro-archivos** - Cada paso es un archivo autocontenido
2. **Carga Just-In-Time** - Solo se carga el paso actual
3. **Cumplimiento Secuencial** - Sin saltos ni optimizaciones
4. **Seguimiento de Estado** - Mediante stepsCompleted en frontmatter
5. **Construccion Solo por Adicion** - El documento crece sin modificar secciones anteriores

### Reglas de Procesamiento de Pasos
1. LEE COMPLETAMENTE cada archivo de paso antes de ejecutar
2. SIGUE LA SECUENCIA sin saltar ni reordenar
3. ESPERA LA ENTRADA del usuario antes de generar contenido
4. VERIFICA CONTINUACION - Solo procede cuando el usuario confirma con C
5. GUARDA ESTADO actualizando frontmatter del documento
6. CARGA SIGUIENTE paso solo despues de completar el actual

### Reglas Criticas (SIN EXCEPCIONES)
- NUNCA cargues multiples archivos de paso simultaneamente
- SIEMPRE lee el archivo de paso completo antes de la ejecucion
- NUNCA saltes pasos u optimices la secuencia
- SIEMPRE actualiza el frontmatter de los archivos de salida
- SIEMPRE sigue las instrucciones exactas en el archivo de paso
- SIEMPRE detente y espera la entrada del usuario antes de continuar
- NUNCA crees listas mentales de tareas pendientes de pasos futuros

---

## SECUENCIA DE INICIALIZACION

### 1. Carga de Configuracion
Cargar {project-root}/.agents/core/config.yaml y resolver variables:
- project_name, user_name, output_folder
- communication_language, document_output_language

### 2. Ejecucion del Primer Paso
Cargar, leer completo y ejecutar: ./steps/step-01-init.md
```

---

## 3. Templates - Documentos de Salida

### Campos obligatorios de frontmatter
```yaml
---
stepsCompleted: []      # Array de steps completados
inputDocuments: []      # Array de documentos de entrada
---
```

### Campos opcionales de frontmatter
```yaml
---
skillName: ''           # Nombre del skill (si aplica)
workflowType: ''        # Tipo de flujo (si es multi-modal)
date: ''                # Fecha de creacion
author: ''              # Autor
---
```

### Patron de template semilla (recomendado)
Solo define encabezado y metadatos. El contenido se agrega paso a paso durante el flujo.

### Patron de template completo
Define toda la estructura del documento final con variables placeholder. Usar cuando la estructura es fija y predecible.

---

## 4. References - Documentacion de Apoyo

### Cuando crear un archivo de referencia
- Cuando el contenido excede lo que cabe en un step sin romper el limite de contexto
- Para guias, criterios de calidad, patrones que se consultan bajo demanda
- Para documentacion de dominio que no todos los steps necesitan

### Formato recomendado
- Titulo H1 como nombre de la referencia
- Secciones H2 para cada tema
- Ejemplos concretos con bloques de codigo
- Tabla de contenidos si excede 100 lineas
- Sin frontmatter YAML (no son documentos de flujo)

---

## 5. Data - Datos de Clasificacion

### Cuando usar archivos de datos
- El skill necesita adaptar su comportamiento segun categorias predefinidas
- Hay datos tabulares que informan decisiones del flujo

### Formato recomendado: CSV
- Primera fila como encabezados
- Separador de campos: coma
- Separador interno (listas dentro de un campo): punto y coma (;)
- Incluir una fila "general" o "default" como fallback

---

## 6. Scripts - Codigo Ejecutable

### Cuando usar scripts
- Operaciones que requieren baja libertad (validaciones exactas, generacion de archivos)
- Tareas repetitivas que se benefician de automatizacion
- Procesamiento que el agente no puede hacer de forma confiable solo con instrucciones

### Buenas practicas
- Incluir `#!/usr/bin/env python3` o shebang apropiado
- Documentar uso con `--help` o docstring
- Manejar errores con mensajes claros
- Salida con indicadores visuales (PASS/FAIL/WARN)
- Independientes: sin dependencias externas mas alla de la libreria estandar
