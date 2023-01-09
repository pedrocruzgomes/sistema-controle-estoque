import sqlite3


class Database():
    def __init__(self, name = "system.db") -> None:
        self.name = name

    def conectar(self):
        self.connection = sqlite3.connect(self.name)

    def desconectar(self):
        try:
            self.connection.close()
        except:
            pass

    def criar_tabela_usuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    acesso TEXT NOT NULL
                );
            
            """)
        except AttributeError:
            print("Faça a conexão")

    def inserir_usuario(self, nome, user, senha, acesso):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO usuarios (nome, user, senha, acesso) VALUES (?,?,?,?)
            """, (nome, user, senha, acesso))
            self.connection.commit()
            return ("OK")
        except:
            return ("Erro")

    def checar_usuario(self, user, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM usuarios
            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == senha and linha[4] == "Administrador":
                    return "Administrador"
                elif linha[2].upper() == user.upper() and linha[3] == senha and linha[4] == "Usuário":
                    return "Usuário"
                else:
                    continue
            return "Sem acesso"
        except:
            pass

    def exibir_usuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, nome, user, acesso FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
        except:
            pass

    def modificar_usuario(self, dado):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE usuarios set
            
            id = "{dado[0]}",
            nome = "{dado[1]}",
            user = "{dado[2]}"
            
            WHERE id = "{dado[0]}" """)

        self.connection.commit()

    def deletar_usuario(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM usuarios WHERE id = '{id}' ")
            self.connection.commit()
            return "Usuário excluído com sucesso!"

        except:
            return "Erro ao excluir usuário"

    def criar_tabela_produtos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                
                CREATE TABLE IF NOT EXISTS produtos(
                    codigo TEXT NOT NULL PRIMARY KEY,
                    descprod TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    cor TEXT NOT NULL,
                    qntdestoque TEXT NOT NULL,
                    preco TEXT NOT NULL,
                    data TEXT NOT NULL
                    
                );
                
            """)
        except AttributeError:
            print("Faça a conexão")

    def criar_tabela_fornecedores(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                CREATE TABLE IF NOT EXISTS fornecedores(
                    nome TEXT NOT NULL,
                    endereco TEXT NOT NULL,
                    cidade TEXT NOT NULL,
                    bairro TEXT NOT NULL,
                    uf TEXT NOT NULL,
                    cep TEXT NOT NULL,
                    cnpj TEXT NOT NULL PRIMARY KEY,
                    telefone TEXT NOT NULL
                    
                );
            
            """)
        except AttributeError:
            print("Faça a conexão")

    def inserir_produto(self, codigo, descprod, tipo, cor, qntdestoque, preco, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO produtos (codigo, descprod, tipo, cor, qntdestoque, preco, data)
            VALUES (?,?,?,?,?,?,?)""", (codigo, descprod, tipo, cor, qntdestoque, preco, data))
            self.connection.commit()
            return("OK")
        except:
            return "Erro"

    def exibir_produtos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            return produtos
        except:
            pass

    def alterar_produtos(self, dados):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE produtos set
            
            codigo = "{dados[0]}",
            descprod = "{dados[1]}",
            tipo = "{dados[2]}",
            cor = "{dados[3]}",
            qntdestoque = "{dados[4]}",
            preco = "{dados[5]}",
            data = "{dados[6]}"
            
            WHERE codigo = "{dados[0]}" """)

        self.connection.commit()

    def deletar_produtos(self, codigo):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM produtos WHERE codigo = '{codigo}' ")
            self.connection.commit()
            return "Produto excluido com sucesso"
        except:
            return "Erro ao excluir produto"

    def inserir_fornecedor(self, nome, endereco, cidade, bairro, uf, cep, cnpj, telefone):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO fornecedores (nome, endereco, cidade, bairro, uf, cep, cnpj, telefone)
            VALUES (?,?,?,?,?,?,?,?)""", (nome, endereco, cidade, bairro, uf, cep, cnpj, telefone))
            self.connection.commit()
            return("OK")
        except:
            return "Erro"

    def exibir_fornecedores(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM fornecedores")
            produtos = cursor.fetchall()
            return produtos
        except:
            pass

    def alterar_fornecedores(self, dados):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE fornecedores set

            nome = "{dados[0]}",
            endereco = "{dados[1]}",
            cidade = "{dados[2]}",
            bairro = "{dados[3]}",
            uf = "{dados[4]}",
            cep = "{dados[5]}",
            cnpj = "{dados[6]}",
            telefone = "{dados[7]}"

            WHERE cnpj = "{dados[6]}" """)

        self.connection.commit()

    def deletar_fornecedores(self, cnpj):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM fornecedores WHERE cnpj = '{cnpj}' ")
            self.connection.commit()
            return "Fornecedor excluido com sucesso"
        except:
            return "Erro ao excluir fornecedor"