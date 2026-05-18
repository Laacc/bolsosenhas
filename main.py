import random
import string
import os
import sys
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from PIL import Image, ImageTk


arquivo = "herebedragons.txt"
def gerar_senha(tamanho=24):
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
    dialogo = CTkInputDialog(title="Gerar e salvar senha", text="Digite a plataforma: ")
    plataforma = dialogo.get_input()
    if plataforma != None and plataforma != "":
        senha = gerar_senha()
        salvar_senha(plataforma, senha, arquivo)
        CTkMessagebox(title="Completo!", message="Senha gerada!")
    else:
        if plataforma == "":
            CTkMessagebox(title="Operação inválida", message="Informe uma plataforma!")
            return   
        CTkMessagebox(title="Operação cancelada", message="A Operação foi cancelada!")
        return 

def consultar():
    os.startfile(arquivo)

def trocar():
    dialogo = CTkInputDialog(title="Alterar senha", text="Plataforma a alterar: ")
    plataforma = dialogo.get_input()
    if plataforma != None and plataforma != "":
        trocar_senha(caminho_arquivo=arquivo, plataforma=plataforma)
        CTkMessagebox(title="Completo!", message="Senha alterada!")
    else:
        if plataforma == "":
            CTkMessagebox(title="Operação inválida", message="Informe uma plataforma!")
            return
        CTkMessagebox(title="Operação cancelada", message="A Operação foi cancelada")
        return

janela = CTk()
janela.title("Bolsosenhas (Flávio Edition)")
janela.geometry("500x400")
botao1 = CTkButton(janela, text="Gerar e salvar senha", command=gerar_salvar_s, corner_radius=32, fg_color="#1C24C5", hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao1.place(relx=0.5, rely=0.3, anchor="center")
botao2 = CTkButton(janela, text="Consultar senhas", command=consultar, corner_radius=32, fg_color="#1C24C5", hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao2.place(relx= 0.5, rely=0.4, anchor="center")
botao3 = CTkButton(janela, text="Alterar senha", command=trocar, corner_radius=32, fg_color="#1C24C5", hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao3.place(relx=0.5, rely=0.5, anchor="center")
botao4 = CTkButton(janela, text="Sair", command=janela.destroy, corner_radius=32, fg_color="#1C24C5", hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao4.place(relx=0.5, rely=0.6, anchor="center" )
janela.mainloop()
