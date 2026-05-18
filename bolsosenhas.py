import random
import string
import tkinter as tk
from tkinter import simpledialog
import os

arquivo = "flavio.txt"
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choices(caracteres, k=tamanho))
    return senha

def salvar_senha(plataforma, senha, caminho_arquivo):
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{plataforma};{senha}\n")

def carregar_senhas(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        senhas = []
        for linha in arquivo:
            linha = linha.strip().split(";")
            senhas.append(linha)
        return senhas
    
def consultar_senhas(caminho_arquivo):
    resultado = carregar_senhas(caminho_arquivo)
    for linha in resultado:
        print(f"Plataforma: {linha[0]} | Senha: {linha[1]}")

def trocar_senha(caminho_arquivo, plataforma):
    senhas = carregar_senhas(caminho_arquivo)
    for linha in senhas:
        if linha[0] == plataforma:
            nova_senha = gerar_senha()
            linha[1] = nova_senha
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in senhas:
            arquivo.write(f"{linha[0]};{linha[1]}\n")

    
def gerar_salvar_s():
    plataforma = simpledialog.askstring("Gerar e salvar senha", "Digite a plataforma: ")
    senha = gerar_senha()
    salvar_senha(plataforma, senha, arquivo)

def consultar():
    os.startfile(arquivo)

def trocar():
    plataforma = simpledialog.askstring("Trocar senha", "Plataforma a trocar: ")
    trocar_senha(caminho_arquivo=arquivo, plataforma=plataforma)



janela = tk.Tk()
janela.title("Bolsosenhas (Flávio Edition)")
janela.geometry("600x400")
fundo = tk.PhotoImage(file="flaviojudeu.png")
fundo_label = tk.Label(janela, image=fundo)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)
botao1 = tk.Button(janela, text="Gerar e salvar senha", command=gerar_salvar_s)
botao1.pack()
botao2 = tk.Button(janela, text="Consultar senhas", command=consultar)
botao2.pack()
botao3 = tk.Button(janela, text="Alterar senha", command=trocar)
botao3.pack()
botao4 = tk.Button(janela, text="Sair", command=janela.destroy)
botao4.pack()
janela.mainloop()

        