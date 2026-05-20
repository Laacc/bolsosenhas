import os
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from PIL import Image
from manager import GerenciadorSenhas

class JanelaPrincipal(CTk):
    def __init__(self):
        super().__init__()
        caminho_pasta = os.path.join("data", "data.txt")
        self.gerenciador = GerenciadorSenhas(caminho_pasta)
        self.title("Bolsosenhas")
        self.geometry("500x500")
        self.resizable(False, False)

        self.icon_gerar = os.path.join("imgs", "key.png")
        self.icon_busca = os.path.join("imgs", "password-magnifying-glass.png")
        self.icon_mudar = os.path.join("imgs", "rotate-square.png")
        self.icon_deletar = os.path.join("imgs", "trash.png")
        self.icon_sair = os.path.join("imgs", "exit.png")
        self.icon_gerar_pil = Image.open(self.icon_gerar)
        self.icon_busca_pil = Image.open(self.icon_busca) 
        self.icon_mudar_pil = Image.open(self.icon_mudar) 
        self.icon_deletar_pil = Image.open(self.icon_deletar) 
        self.icon_sair_pil = Image.open(self.icon_sair)
        self.icon_gerar_ctk = CTkImage(light_image=self.icon_gerar_pil, dark_image=self.icon_gerar_pil, size=(15, 15))
        self.icon_busca_ctk = CTkImage(light_image=self.icon_busca_pil, dark_image=self.icon_busca_pil, size=(15, 15))
        self.icon_mudar_ctk = CTkImage(light_image=self.icon_mudar_pil, dark_image=self.icon_mudar_pil, size=(15, 15))
        self.icon_deletar_ctk = CTkImage(light_image=self.icon_deletar_pil, dark_image=self.icon_deletar_pil, size=(15, 15))
        self.icon_sair_ctk = CTkImage(light_image=self.icon_sair_pil, dark_image=self.icon_sair_pil, size=(15, 15))

        self.botao1 = CTkButton(self, text="Gerar e salvar senha", command=self.gerar_salvar_s, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B", image=self.icon_gerar_ctk)
        self.botao1.place(relx=0.5, rely=0.3, anchor="center")
        self.botao2 = CTkButton(self, text="Consultar senhas", command=self.consultar_senhas, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B", image=self.icon_busca_ctk)
        self.botao2.place(relx= 0.5, rely=0.4, anchor="center")
        self.botao3 = CTkButton(self, text="Alterar senha", command=self.trocar_senha, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B", image=self.icon_mudar_ctk)
        self.botao3.place(relx=0.5, rely=0.5, anchor="center")
        self.botao4 = CTkButton(self, text="Deletar senha", command=self.deletar_senha, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B", image=self.icon_deletar_ctk)
        self.botao4.place(relx=0.5, rely=0.6, anchor="center")
        self.botao5 = CTkButton(self, text="Sair", command=self.destroy, corner_radius=32, hover_color="#70BEEB", border_width=1, border_color="#2B4A5B", image=self.icon_sair_ctk)
        self.botao5.place(relx=0.5, rely=0.7, anchor="center" )

    def gerar_salvar_s(self):
        dialogo = CTkInputDialog(title="Gerar e salvar senha", text="Digite a plataforma: ")
        plataforma = dialogo.get_input().lower()
        if plataforma != None and plataforma != "":
            senha = self.gerenciador.gerar_senha()
            self.gerenciador.salvar_senha(plataforma, senha)
            CTkMessagebox(title="Completo!", message="Senha gerada!", icon="check")
        else:
            if plataforma == "":
                CTkMessagebox(title="Operação inválida", message="Informe uma plataforma!", icon="cancel")
                return   
            CTkMessagebox(title="Operação cancelada", message="A Operação foi cancelada!")
            return
        
    def consultar_senhas(self):
        os.startfile(self.gerenciador.arquivo)

    def trocar_senha(self):
        dialogo = CTkInputDialog(title="Alterar senha", text="Plataforma a alterar: ")
        plataforma = dialogo.get_input().lower()
        if plataforma != None and plataforma != "":
            alterada = self.gerenciador.trocar_senha(plataforma=plataforma)
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
        
    def deletar_senha(self):
        dialogo = CTkInputDialog(title="Deletar senha", text="Plataforma para deletar: ")
        plataforma = dialogo.get_input().lower()
        if plataforma != None and plataforma != "":
            deletada = self.gerenciador.deletar_senha(plataforma=plataforma)
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