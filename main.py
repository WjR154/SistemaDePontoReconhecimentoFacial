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
janela.geometry("420x480")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)



def cadastrar():

    codigo = entrada_codigo.get().strip()
    nome = entrada_nome.get().strip()

    if not codigo or not nome:

        messagebox.showwarning(
            "Aviso",
            "Preencha todos os campos."
        )
        return

    sucesso = cadastrar_funcionario(
        codigo,
        nome
    )

    if sucesso:

        messagebox.showinfo(
            "Sucesso",
            "Funcionário cadastrado e modelo atualizado."
        )

    else:

        messagebox.showerror(
            "Erro",
            "ID já cadastrado."
        )


def mostrar_registros():

    texto = consultar_registros()

    janela_consulta = tk.Toplevel(janela)
    janela_consulta.title("Registros de Ponto")
    janela_consulta.geometry("500x400")
    janela_consulta.configure(bg=COR_FUNDO)

    frame_titulo_consulta = tk.Frame(janela_consulta, bg=COR_PRIMARIA, pady=12)
    frame_titulo_consulta.pack(fill="x")

    tk.Label(
        frame_titulo_consulta,
        text="Registros de Ponto",
        font=("Segoe UI", 14, "bold"),
        bg=COR_PRIMARIA,
        fg=COR_FUNDO
    ).pack()

    frame_texto = tk.Frame(janela_consulta, bg=COR_FUNDO, padx=15, pady=15)
    frame_texto.pack(fill="both", expand=True)

    area = tk.Text(
        frame_texto,
        font=("Consolas", 10),
        bg="white",
        fg=COR_ESCURO,
        relief="flat",
        bd=0,
        highlightthickness=1,
        highlightbackground=COR_CINZA_CLARO,
        highlightcolor=COR_SECUNDARIA,
        padx=10,
        pady=10
    )

    area.pack(
        fill="both",
        expand=True
    )

    area.insert("1.0", texto)


def bater_ponto():

    reconhecer_usuario()


# === Header ===
frame_header = tk.Frame(janela, bg=COR_PRIMARIA, pady=18)
frame_header.pack(fill="x")

tk.Label(
    frame_header,
    text="Sistema de Ponto Facial",
    font=("Segoe UI", 16, "bold"),
    bg=COR_PRIMARIA,
    fg=COR_FUNDO
).pack()

# === Formulário ===
frame_form = tk.Frame(janela, bg=COR_FUNDO, padx=40, pady=20)
frame_form.pack(fill="x")

tk.Label(
    frame_form,
    text="Código",
    font=("Segoe UI", 10),
    bg=COR_FUNDO,
    fg=COR_ESCURO,
    anchor="w"
).pack(fill="x", pady=(0, 2))

entrada_codigo = tk.Entry(
    frame_form,
    font=("Segoe UI", 11),
    bg="white",
    fg=COR_ESCURO,
    relief="flat",
    bd=0,
    highlightthickness=1,
    highlightbackground=COR_CINZA_CLARO,
    highlightcolor=COR_SECUNDARIA
)
entrada_codigo.pack(fill="x", ipady=6, pady=(0, 10))

tk.Label(
    frame_form,
    text="Nome",
    font=("Segoe UI", 10),
    bg=COR_FUNDO,
    fg=COR_ESCURO,
    anchor="w"
).pack(fill="x", pady=(0, 2))

entrada_nome = tk.Entry(
    frame_form,
    font=("Segoe UI", 11),
    bg="white",
    fg=COR_ESCURO,
    relief="flat",
    bd=0,
    highlightthickness=1,
    highlightbackground=COR_CINZA_CLARO,
    highlightcolor=COR_SECUNDARIA
)
entrada_nome.pack(fill="x", ipady=6, pady=(0, 10))

# === Botões ===
frame_botoes = tk.Frame(janela, bg=COR_FUNDO, padx=40)
frame_botoes.pack(fill="x")

tk.Button(
    frame_botoes,
    text="Cadastrar Funcionário",
    command=cadastrar,
    font=("Segoe UI", 11, "bold"),
    bg=COR_PRIMARIA,
    fg=COR_FUNDO,
    activebackground=COR_SECUNDARIA,
    activeforeground=COR_FUNDO,
    relief="flat",
    cursor="hand2",
    pady=8
).pack(fill="x", pady=(0, 8))

tk.Button(
    frame_botoes,
    text="Consultar Registros",
    command=mostrar_registros,
    font=("Segoe UI", 11, "bold"),
    bg=COR_SECUNDARIA,
    fg=COR_FUNDO,
    activebackground=COR_PRIMARIA,
    activeforeground=COR_FUNDO,
    relief="flat",
    cursor="hand2",
    pady=8
).pack(fill="x", pady=(0, 8))

tk.Button(
    frame_botoes,
    text="Bater Ponto",
    command=bater_ponto,
    font=("Segoe UI", 11, "bold"),
    bg=COR_ESCURO,
    fg=COR_FUNDO,
    activebackground=COR_PRIMARIA,
    activeforeground=COR_FUNDO,
    relief="flat",
    cursor="hand2",
    pady=8
).pack(fill="x", pady=(0, 8))

janela.mainloop()