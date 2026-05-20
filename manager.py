import random
import string

class GerenciadorSenhas:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        with open(self.arquivo, "a", encoding="utf-8") as a:
            pass

    def gerar_senha(self, tamanho=24):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = "".join(random.choices(caracteres, k=tamanho))
        return senha
    
    def salvar_senha(self, plataforma, senha):
        with open(self.arquivo, "a", encoding="utf-8") as a:
            a.write(f"{plataforma};{senha}\n")

    def carregar_senhas(self):
        with open(self.arquivo, "r", encoding="utf-8") as a:
            senhas = []
            for linha in a:
                linha = linha.strip().split(";")
                senhas.append(linha)
            return senhas
        
    def trocar_senha(self, plataforma):
        senhas = self.carregar_senhas()
        encontrado = False
        for linha in senhas:
            if linha[0] == plataforma:
                encontrado = True
                nova_senha = self.gerar_senha()
                linha[1] = nova_senha
                break
        with open(self.arquivo, "w", encoding="utf-8") as a:
            for linha in senhas:
                a.write(f"{linha[0]};{linha[1]}\n")
        return encontrado
    
    def deletar_senha(self, plataforma):
        senhas = self.carregar_senhas()
        encontrado = False
        for linha in senhas:
            if linha[0] == plataforma:
                encontrado = True
                senhas.remove(linha)
                break
        with open(self.arquivo, "w", encoding="utf-8") as a:
            for linha in senhas:
                a.write(f"{linha[0]};{linha[1]}\n")
        return encontrado