from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from pathlib import Path
import tempfile
import subprocess
import os
import traceback
import ctypes
from ctypes import wintypes


def iter_block_items(parent):
    """
    Itera párrafos y tablas en el orden real del documento.
    """
    for child in parent.element.body:
        if child.tag.endswith('p'):
            yield Paragraph(child, parent)
        elif child.tag.endswith('tbl'):
            yield Table(child, parent)


INPUT_DIR = Path("cv/templates_input")
OUTPUT_DIR = Path("cv/parsed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_short_path(path: Path) -> str | None:
    GetShortPathNameW = ctypes.windll.kernel32.GetShortPathNameW
    GetShortPathNameW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD]
    GetShortPathNameW.restype = wintypes.DWORD
    buf = ctypes.create_unicode_buffer(260)
    res = GetShortPathNameW(str(path), buf, 260)
    if res == 0:
        return None
    return buf.value


def convert_doc_to_docx(doc_path: Path) -> Path:
    """
    Convierte un .doc (binario) a .docx usando COM de Word (Windows) si está disponible,
    o usando LibreOffice (`soffice --headless --convert-to docx`) como alternativa.
    Devuelve la ruta del archivo .docx generado.
    Lanza RuntimeError si no puede convertir.
    """
    # Normalizar y comprobar el archivo
    p = Path(doc_path).resolve()
    print(f"DEBUG: ruta resuelta: {p}")
    print(f"DEBUG: existe: {p.exists()}, longitud: {len(str(p))}")
    short = get_short_path(p)
    print(f"DEBUG: ruta corta (8.3): {short}")

    # Intentar con pywin32 (requiere MS Word instalado)
    try:
        import win32com.client  # type: ignore

        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        tried_paths = [str(p)]
        if short:
            tried_paths.append(short)

        doc = None
        for path_to_try in tried_paths:
            try:
                doc = word.Documents.Open(path_to_try)
                print(f"DEBUG: Word abrió: {path_to_try}")
                break
            except Exception:
                print(f"DEBUG: fallo Word al abrir: {path_to_try}")
                traceback.print_exc()

        if doc is None:
            # no se pudo abrir con COM
            try:
                word.Quit()
            except Exception:
                pass
            raise RuntimeError("Word COM no pudo abrir el archivo con ninguna ruta probada")

        # Guardar como .docx en un archivo temporal para evitar sobrescribir
        tmp_dir = tempfile.mkdtemp()
        out_path = Path(tmp_dir) / (p.stem + ".docx")
        # FileFormat=16 normalmente corresponde a wdFormatDocumentDefault (docx)
        doc.SaveAs(str(out_path), FileFormat=16)
        doc.Close(False)
        try:
            word.Quit()
        except Exception:
            pass
        return out_path
    except Exception as e:
        # Mostrar el error real de la conversión por COM para depuración y luego intentar con LibreOffice
        print("DEBUG: fallo conversión por COM (pywin32/MS Word):")
        traceback.print_exc()

        # Intentar con LibreOffice / soffice
        try:
            tmp_dir = tempfile.mkdtemp()
            cmd = [
                "soffice",
                "--headless",
                "--convert-to",
                "docx",
                "--outdir",
                str(tmp_dir),
                str(p),
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out_path = Path(tmp_dir) / (p.stem + ".docx")
            if out_path.exists():
                return out_path
            raise RuntimeError("LibreOffice no produjo el .docx esperado")
        except Exception as e2:
            print("DEBUG: fallo conversión con LibreOffice:")
            traceback.print_exc()
            raise RuntimeError(
                "No se pudo convertir .doc a .docx: revisa la salida DEBUG. Asegúrate de tener MS Word con pywin32 instalado o LibreOffice (soffice) en PATH"
            ) from e2


def extract_text_from_docx(docx_file: Path):
    document = Document(str(docx_file))

    lines = []

    for block in iter_block_items(document):

        # Si es párrafo
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if text:
                lines.append(text)

        # Si es tabla
        elif isinstance(block, Table):
            for row in block.rows:
                row_text = " | ".join(
                    cell.text.strip() for cell in row.cells if cell.text.strip()
                )
                if row_text:
                    lines.append(row_text)

    return lines


# Procesar tanto .docx como .doc
files = list(INPUT_DIR.glob("*.docx")) + list(INPUT_DIR.glob("*.doc"))

for file in files:
    temp_converted = False
    converted_path = None

    if file.suffix.lower() == ".doc":
        try:
            converted_path = convert_doc_to_docx(file)
            temp_converted = True
            source_for_parsing = converted_path
        except RuntimeError as e:
            print(f"ERROR: {e}")
            continue
    else:
        source_for_parsing = file

    try:
        lines = extract_text_from_docx(source_for_parsing)

        output_file = OUTPUT_DIR / f"{file.stem}.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"Convertido: {file.name} → {output_file.name}")
    finally:
        # eliminar archivo .docx temporal si fue creado
        if temp_converted and converted_path is not None:
            try:
                os.remove(converted_path)
                # intentar eliminar el directorio temporal también
                tmpdir = converted_path.parent
                if not any(tmpdir.iterdir()):
                    os.rmdir(tmpdir)
            except Exception:
                pass
