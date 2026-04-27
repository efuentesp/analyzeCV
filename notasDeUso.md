# Notas de uso

## Objetivo

Este documento describe el flujo para:

- convertir un CV fuente a `.txt`
- generar el `.json` del perfil usando la skill correspondiente
- convertir el `.json` a CV final
- aplicar el checklist al CV generado

## 1. Preparar el CV de entrada

1. Descarga el CV que vas a procesar.
2. Copia el archivo dentro de `cv/templates_input`.
3. Identifica el tipo de archivo:
   - si el CV es `.docx` o `.doc`, usa `convert_to_txt.py`
   - si el CV es `.pdf`, usa `convert_pdf_txt.py`

## 2. Convertir el CV a TXT

### Si el CV es Word (`.docx` o `.doc`)

Ejecuta:

```bash
python convert_to_txt.py
```

Este programa toma los archivos de `cv/templates_input` y genera el `.txt` en `cv/parsed`.

### Si el CV es PDF (`.pdf`)

Ejecuta:

```bash
python convert_pdf_txt.py
```

Este programa toma los PDF de `cv/templates_input` y genera el `.txt` en `cv/parsed`.

## 3. Generar el JSON del perfil

Una vez que el CV ya existe en `cv/parsed`, ejecuta un prompt como este, cambiando solo el archivo y la skill segun el perfil:

```text
lee el siguiente archivo @cv\parsed\HRG2.HORUS RAMSES GARCIA SAN MIGUEL 09_2025.txt y de ser necesario haz mas de una lectura en caso de que se trunque, despues usa la skill de cv-administrador-proyectos para obtener la informacion que necesites y construir el json, la informacion personal, los cursos, certificados y el no de cedula los obtendras unicamente del archivo @cv\templates_input\certificaciones_cursos.txt, lee cuidadosamente la instruccion del consolidado de actividades laborales y sigue al pie de la letra todas las instrucciones
```

Consideraciones importantes para este paso:

- cambia unicamente la skill segun el perfil que estes procesando
- el archivo `cv/templates_input/certificaciones_cursos.txt` es la unica fuente para informacion personal, cursos, certificados y numero de cedula
- si el archivo en `cv/parsed` se trunca, hay que releerlo las veces necesarias
- se debe respetar exactamente la instruccion del consolidado de actividades laborales

## 4. Ajustar resumenes y reemplazo de siglas

Cuando termine el prompt anterior, ejecuta otro prompt para trabajar las secciones `resumen_profesional`, `experiencia_laboral` y `resumen_laboral` sobre el .json generado.

Usa una instruccion como esta:

```text
en las secciones resumen_profesional, experiencia_laboral y resumen_laboral, busca todos los acronimos o siglas y cambialas por la informacion definida en el archivo @cv\templates_input\acronimos_siglas.txt de la siguiente manera: si encuentras las siglas QA, reemplazalo por el texto Aseguramiento de la Calidad (QA) segun el archivo, de la seccion de cursos y certificaciones no cambies nada
```

Reglas de este paso:

- solo se modifican `resumen_profesional`, `experiencia_laboral` y `resumen_laboral`
- no se cambia nada en la seccion de cursos y certificaciones
- todas las siglas o acronimos deben expandirse usando exclusivamente `cv/templates_input/acronimos_siglas.txt`

## 5. Sustituir herramientas tecnologicas

Despues, ejecuta otro prompt para sustituir herramientas tecnicas dentro de las mismas secciones.

Usa una instruccion como esta:

```text
dentro de las mismas secciones, identifica las herramientas tecnologicas mencionadas en el archivo @cv\templates_input\herramientas_perfil.txt y sustituyelas segun corresponda. Por ejemplo, si encuentras "SQL", reemplazalo por "SQL (Lenguaje para gestion y consulta de bases de datos relacionales)". Utiliza unicamente la informacion contenida en dicho archivo para realizar las sustituciones.
```

Reglas de este paso:

- solo se trabaja sobre `resumen_profesional`, `experiencia_laboral` y `resumen_laboral`
- las sustituciones deben salir unicamente de `cv/templates_input/herramientas_perfil.txt`
- no se debe inventar descripcion adicional

## 6. Guardar el JSON generado

El resultado debe guardarse como archivo `.json` dentro de `cv/json_data`.

Ejemplo:

- `cv/json_data/administradorProyectos.json`
- `cv/json_data/analistaJunior.json`

Regla especial para perfiles:

- si estas transformando CV del mismo perfil, en el mismo JSON debes guardar todos los cv que proceses

Antes de seguir:

1. revisa manualmente el JSON generado
2. si detectas errores o ajustes necesarios, corrigelos antes de continuar

## 7. Generar el CV final desde el JSON

Cuando el JSON este correcto, usa `main.py` para convertir cada objeto del JSON en un archivo final.

Antes de ejecutarlo, cambia el nombre del JSON a procesar en la constante `JSON_PATH` de `main.py`.

Actualmente, la ruta se define en `main.py`.

Ejecuta:

```bash
python main.py
```

Salida esperada:

- los CV generados quedaran en `cv/final_cv`

## 8. Convertir el CV generado a TXT para checklist

Para aplicar el checklist sobre el CV recien generado:

1. toma el archivo generado en `cv/final_cv`
2. copialo a `cv/templates_input`
3. conviertelo a `.txt` con `convert_to_txt.py`

Ejecuta:

```bash
python convert_to_txt.py
```

El `.txt` resultante quedara en `cv/parsed`.

Si hubo ajustes manuales al CV, aplica este paso sobre la version final corregida.

## 9. Ejecutar validacion del checklist

Despues ejecuta un prompt como este, cambiando el nombre del archivo y el checklist segun el perfil:

```text
lee el archivo @cv\parsed\Rosain Castillo Eng - CV_generado.txt y valida que su contenido cumpla correctamente con cada uno de los puntos definidos en el archivo @checklist\checkAdministradorProyectos.json. Si el contenido cumple con algun criterio, devuelveme el mismo json con el atributo "resultado" establecido en "OK", en caso contrario ponle un "NO OK".
```

Reglas de este paso:

- debes devolver el mismo checklist en formato JSON
- cada criterio debe quedar con `resultado: "OK"` o `resultado: "NO OK"`
- el checklist usado debe corresponder al perfil procesado

## 10. Generar el checklist final en Excel

Cuando ya tengas listo el archivo `check.json`, usa `main_checklist.py` para generar el checklist final de la persona.

Antes de ejecutarlo:

- cambia el nombre del checklist JSON que se va a usar en `main_checklist.py`
- cambia tambien la plantilla Excel segun el perfil, si aplica
- se generará en la raiz del proyecto un archivo llamado output.xlsx, abrelo, y guarda los cambios con el nombre correspondientes como checkListAnalista-Rocio.

Ejecuta:

```bash
python main_checklist.py
```

## 11. Paso extra: revision final, firma y consolidacion de PDF

Una vez generados el CV y el checklist, los colaboradores del proyecto revisan a profundidad el contenido del CV.

En este paso:

1. revisan manualmente el contenido completo del CV
2. si consideran necesario hacer modificaciones, las realizan a mano
3. generan un `.pdf` con el CV final firmado

Cuando ya tengas varios PDF finales firmados y quieras unirlos:

1. coloca todos los PDF en una misma carpeta
2. ejecuta `create_pdf.py` indicando la ruta de esa carpeta

Ejemplo basico:

```bash
python create_pdf.py "ruta\donde\estan\los\cv\pdf"
```

Si quieres indicar una ruta de salida especifica para el archivo consolidado, usa `-o`.

Ejemplo con salida personalizada:

```bash
python create_pdf.py "ruta\donde\estan\los\cv\pdf" -o "ruta\donde\guardar\pdf_unido.pdf"
```

El consolidado ahora puede incluir automaticamente una plantilla al inicio y aplicar su pie de pagina en cada pagina integrada.

Comportamiento predeterminado:

- si dentro de la carpeta existe un archivo llamado `plantilla.pdf`, se agrega al inicio del PDF consolidado
- se toma la primera pagina de `plantilla.pdf` y se usa su franja inferior como pie de pagina para cada pagina integrada

Si quieres indicar otra plantilla distinta, usa `--plantilla`.

Ejemplo:

```bash
python create_pdf.py "ruta\donde\estan\los\cv\pdf" -o "ruta\donde\guardar\pdf_unido.pdf" --plantilla "ruta\a\plantilla.pdf"
```

Si necesitas ajustar que tanto de la parte inferior de la plantilla se considera como pie, usa `--proporcion-pie`.

Ejemplo:

```bash
python create_pdf.py "ruta\donde\estan\los\cv\pdf" --plantilla "ruta\a\plantilla.pdf" --proporcion-pie 0.18
```

Comportamiento del programa:

- si usas `-o`, el archivo final se guarda en la ruta indicada
- si no usas `-o`, el archivo se genera en la misma carpeta de los PDF de origen con el nombre `pdf_unido.pdf`
- si hay plantilla, sus paginas se agregan primero y ademas se usa su pie de pagina sobre cada pagina de los PDF unidos

## Resumen rapido del flujo

1. Descargar CV y copiarlo a `cv/templates_input`.
2. Convertir a TXT con `convert_to_txt.py` o `convert_pdf_txt.py`.
3. Leer el TXT de `cv/parsed` y generar el JSON con la skill correcta.
4. Ajustar siglas con `cv/templates_input/acronimos_siglas.txt`.
5. Ajustar herramientas con `cv/templates_input/herramientas_perfil.txt`.
6. Guardar y revisar el JSON en `cv/json_data`.
7. Ejecutar `python main.py` para generar el CV final en `cv/final_cv`.
8. Convertir el CV generado nuevamente a TXT.
9. Aplicar el checklist usando el JSON del perfil correspondiente.
10. Ejecutar `python main_checklist.py` para generar el checklist final.
11. Como paso extra, revisar manualmente el CV, hacer ajustes si aplica, generar PDF firmado y consolidar PDF con `create_pdf.py` si es necesario.

## Archivos de apoyo importantes

- `cv/templates_input/certificaciones_cursos.txt`
- `cv/templates_input/acronimos_siglas.txt`
- `cv/templates_input/herramientas_perfil.txt`
- `cv/parsed`
- `cv/json_data`
- `cv/final_cv`
- `checklist`
- `create_pdf.py`

## Observaciones

- solo debes cambiar la skill segun el perfil que estes procesando
- en `main.py` debes cambiar el nombre del JSON que se va a procesar
- en `main_checklist.py` debes cambiar el nombre del checklist segun el perfil
- para unir varios PDF finales firmados, todos deben estar dentro de una misma carpeta antes de ejecutar `create_pdf.py`
- antes de correr `main.py` y `main_checklist.py`, valida que los nombres de archivo y rutas sean correctos
