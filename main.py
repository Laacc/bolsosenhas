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
    
def trocar_senha(caminho_arquivo, plataforma):
    senhas = carregar_senhas(caminho_arquivo)
    encontrado = False
    for linha in senhas:
        if linha[0] == plataforma:
            encontrado = True
            nova_senha = gerar_senha()
            linha[1] = nova_senha
            break
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in senhas:
            arquivo.write(f"{linha[0]};{linha[1]}\n")
    return encontrado

def deletar_senha(caminho_arquivo, plataforma):
    senhas = carregar_senhas(caminho_arquivo)
    encontrado = False
    for linha in senhas:
        if linha[0] == plataforma:
            encontrado = True
            senhas.remove(linha)
            break
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in senhas:
            arquivo.write(f"{linha[0]};{linha[1]}\n")
    return encontrado


    
def gerar_salvar_s():
    dialogo = CTkInputDialog(title="Gerar e salvar senha", text="Digite a plataforma: ")
    plataforma = dialogo.get_input()
    if plataforma != None and plataforma != "":
        senha = gerar_senha()
        salvar_senha(plataforma, senha, arquivo)
        CTkMessagebox(title="Completo!", message="Senha gerada!", icon="check")
    else:
        if plataforma == "":
            CTkMessagebox(title="Operação inválida", message="Informe uma plataforma!", icon="cancel")
            return   
        CTkMessagebox(title="Operação cancelada", message="A Operação foi cancelada!")
        return 

def consultar():
    os.startfile(arquivo)

def trocar():
    dialogo = CTkInputDialog(title="Alterar senha", text="Plataforma a alterar: ")
    plataforma = dialogo.get_input()
    if plataforma != None and plataforma != "":
        alterada = trocar_senha(caminho_arquivo=arquivo, plataforma=plataforma)
        if alterada == True:
            CTkMessagebox(title="Sucesso!", message="Senha alterada!", icon="check")
        else:
            CTkMessagebox(title="Erro", message="Plataforma não encontrada!", icon="cancel")
    else:
        if plataforma == "":
            CTkMessagebox(title="Operação inválida", message="Informe uma plataforma!", icon="cancel")
            return
        CTkMessagebox(title="Operação cancelada", message="A Operação foi cancelada")
        return
    
def deletar():
    dialogo = CTkInputDialog(title="Deletar senha", text="Plataforma para deletar: ")
    plataforma = dialogo.get_input()
    if plataforma != None and plataforma != "":
        deletada = deletar_senha(caminho_arquivo=arquivo, plataforma=plataforma)
        if deletada == True:
            CTkMessagebox(title="Sucesso!", message="Senha deletada!", icon="check")
        else:
            CTkMessagebox(title="Erro", message="Plataforma não encontrada!", icon="cancel")
    else:
        if plataforma == "":
            CTkMessagebox(title="Operação inválida", message="Informe uma plataforma!", icon="cancel")
            return
        CTkMessagebox(title="Operação cancelada", message="A Operação foi cancelada!")
        return

janela = CTk()
janela.title("Bolsosenhas (Flávio Edition)")
janela.geometry("500x400")
botao1 = CTkButton(janela, text="Gerar e salvar senha", command=gerar_salvar_s, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao1.place(relx=0.5, rely=0.3, anchor="center")
botao2 = CTkButton(janela, text="Consultar senhas", command=consultar, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao2.place(relx= 0.5, rely=0.4, anchor="center")
botao3 = CTkButton(janela, text="Alterar senha", command=trocar, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao3.place(relx=0.5, rely=0.5, anchor="center")
botao4 = CTkButton(janela, text="Deletar senha", command=deletar, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao4.place(relx=0.5, rely=0.6, anchor="center")
botao5 = CTkButton(janela, text="Sair", command=janela.destroy, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B")
botao5.place(relx=0.5, rely=0.7, anchor="center" )

janela.mainloop()
