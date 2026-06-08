import tkinter as tk
from tkinter import messagebox

from reconhecimento import reconhecer_usuario
from consulta import consultar_registros
from cadastro import cadastrar_funcionario

COR_PRIMARIA = "#284b63"
COR_CINZA_CLARO = "#d9d9d9"
COR_FUNDO = "#f4f4f9"
COR_SECUNDARIA = "#3c6e71"
COR_ESCURO = "#353535"

janela = tk.Tk()

janela.title("Sistema de Ponto Facial")
janela.geometry("420x300")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)


def abrir_tela_cadastro():

    cadastro = tk.Toplevel(janela)

    cadastro.title("Cadastro de Funcionário")
    cadastro.geometry("450x250")
    cadastro.configure(bg=COR_FUNDO)
    cadastro.resizable(False, False)

    frame_titulo = tk.Frame(
        cadastro,
        bg=COR_PRIMARIA,
        pady=15
    )
    frame_titulo.pack(fill="x")

    tk.Label(
        frame_titulo,
        text="Novo Funcionário",
        font=("Segoe UI", 14, "bold"),
        bg=COR_PRIMARIA,
        fg=COR_FUNDO
    ).pack()

    frame_conteudo = tk.Frame(
        cadastro,
        bg=COR_FUNDO,
        padx=30,
        pady=25
    )
    frame_conteudo.pack(fill="both", expand=True)

    tk.Label(
        frame_conteudo,
        text="Nome do Funcionário",
        font=("Segoe UI", 10),
        bg=COR_FUNDO,
        fg=COR_ESCURO
    ).pack(anchor="w")

    entrada_nome = tk.Entry(
        frame_conteudo,
        font=("Segoe UI", 11)
    )
    entrada_nome.pack(
        fill="x",
        ipady=6,
        pady=(5, 20)
    )

    def salvar():

        nome = entrada_nome.get().strip()

        if not nome:
            messagebox.showwarning(
                "Aviso",
                "Digite o nome do funcionário."
            )
            return

        codigo = cadastrar_funcionario(nome)

        if codigo is None:
            messagebox.showerror(
                "Erro",
                "Não foi possível concluir o cadastro."
            )

            return

        messagebox.showinfo(
            "Sucesso",
            f"Funcionário cadastrado com sucesso!\nID gerado: {codigo}"
        )

        cadastro.destroy()
    tk.Button(
        frame_conteudo,
        text="Capturar Fotos e Salvar",
        command=salvar,
        font=("Segoe UI", 11, "bold"),
        bg=COR_SECUNDARIA,
        fg=COR_FUNDO,
        relief="flat",
        cursor="hand2",
        pady=8
    ).pack(fill="x")


def mostrar_registros():

    texto = consultar_registros()

    janela_consulta = tk.Toplevel(janela)
    janela_consulta.title("Registros de Ponto")
    janela_consulta.geometry("500x400")
    janela_consulta.configure(bg=COR_FUNDO)

    frame_titulo = tk.Frame(
        janela_consulta,
        bg=COR_PRIMARIA,
        pady=12
    )
    frame_titulo.pack(fill="x")

    tk.Label(
        frame_titulo,
        text="Registros de Ponto",
        font=("Segoe UI", 14, "bold"),
        bg=COR_PRIMARIA,
        fg=COR_FUNDO
    ).pack()

    frame_texto = tk.Frame(
        janela_consulta,
        bg=COR_FUNDO,
        padx=15,
        pady=15
    )
    frame_texto.pack(fill="both", expand=True)

    area = tk.Text(
        frame_texto,
        font=("Consolas", 10),
        bg="white",
        fg=COR_ESCURO
    )

    area.pack(
        fill="both",
        expand=True
    )

    area.insert("1.0", texto)
    area.config(state="disabled")


def bater_ponto():

    reconhecer_usuario()


# ==========================
# CABEÇALHO
# ==========================

frame_header = tk.Frame(
    janela,
    bg=COR_PRIMARIA,
    pady=18
)
frame_header.pack(fill="x")

tk.Label(
    frame_header,
    text="Sistema de Ponto Facial",
    font=("Segoe UI", 16, "bold"),
    bg=COR_PRIMARIA,
    fg=COR_FUNDO
).pack()


# ==========================
# BOTÕES
# ==========================

frame_botoes = tk.Frame(
    janela,
    bg=COR_FUNDO,
    padx=40,
    pady=30
)
frame_botoes.pack(fill="both", expand=True)

tk.Button(
    frame_botoes,
    text="Cadastrar Funcionário",
    command=abrir_tela_cadastro,
    font=("Segoe UI", 11, "bold"),
    bg=COR_SECUNDARIA,
    fg=COR_FUNDO,
    relief="flat",
    cursor="hand2",
    pady=8
).pack(fill="x", pady=(0, 10))

tk.Button(
    frame_botoes,
    text="Consultar Registros",
    command=mostrar_registros,
    font=("Segoe UI", 11, "bold"),
    bg=COR_SECUNDARIA,
    fg=COR_FUNDO,
    relief="flat",
    cursor="hand2",
    pady=8
).pack(fill="x", pady=(0, 10))

tk.Button(
    frame_botoes,
    text="Bater Ponto",
    command=bater_ponto,
    font=("Segoe UI", 11, "bold"),
    bg=COR_ESCURO,
    fg=COR_FUNDO,
    relief="flat",
    cursor="hand2",
    pady=8
).pack(fill="x")

janela.mainloop()