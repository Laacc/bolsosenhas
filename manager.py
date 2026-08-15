import random
import string
import sqlite3

class GerenciadorSenhas:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as con:
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS senhas ("
                           "id INTEGER PRIMARY KEY," \
                           "plataforma TEXT," \
                           "senha TEXT)")
            con.commit()
            
    def gerar_senha(self, tamanho=16):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = "".join(random.choices(caracteres, k=tamanho))
        return senha
    
    def salvar_senha(self, plataforma, senha):
        nova_senha = ((plataforma, senha))
        with sqlite3.connect(self.caminho) as con:
            cursor = con.cursor()
            cursor.execute("INSERT INTO senhas (plataforma, senha) VALUES (?, ?)", nova_senha)
            con.commit()

    def carregar_senhas(self):
        with sqlite3.connect(self.caminho) as con:
            senhas = []
            cursor = con.cursor()
            cursor.execute("SELECT * FROM senhas ORDER BY id, plataforma")
            fetch = cursor.fetchall()
            for linha in fetch:
                senhas.append(linha)
            return senhas

    def trocar_senha(self, plataforma):
        senha = self.gerar_senha()
        nova_senha = ((senha, plataforma))
        with sqlite3.connect(self.caminho) as con:
            cursor = con.cursor()
            cursor.execute("UPDATE senhas SET senha=(?) WHERE plataforma=(?)", nova_senha)
            row_bool = cursor.rowcount
            con.commit()
            if row_bool == 1:
                return True
            else:
                return False
            
    def deletar_senha(self, plataforma):
        plataforma_busca = ((plataforma,))
        with sqlite3.connect(self.caminho) as con:
            cursor = con.cursor()
            cursor.execute("DELETE FROM senhas WHERE plataforma=(?)", plataforma_busca)
            row_bool = cursor.rowcount
            con.commit()
            return row_bool == 1
