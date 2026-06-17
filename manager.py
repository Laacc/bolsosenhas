import random
import string
import sqlite3
import os

class GerenciadorSenhas:
    def __init__(self):
        self.caminho = os.path.join("data", "data.db")
        with sqlite3.connect(self.caminho) as con:
            cursor = con.cursor()
            cursor.execute("" \
            "CREATE TABLE IF NOT EXISTS data(" \
            "plataforma TEXT," \
            "senha TEXT)")
            con.commit()

    def gerar_senha(self, tamanho=16):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = "".join(random.choices(caracteres, k=tamanho))
        return senha
    
    def salvar_senha(self, plataforma, senha):
        with sqlite3.connect(self.caminho) as con:
            nova_senha = ((plataforma, senha))
            cursor = con.cursor()
            cursor.execute("INSERT INTO data VALUES (?, ?)", nova_senha)
            con.commit()

    def carregar_senhas(self):
        with sqlite3.connect(self.caminho) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM data")
            fetch = cursor.fetchall()
            return fetch
        
    def trocar_senha(self, plataforma):
        with sqlite3.connect(self.caminho) as con:
            nova_senha_gerada = self.gerar_senha()
            nova_senha_final = ((nova_senha_gerada, plataforma))
            cursor = con.cursor()
            cursor.execute("UPDATE data SET senha=(?) WHERE plataforma=(?)", nova_senha_final)
            atualizado = cursor.rowcount
            con.commit()
            if atualizado:
                return True
            else:
                return False

    def deletar_senha(self, plataforma):
        with sqlite3.connect(self.caminho) as con:
            plataforma_f = (plataforma,)
            cursor = con.cursor()
            cursor.execute("DELETE FROM data WHERE plataforma=(?)", plataforma_f)
            atualizado = cursor.rowcount
            con.commit()
            if atualizado:
                return True
            else:
                return False