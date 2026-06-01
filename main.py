import tkinter as tk
from tkinter import messagebox

from reconhecimento import reconhecer_usuario
from consulta import consultar_registros
from cadastro import cadastrar_funcionario

janela = tk.Tk()

janela.title("Sistema de Ponto Facial")
janela.geometry("400x350")


def cadastrar():

    codigo = entrada_codigo.get()
    nome = entrada_nome.get()

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

        messagebox.showwarning(
            "Aviso",
            "Cadastro cancelado."
        )


def mostrar_registros():

    texto = consultar_registros()

    janela_consulta = tk.Toplevel(janela)
    janela_consulta.title("Registros")

    area = tk.Text(janela_consulta)

    area.pack(
        fill="both",
        expand=True
    )

    area.insert("1.0", texto)


def bater_ponto():

    reconhecer_usuario()


tk.Label(
    janela,
    text="Código"
).pack()

entrada_codigo = tk.Entry(janela)
entrada_codigo.pack()

tk.Label(
    janela,
    text="Nome"
).pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Button(
    janela,
    text="Cadastrar Funcionário",
    command=cadastrar
).pack(pady=10)

tk.Button(
    janela,
    text="Consultar Registros",
    command=mostrar_registros
).pack(pady=10)

tk.Button(
    janela,
    text="Bater Ponto",
    command=bater_ponto
).pack(pady=10)

janela.mainloop()