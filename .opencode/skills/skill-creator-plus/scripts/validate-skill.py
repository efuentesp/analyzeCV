#!/usr/bin/env python3
"""
validate-skill.py — Validador integral de skills de tipo workflow para OpenCode.

Ejecuta 14 validaciones estructurales y de contenido sobre un directorio de skill,
verificando conformidad con los patrones arquitectonicos documentados.

Uso:
    python validate-skill.py <directorio-del-skill>

Ejemplo:
    python validate-skill.py .opencode/skills/mi-skill

Codigos de salida:
    0 — Todas las validaciones pasaron
    1 — Una o mas validaciones fallaron
    2 — Error de uso (argumentos incorrectos)
"""

import sys
import os
import re
from pathlib import Path

# --- Constantes ---

ALLOWED_SKILLMD_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
ALLOWED_STEP_KEYS = {
    "name", "description", "nextStepFile", "outputFile",
    "templateFile", "dataFile", "referenceFile",
    "templateFiles", "dataFiles", "referenceFiles",
}
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_SKILLMD_LINES = 500
HYPHEN_CASE_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


# --- Utilidades ---

def parse_frontmatter(text):
    """Extraer y parsear frontmatter YAML de un texto markdown.

    Retorna (dict, error_string). Si hay error, dict es None.
    No depende de PyYAML — parseo simplificado de pares clave:valor
    para evitar dependencias externas.
    """
    if not text.startswith("---"):
        return None, "No se encontro frontmatter YAML (debe iniciar con ---)"

    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None, "Formato de frontmatter invalido (falta cierre ---)"

    raw = match.group(1)
    result = {}
    current_key = None

    for line in raw.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Detectar clave: valor
        kv = re.match(r"^([a-zA-Z_][a-zA-Z0-9_-]*)\s*:\s*(.*)", line)
        if kv:
            key = kv.group(1).strip()
            value = kv.group(2).strip()
            # Quitar comillas envolventes
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            result[key] = value
            current_key = key
        elif line.startswith("  ") and current_key:
            # Linea de continuacion (listas, multilínea) — ignorar para validacion basica
            pass

    return result, None


def count_lines(filepath):
    """Contar lineas de un archivo."""
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


# --- Validaciones ---

class ValidationResult:
    """Resultado de una validacion individual."""

    def __init__(self, rule_id, description, passed, detail=""):
        self.rule_id = rule_id
        self.description = description
        self.passed = passed
        self.detail = detail

    def __str__(self):
        status = "PASS" if self.passed else "FAIL"
        msg = f"  [{status}] V{self.rule_id:02d}: {self.description}"
        if self.detail:
            msg += f"\n         -> {self.detail}"
        return msg


def validate_skill(skill_path_str):
    """Ejecutar todas las validaciones sobre un directorio de skill.

    Retorna una lista de ValidationResult.
    """
    skill_path = Path(skill_path_str).resolve()
    results = []

    # ------------------------------------------------------------------
    # V01: SKILL.md existe
    # ------------------------------------------------------------------
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        results.append(ValidationResult(1, "SKILL.md existe", False, "Archivo no encontrado"))
        # Sin SKILL.md no podemos continuar varias validaciones
        for i in range(2, 15):
            results.append(ValidationResult(i, "(omitida — SKILL.md no existe)", False, "Dependencia V01"))
        return results
    results.append(ValidationResult(1, "SKILL.md existe", True))

    # Leer contenido
    skill_content = skill_md.read_text(encoding="utf-8")

    # ------------------------------------------------------------------
    # V02: Frontmatter YAML valido en SKILL.md
    # ------------------------------------------------------------------
    fm, fm_error = parse_frontmatter(skill_content)
    if fm is None:
        results.append(ValidationResult(2, "Frontmatter YAML valido", False, fm_error))
        # Sin frontmatter valido, omitir V03-V06, V12
        results.append(ValidationResult(3, "Campo 'name' presente y valido", False, "Dependencia V02"))
        results.append(ValidationResult(4, "Campo 'description' presente y valido", False, "Dependencia V02"))
        results.append(ValidationResult(5, "Solo propiedades permitidas en frontmatter", False, "Dependencia V02"))
        results.append(ValidationResult(6, "Longitudes dentro de limites", False, "Dependencia V02"))
        fm = {}  # Continuar con validaciones no dependientes
    else:
        results.append(ValidationResult(2, "Frontmatter YAML valido", True))

        # ------------------------------------------------------------------
        # V03: Campo 'name' presente y valido (hyphen-case)
        # ------------------------------------------------------------------
        name = fm.get("name", "")
        if not name:
            results.append(ValidationResult(3, "Campo 'name' presente y valido", False, "Falta el campo 'name'"))
        elif not HYPHEN_CASE_PATTERN.match(name):
            results.append(ValidationResult(3, "Campo 'name' presente y valido", False,
                                            f"'{name}' no cumple hyphen-case (solo minusculas, digitos, guiones; sin iniciar/terminar con guion)"))
        else:
            results.append(ValidationResult(3, "Campo 'name' presente y valido", True, f"name='{name}'"))

        # ------------------------------------------------------------------
        # V04: Campo 'description' presente y valido
        # ------------------------------------------------------------------
        desc = fm.get("description", "")
        if not desc:
            results.append(ValidationResult(4, "Campo 'description' presente y valido", False, "Falta el campo 'description'"))
        elif "<" in desc or ">" in desc:
            results.append(ValidationResult(4, "Campo 'description' presente y valido", False,
                                            "La descripcion no puede contener < o >"))
        else:
            results.append(ValidationResult(4, "Campo 'description' presente y valido", True))

        # ------------------------------------------------------------------
        # V05: Solo propiedades permitidas en frontmatter de SKILL.md
        # ------------------------------------------------------------------
        unexpected = set(fm.keys()) - ALLOWED_SKILLMD_KEYS
        if unexpected:
            results.append(ValidationResult(5, "Solo propiedades permitidas en frontmatter", False,
                                            f"Claves no permitidas: {', '.join(sorted(unexpected))}. "
                                            f"Permitidas: {', '.join(sorted(ALLOWED_SKILLMD_KEYS))}"))
        else:
            results.append(ValidationResult(5, "Solo propiedades permitidas en frontmatter", True))

        # ------------------------------------------------------------------
        # V06: Longitudes dentro de limites
        # ------------------------------------------------------------------
        length_issues = []
        if name and len(name) > MAX_NAME_LENGTH:
            length_issues.append(f"name tiene {len(name)} caracteres (max {MAX_NAME_LENGTH})")
        if desc and len(desc) > MAX_DESCRIPTION_LENGTH:
            length_issues.append(f"description tiene {len(desc)} caracteres (max {MAX_DESCRIPTION_LENGTH})")
        if length_issues:
            results.append(ValidationResult(6, "Longitudes dentro de limites", False, "; ".join(length_issues)))
        else:
            results.append(ValidationResult(6, "Longitudes dentro de limites", True))

    # ------------------------------------------------------------------
    # V07: SKILL.md < 500 lineas (best practice Anthropic)
    # ------------------------------------------------------------------
    line_count = count_lines(skill_md)
    if line_count > MAX_SKILLMD_LINES:
        results.append(ValidationResult(7, f"SKILL.md < {MAX_SKILLMD_LINES} lineas", False,
                                        f"Tiene {line_count} lineas"))
    else:
        results.append(ValidationResult(7, f"SKILL.md < {MAX_SKILLMD_LINES} lineas", True,
                                        f"{line_count} lineas"))

    # ------------------------------------------------------------------
    # V08: Directorio steps/ existe
    # ------------------------------------------------------------------
    steps_dir = skill_path / "steps"
    if not steps_dir.is_dir():
        results.append(ValidationResult(8, "Directorio steps/ existe", False, "No se encontro el directorio"))
        # Sin steps, omitir V09-V11, V13-V14
        for vid, vdesc in [(9, "step-01-init.md existe"), (10, "Ultimo step sin nextStepFile"),
                           (11, "Cada nextStepFile referenciado existe"),
                           (13, "Templates referenciados existen"),
                           (14, "Frontmatter valido en cada step")]:
            results.append(ValidationResult(vid, vdesc, False, "Dependencia V08"))
        # V12 no depende de steps
    else:
        results.append(ValidationResult(8, "Directorio steps/ existe", True))

        # Listar archivos de step
        step_files = sorted([f for f in steps_dir.iterdir() if f.suffix == ".md"])

        # ------------------------------------------------------------------
        # V09: step-01-init.md existe
        # ------------------------------------------------------------------
        init_step = steps_dir / "step-01-init.md"
        if not init_step.exists():
            results.append(ValidationResult(9, "step-01-init.md existe", False,
                                            "No se encontro steps/step-01-init.md"))
        else:
            results.append(ValidationResult(9, "step-01-init.md existe", True))

        # ------------------------------------------------------------------
        # Parsear frontmatter de todos los steps para V10, V11, V13, V14
        # ------------------------------------------------------------------
        step_data = {}  # filename -> (frontmatter_dict, error)
        for sf in step_files:
            content = sf.read_text(encoding="utf-8")
            sfm, sfe = parse_frontmatter(content)
            step_data[sf.name] = (sfm, sfe)

        # ------------------------------------------------------------------
        # V10: Ultimo step no tiene nextStepFile
        # ------------------------------------------------------------------
        # Identificar steps que parecen ser el ultimo (nombre contiene "complete" o "final",
        # o simplemente el de mayor numero sin nextStepFile)
        steps_with_next = []
        steps_without_next = []
        for sname, (sfm, sfe) in step_data.items():
            if sfm and sfm.get("nextStepFile"):
                steps_with_next.append(sname)
            else:
                steps_without_next.append(sname)

        # El ultimo step deberia ser el de mayor numero de secuencia
        if step_files:
            last_step = step_files[-1]
            last_fm = step_data.get(last_step.name, (None, None))[0]
            if last_fm and last_fm.get("nextStepFile"):
                results.append(ValidationResult(10, "Ultimo step sin nextStepFile", False,
                                                f"'{last_step.name}' es el ultimo step pero tiene nextStepFile='{last_fm['nextStepFile']}'"))
            else:
                results.append(ValidationResult(10, "Ultimo step sin nextStepFile", True,
                                                f"Ultimo step: {last_step.name}"))
        else:
            results.append(ValidationResult(10, "Ultimo step sin nextStepFile", False, "No hay archivos de step"))

        # ------------------------------------------------------------------
        # V11: Cada nextStepFile referenciado existe
        # ------------------------------------------------------------------
        missing_next = []
        for sname, (sfm, sfe) in step_data.items():
            if sfm and sfm.get("nextStepFile"):
                next_ref = sfm["nextStepFile"]
                # Resolver ruta relativa (puede ser ./steps/X o solo X)
                next_path = _resolve_resource_path(skill_path, steps_dir, next_ref)
                if not next_path.exists():
                    missing_next.append(f"{sname} -> {next_ref}")
        if missing_next:
            results.append(ValidationResult(11, "Cada nextStepFile referenciado existe", False,
                                            f"No encontrados: {'; '.join(missing_next)}"))
        else:
            results.append(ValidationResult(11, "Cada nextStepFile referenciado existe", True))

        # ------------------------------------------------------------------
        # V13: Templates referenciados en steps existen
        # ------------------------------------------------------------------
        missing_resources = []
        resource_keys = ["templateFile", "templateFiles", "dataFile", "dataFiles",
                         "referenceFile", "referenceFiles"]
        for sname, (sfm, sfe) in step_data.items():
            if not sfm:
                continue
            for rk in resource_keys:
                val = sfm.get(rk, "")
                if not val:
                    continue
                # Puede ser un valor unico o lista separada por comas
                refs = [v.strip() for v in val.split(",") if v.strip()]
                for ref in refs:
                    ref_path = _resolve_resource_path(skill_path, steps_dir, ref)
                    if not ref_path.exists():
                        missing_resources.append(f"{sname}: {rk}='{ref}'")
        if missing_resources:
            results.append(ValidationResult(13, "Recursos referenciados existen", False,
                                            f"No encontrados: {'; '.join(missing_resources)}"))
        else:
            results.append(ValidationResult(13, "Recursos referenciados existen", True))

        # ------------------------------------------------------------------
        # V14: Frontmatter valido en cada step
        # ------------------------------------------------------------------
        invalid_steps = []
        for sname, (sfm, sfe) in step_data.items():
            if sfe:
                invalid_steps.append(f"{sname}: {sfe}")
            elif sfm is None:
                invalid_steps.append(f"{sname}: sin frontmatter")
            else:
                # Verificar que tiene al menos 'name' y 'description'
                if "name" not in sfm:
                    invalid_steps.append(f"{sname}: falta 'name'")
                if "description" not in sfm:
                    invalid_steps.append(f"{sname}: falta 'description'")
        if invalid_steps:
            results.append(ValidationResult(14, "Frontmatter valido en cada step", False,
                                            "; ".join(invalid_steps)))
        else:
            results.append(ValidationResult(14, "Frontmatter valido en cada step", True))

    # ------------------------------------------------------------------
    # V12: Nombre del directorio coincide con 'name' del frontmatter
    # ------------------------------------------------------------------
    if fm and fm.get("name"):
        dir_name = skill_path.name
        fm_name = fm["name"]
        if dir_name != fm_name:
            results.append(ValidationResult(12, "Nombre de directorio = name del frontmatter", False,
                                            f"Directorio='{dir_name}', name='{fm_name}'"))
        else:
            results.append(ValidationResult(12, "Nombre de directorio = name del frontmatter", True))
    else:
        results.append(ValidationResult(12, "Nombre de directorio = name del frontmatter", False,
                                        "No se pudo verificar (falta name en frontmatter)"))

    # Ordenar por rule_id
    results.sort(key=lambda r: r.rule_id)
    return results


def _resolve_resource_path(skill_root, context_dir, ref):
    """Resolver una referencia de recurso a una ruta absoluta.

    Maneja referencias como:
      - ./step-02.md            (relativa al context_dir)
      - ../templates/foo.md     (relativa al context_dir, sube un nivel)
      - templates/foo.md        (relativa al skill root)
      - step-02.md              (relativa al context_dir)
    """
    ref = ref.strip().strip("'\"")
    if ref.startswith("./") or ref.startswith("../"):
        # Rutas relativas explicitas: resolver desde context_dir
        return (context_dir / ref).resolve()
    # Si contiene separador de directorio, resolver desde skill_root
    if "/" in ref:
        return (skill_root / ref).resolve()
    # Sin separador, resolver desde context_dir
    return (context_dir / ref).resolve()


# --- Punto de entrada ---

def main():
    if len(sys.argv) != 2:
        print("Uso: python validate-skill.py <directorio-del-skill>")
        print()
        print("Ejemplo:")
        print("  python validate-skill.py .opencode/skills/mi-skill")
        sys.exit(2)

    skill_dir = sys.argv[1]
    if not os.path.isdir(skill_dir):
        print(f"Error: '{skill_dir}' no es un directorio valido.")
        sys.exit(2)

    print(f"Validando skill en: {Path(skill_dir).resolve()}")
    print("=" * 60)

    results = validate_skill(skill_dir)

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)
    total = len(results)

    for r in results:
        print(r)

    print()
    print("=" * 60)
    print(f"Resultado: {passed}/{total} validaciones pasaron, {failed} fallaron.")

    if failed == 0:
        print("El skill es valido y cumple con la arquitectura de workflow.")
        sys.exit(0)
    else:
        print("Corregir los errores indicados y ejecutar nuevamente.")
        sys.exit(1)


if __name__ == "__main__":
    main()
