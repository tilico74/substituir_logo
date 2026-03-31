import fitz  # PyMuPDF
import os
from tkinter import Tk, filedialog, messagebox
from datetime import datetime

# 🔥 BASE DO PROJETO (resolve problema do atalho)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# caminhos corrigidos
LOGO_PATH = os.path.join(BASE_DIR, "img", "logo301x95.png")
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")


def selecionar_pdf():
    root = Tk()
    root.withdraw()  # esconde janela principal

    file_path = filedialog.askopenfilename(
        title="Selecione o PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    root.destroy()
    return file_path


def substituir_logo(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    for page in doc:
        rect = fitz.Rect(16, 35, 200, 120)

        # cobre logo antiga
        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

        # insere nova logo
        page.insert_image(rect, filename=LOGO_PATH)

    doc.save(output_pdf)
    doc.close()


def data_atual():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def main():
    try:
        input_pdf = selecionar_pdf()

        if not input_pdf:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
            return

        output_pdf = os.path.join(
            DOWNLOAD_PATH,
            "orc_" + data_atual() + ".pdf"
        )

        substituir_logo(input_pdf, output_pdf)

        messagebox.showinfo(
            "Sucesso",
            f"Arquivo salvo em:\n{output_pdf}"
        )

    except Exception as e:
        messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    main()