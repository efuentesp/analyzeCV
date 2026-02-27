import os
import json
from docxtpl import DocxTemplate
from pydantic import create_model, ValidationError
from typing import Any, Dict, List


# Programa para rellenar una plantilla .docx usando datos de un JSON.
# No se definen clases manuales; se usa pydantic.create_model para validación ligera.

TEMPLATE_PATH = os.path.join("PLANTILLA-DE-CV.docx")
JSON_PATH = os.path.join("cv", "json_data", "desarrolladorJuniorBI.json")
OUTPUT_DIR = os.path.join("cv", "final_cv")

def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def sanitize_filename(name: str) -> str:
    # Normalizar acentos y eliminar caracteres no ASCII
    import unicodedata
    if not isinstance(name, str):
        name = str(name)
    name = unicodedata.normalize('NFKD', name)
    name = name.encode('ascii', 'ignore').decode('ascii')
    invalid = "\\/:*?\"<>|"
    for ch in invalid:
        name = name.replace(ch, "-")
    # Reemplazar saltos y múltiples espacios por uno solo
    name = " ".join(name.split())
    # Limitar longitud razonable
    return name[:200]


def prepare_context(data: Dict[str, Any]) -> Dict[str, Any]:
    # Normalizar claves posibles del JSON a los nombres esperados por la aplicación.
    def _normalize_keys(d: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(d, dict):
            return d
        # Mapeo de alias comunes -> clave esperada
        aliases = {
            "nombre": ["nombre", "name"],
            "rol_propuesto": ["rol_propuesto", "rol", "role", "rolPropuesto"],
            "resumen_profesional": ["resumen_profesional", "perfil", "profile", "summary"],
            "experiencia_laboral": ["experiencia_laboral", "experiencia", "experience", "work_experience"],
            "resumen_laboral": ["resumen_laboral", "resumen", "resumen_text", "summary_laboral"],
            "periodo_resumen_laboral": ["periodo_resumen_laboral", "periodo_resumen", "periodoResumenLaboral"],
            "estudios": ["estudios", "educacion", "education", "estudio"],
            "certificaciones_y_cursos": ["certificaciones_y_cursos", "certificaciones", "certs", "certificacionesCursos"]
            ,
            "ajuste_puesto_liderazgo": ["ajuste_puesto_liderazgo", "ajuste_puesto", "ajuste", "ajustePuestoLiderazgo"]
        }

        normalized: Dict[str, Any] = dict(d)  
        for target, keys in aliases.items():
            if target in normalized:
                continue
            for k in keys:
                if k in d and d.get(k) is not None:
                    normalized[target] = d.get(k)
                    break

        return normalized

    data = _normalize_keys(data)

    CVModel = create_model(
        "CVModel",
        nombre=(str, ...),
        rol_propuesto=(str, ...),
        resumen_profesional=(str, ...),
        experiencia_laboral=(list, []),
        resumen_laboral=(Any, []),
        periodo_resumen_laboral=(str, ""),
        estudios=(dict, {}),
        certificaciones_y_cursos=(list, []),
        ajuste_puesto_liderazgo=(dict, {}),
    )

    try:
        validated = CVModel(**data)
    except ValidationError as e:
        raise ValueError(f"Validación fallida del JSON: {e}")
    
    context = dict(validated.__dict__)

    # Helper para normalizar strings (evita "None" y None)
    def _norm_str(val: Any) -> str:
        if val is None:
            return ""
        s = str(val).strip()
        if s.lower() == "none":
            return ""
        return s

    # Preparar texto con viñetas para actividades de experiencia
    experiencias = []
    for exp in context.get("experiencia_laboral", []):
        empresa = _norm_str(exp.get("empresa", ""))
        puesto = _norm_str(exp.get("puesto", ""))
        fecha_inicio = _norm_str(exp.get("fecha_inicio", ""))
        fecha_fin = _norm_str(exp.get("fecha_fin", ""))
        # Mantener campo periodo por compatibilidad
        periodo = f"{fecha_inicio} - {fecha_fin}".strip(" -") if (fecha_inicio or fecha_fin) else _norm_str(exp.get("periodo", ""))
        # admitir ambos nombres posibles para actividades
        actividades = exp.get("actividades_principales", []) or exp.get("actividades", [])
        # Normalizar actividades: reemplazar None, "", "None" por un espacio
        actividades_clean = []
        for a in actividades:
            if a is None:
                actividades_clean.append(" ")
                continue
            if isinstance(a, str):
                if a.strip() == "" or a.strip().lower() == "none":
                    actividades_clean.append(" ")
                else:
                    actividades_clean.append(a.strip())
            else:
                actividades_clean.append(str(a))
        
        actividades_text = "\n".join([f"- {a}" for a in actividades_clean])
        experiencias.append({
            "empresa": empresa,
            "puesto": puesto,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "periodo": periodo,
            "actividades_text": actividades_text,
            "actividades": actividades,
        })

    context["experiencia_laboral"] = experiencias

    # Procesar sección 'ajuste_puesto_liderazgo' (siempre se espera un único objeto)
    raw_ajuste = context.get("ajuste_puesto_liderazgo", None)
    ajuste_procesado = None

    # Sólo aceptar dict; si no es dict, ignorar y dejar vacío
    if isinstance(raw_ajuste, dict):
        adj = raw_ajuste
    else:
        adj = None

    if adj is not None:
        empresa = _norm_str(adj.get("empresa", ""))
        puesto = _norm_str(adj.get("puesto", ""))
        fecha_inicio = _norm_str(adj.get("fecha_inicio", ""))
        fecha_fin = _norm_str(adj.get("fecha_fin", ""))
        periodo = f"{fecha_inicio} - {fecha_fin}".strip(" -") if (fecha_inicio or fecha_fin) else _norm_str(adj.get("periodo", ""))
        actividades = adj.get("actividades_principales", []) or adj.get("actividades", [])
        actividades_clean = []
        for a in actividades:
            if a is None:
                actividades_clean.append(" ")
                continue
            if isinstance(a, str):
                if a.strip() == "" or a.strip().lower() == "none":
                    actividades_clean.append(" ")
                else:
                    actividades_clean.append(a.strip())
            else:
                actividades_clean.append(str(a))

        actividades_text = "\n".join([f"- {a}" for a in actividades_clean])
        ajuste_procesado = {
            "empresa": empresa,
            "puesto": puesto,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "periodo": periodo,
            "actividades_text": actividades_text,
            "actividades": actividades_clean,
        }

    # Determinar si el ajuste tiene contenido significativo; guardamos resultado temporalmente
    ajuste_was_meaningful = False
    if ajuste_procesado is not None:
        # Considerar significativo si alguna de las cadenas no está vacía o si hay actividades útiles
        for v in (ajuste_procesado.get("empresa", ""), ajuste_procesado.get("puesto", ""), ajuste_procesado.get("fecha_inicio", ""), ajuste_procesado.get("fecha_fin", ""), ajuste_procesado.get("periodo", "")):
            if isinstance(v, str) and v.strip():
                ajuste_was_meaningful = True
                break
        # comprobar actividades
        if not ajuste_was_meaningful:
            acts = ajuste_procesado.get("actividades", []) or []
            for a in acts:
                if isinstance(a, str) and a.strip() and a.strip() != "":
                    if a.strip() != " ":
                        ajuste_was_meaningful = True
                        break

    # No escribir todavía en context: lo haremos después de normalizar vacíos
    raw_resumen = context.get("resumen_laboral", "")
    periodo_nuevo = _norm_str(context.get("periodo_resumen_laboral", ""))

    if isinstance(raw_resumen, str) and raw_resumen.strip():
        lines = [ln.rstrip() for ln in raw_resumen.splitlines()]
        texto = "\n".join(lines).strip()
        context["resumen_laboral_text"] = texto if texto else " "
        context["resumen_laboral"] = []
    else:
        context["resumen_laboral"] = []
        context["resumen_laboral_text"] = " "
    
    certs = []
    certs_obj = []
    for c in context.get("certificaciones_y_cursos", []):
        if isinstance(c, dict) and "nombre" in c:
            nombre = c["nombre"]
            anio = c.get("anio") or c.get("year")
            display = f"{nombre} ({anio})" if anio else nombre
            certs.append(display)
            certs_obj.append({"nombre": nombre, "anio": anio})
        elif isinstance(c, str):
            certs.append(c)
            certs_obj.append({"nombre": c, "anio": None})

    context["certificaciones_y_cursos"] = certs_obj
    context["certificaciones_y_cursos_display"] = certs
    context["certificaciones_obj"] = certs_obj
    estudios = context.get("estudios", {}) or {}
    carrera_raw = estudios.get("carrera", "")
    # separar líneas y limpiar
    lines = [ln.strip() for ln in carrera_raw.splitlines() if ln.strip()]
    institucion = lines[0] if len(lines) >= 1 else ""
    titulo = lines[1] if len(lines) >= 2 else carrera_raw
    context["estudios_institucion"] = institucion
    context["estudios_titulo"] = titulo
    context["estudios_lugar"] = estudios.get("lugar", "")
    context["estudios_periodo"] = estudios.get("periodo", "")

    # Reemplazar elementos vacíos "" por un espacio, listas vacías [] por [" "],
    # y cadenas literales "None" por un espacio
    def _replace_empty(obj: Any) -> Any:
        # Recorrer estructuras y sustituir únicamente "" y [] (no alterar otros tipos)
        if isinstance(obj, dict):
            return {k: _replace_empty(v) for k, v in obj.items()}
        if isinstance(obj, list):
            if len(obj) == 0:
                return [" "]
            return [_replace_empty(v) for v in obj]
        # Reemplazar None y cadenas vacías por un espacio
        if obj is None:
            return " "
        if isinstance(obj, str) and obj == "":
            return " "
        if isinstance(obj, str) and obj.strip().lower() == "none":
            return " "
        return obj

    context = _replace_empty(context)

    # Después de normalizar vacíos, establecer ajuste_puesto_liderazgo a None si no había contenido
    if not ajuste_was_meaningful:
        context["ajuste_puesto_liderazgo"] = None
    else:
        # Si era significativo, escribir el objeto procesado (ya limpio)
        context["ajuste_puesto_liderazgo"] = ajuste_procesado

    return context


def render_docx(template_path: str, context: Dict[str, Any], output_path: str) -> None:
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Plantilla no encontrada: {template_path}")

    doc = DocxTemplate(template_path)
    doc.render(context)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)

def _generate_for_candidate(template: str, candidate_data: Any) -> None:
    """Prepara contexto para un candidato y genera su CV."""
    try:
        context = prepare_context(candidate_data)
    except ValueError as e:
        print(f"Validación fallida para candidato: {e}")
        return

    nombre = context.get("nombre", "CV")
    safe_name = sanitize_filename(nombre)
    output_file = os.path.join(OUTPUT_DIR, f"{safe_name} - CV_generado.docx")

    try:
        render_docx(template, context, output_file)
    except Exception as e:
        print(f"Error al generar el documento para {nombre}: {e}")
        return

    print(f"Documento generado: {output_file}")


def main(template: str = TEMPLATE_PATH, json_path: str = JSON_PATH) -> None:
    print(f"Usando plantilla: {template}")
    print(f"Leyendo JSON: {json_path}")

    data = load_json(json_path)

    # Si el JSON es una lista, generar un CV por cada elemento
    if isinstance(data, list):
        print(f"Se encontraron {len(data)} candidatos en el JSON. Generando CVs...")
        for idx, candidate in enumerate(data, start=1):
            # Solo procesar objetos tipo dict; omitir entradas atípicas
            display_name = candidate.get('nombre', '<sin nombre>') if isinstance(candidate, dict) else str(candidate)
            print(f"\nProcesando candidato {idx}/{len(data)}: {display_name}")
            if not isinstance(candidate, dict):
                print(f"Entrada {idx} en el JSON no es un objeto; se omite.")
                continue
            _generate_for_candidate(template, candidate)
    elif isinstance(data, dict):
        _generate_for_candidate(template, data)
    else:
        print("Formato JSON no reconocido: se esperaba un objeto o una lista de objetos.")


if __name__ == "__main__":
    # Permite pasar rutas alternativas desde la línea de comandos
    import sys

    tpl = sys.argv[1] if len(sys.argv) > 1 else TEMPLATE_PATH
    js = sys.argv[2] if len(sys.argv) > 2 else JSON_PATH
    main(template=tpl, json_path=js)
