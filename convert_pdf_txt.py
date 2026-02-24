#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
convert_pdf_txt.py

Convierte PDFs a TXT.
- Si el PDF tiene texto → usa PyPDF2
- Si el PDF es imagen → usa OCR (pdf2image + Tesseract)

Requisitos:
    pip install PyPDF2 pdf2image pytesseract pillow

También necesitas:
    - Tesseract instalado
    - Poppler descomprimido
"""

from __future__ import annotations
import argparse
import os
import sys
from typing import Iterable, Set, Optional
from pathlib import Path


# ==========================
# 🔧 CONFIGURA TUS RUTAS AQUÍ
# ========================== 

TESSERACT_PATH = r"C:\Users\raquell.martinez\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\raquell.martinez\poppler\Release-25.12.0-0\poppler-25.12.0\Library\bin"

# ==========================


def pedir_instalacion_paquete(name: str) -> None:
    mensaje = (
        f"Falta el paquete '{name}'. Instálalo con:\n"
        f"    pip install {name}\n"
    )
    print(mensaje, file=sys.stderr)


def parsear_rango_paginas(rango: Optional[str], total: int) -> Set[int]:
    if rango is None or rango.strip().lower() in ('all', ''):
        return set(range(total))

    indices: Set[int] = set()
    partes = [p.strip() for p in rango.split(',') if p.strip()]

    for parte in partes:
        if '-' in parte:
            a, b = parte.split('-', 1)
            a_i = int(a)
            b_i = int(b)
            for p in range(a_i - 1, b_i):
                if 0 <= p < total:
                    indices.add(p)
        else:
            p = int(parte)
            if 1 <= p <= total:
                indices.add(p - 1)

    return indices


def convertir(pdf_path: str, txt_path: str | Path, paginas: str | None, password: str | None) -> int:
    try:
        from PyPDF2 import PdfReader
    except Exception:
        pedir_instalacion_paquete('PyPDF2')
        raise

    try:
        from pdf2image import convert_from_path
    except Exception:
        pedir_instalacion_paquete('pdf2image')
        raise

    try:
        import pytesseract
    except Exception:
        pedir_instalacion_paquete('pytesseract')
        raise

    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"No existe el archivo: {pdf_path}")

    # Configurar Tesseract
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    reader = PdfReader(pdf_path)

    if reader.is_encrypted:
        if password:
            reader.decrypt(password)
        else:
            try:
                reader.decrypt("")
            except Exception:
                raise RuntimeError("El PDF está cifrado. Usa -w contraseña.")

    total = len(reader.pages)
    indices = parsear_rango_paginas(paginas, total)

    textos: list[str] = []
    extraidas = 0

    for i in sorted(indices):
        page = reader.pages[i]

        try:
            texto = page.extract_text()
        except AttributeError:
            texto = page.extractText()

        # Si no hay texto → aplicar OCR
        if not texto or texto.strip() == "":
            print(f"Aplicando OCR en página {i+1}...")

            images = convert_from_path(
                pdf_path,
                first_page=i+1,
                last_page=i+1,
                poppler_path=POPPLER_PATH
            )

            texto = pytesseract.image_to_string(images[0], lang="spa")

            textos.append(f"\n\n--- Página {i+1} (OCR) ---\n\n")
            textos.append(texto)

        else:
            textos.append(f"\n\n--- Página {i+1} ---\n\n")
            textos.append(texto)

        extraidas += 1

    txt_path = str(txt_path)
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.writelines(textos)

    return extraidas


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description='Convierte un PDF a TXT (con soporte OCR).')
    p.add_argument('input', nargs='?', default='cv/templates_input',
                   help="Archivo PDF o carpeta con PDFs.")
    p.add_argument('txt', nargs='?', help='Ruta de salida .txt (solo para un archivo).')
    p.add_argument('-p', '--pages', help="Páginas: 'all' o rango tipo '1-3,5'.")
    p.add_argument('-w', '--password', help='Contraseña si el PDF está cifrado')
    args = p.parse_args(list(argv) if argv is not None else None)

    OUTPUT_DIR = Path("cv/parsed")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    entrada = args.input

    # Si es carpeta
    if os.path.isdir(entrada):
        archivos = sorted([f for f in os.listdir(entrada) if f.lower().endswith('.pdf')])

        exitos = []
        fallidos = []

        for nombre in archivos:
            pdf_path = os.path.join(entrada, nombre)
            stem = Path(pdf_path).stem
            txt_path = OUTPUT_DIR / f"{stem}.txt"

            try:
                paginas_extraidas = convertir(pdf_path, txt_path, args.pages, args.password)
                print(f"Hecho: {pdf_path} -> {txt_path}  (páginas procesadas: {paginas_extraidas})")
                exitos.append(pdf_path)
            except Exception as e:
                print(f"Error procesando {pdf_path}: {e}", file=sys.stderr)
                fallidos.append((pdf_path, str(e)))

        print('\nResumen:')
        print(f"  Procesados: {len(exitos)}")
        if fallidos:
            print(f"  Fallidos: {len(fallidos)}")
            for p, err in fallidos:
                print(f"    - {p}: {err}")

        return 0 if not fallidos else 3

    # Si es archivo único
    pdf_path = entrada
    if args.txt:
        txt_path = args.txt
    else:
        stem = Path(pdf_path).stem
        txt_path = OUTPUT_DIR / f"{stem}.txt"

    try:
        paginas_extraidas = convertir(pdf_path, txt_path, args.pages, args.password)
    except Exception as e:
        print('Error:', e, file=sys.stderr)
        return 2

    print(f"Hecho: {pdf_path} -> {txt_path}  (páginas procesadas: {paginas_extraidas})")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
