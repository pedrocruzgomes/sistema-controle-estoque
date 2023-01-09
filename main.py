import pandas as pd
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QTableView, QDateEdit)
from sistema import Ui_MainWindow
from login import Ui_Login
import sys
from database import Database
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon("icones/iconeapp.png")
        self.setWindowIcon(appIcon)

        self.btn_login.clicked.connect(self.checar_login)

    def checar_login(self):
        self.usuarios = Database()
        self.usuarios.conectar()
        acesso = self.usuarios.checar_usuario(self.txt_user.text().upper(), self.txt_senha.text())

        if acesso.lower() == "administrador" or acesso.lower() == "usuário":
            self.w = MainWindow(acesso.lower())
            self.w.showMaximized()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao Acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativas +1} de 3')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                self.usuarios.desconectar()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema Controle de Estoque")
        appIcon = QIcon("icones/iconeapp.png")
        self.setWindowIcon(appIcon)

        if user.lower() == "usuário":
            self.btn_cad_user.clicked.connect(self.alerta)
            self.btn_alterar_user.clicked.connect(self.alerta)
            self.btn_alterar_user.clicked.connect(self.buscar_usuarios)
            self.btn_excluir_user.clicked.connect(self.alerta)

        elif user.lower() == "administrador":
            self.btn_cad_user.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_cad_user))
            self.btn_alterar_user.clicked.connect(self.atualizar_usuario)
            self.btn_excluir_user.clicked.connect(self.excluir_usuario)

        self.btn_cad_prod.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_cad_prod))
        self.btn_estoque.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_estoque))
        self.btn_users.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_users))

        self.btn_sair.clicked.connect(exit)
        self.btn_menu.clicked.connect(self.animacao_menu)
        self.btn_cadastro_user.clicked.connect(self.adicionar_usuario)

        self.btn_salvar_prod.clicked.connect(self.cadastrar_produto)

        self.btn_alterar_tw_estoque.clicked.connect(self.atualizar_produto)
        self.btn_excluir_tw_estoque.clicked.connect(self.excluir_produto)
        self.btn_relatorio_tw_estoque.clicked.connect(self.gerar_excel_produtos)

        self.btn_alterar_tw_fornecedores.clicked.connect(self.atualizar_fornecedor)
        self.btn_excluir_tw_fornecedores.clicked.connect(self.excluir_fornecedor)
        self.btn_relatorio_tw_fornecedores.clicked.connect(self.gerar_excel_fornecedores)

        self.calendario_prod.selectionChanged.connect(self.conectar_calendario)

        self.txt_pesquisa_prod.textChanged.connect(self.filtro)

        self.buscar_usuarios()
        self.buscar_produtos()
        self.buscar_fornecedores()
        self.tv_pesquisa_estoque()

    def alerta(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Acesso Negado")
        msg.setText("Você não possui acesso para acessar essa função do sistema!")
        msg.exec()

    def animacao_menu(self):
        width = self.menu.width()
        if width == 0:
            newWidth = 230
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def adicionar_usuario(self):
        if self.txt_senha_user.text() != self.txt_senha2_user.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas Diferentes")
            msg.setText("As senhas não são iguais!")
            msg.exec()
            return None

        nome = self.txt_nome_user.text()
        usuario = self.txt_user_user.text()
        senha = self.txt_senha_user.text()
        acesso = self.txt_perfil_user.currentText()

        db = Database()
        db.conectar()
        resp = db.inserir_usuario(nome, usuario, senha, acesso)
        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro de Usuário")
            msg.setText("Cadastro de usuário realizado com sucesso!")
            msg.exec()

            self.buscar_usuarios()
            self.txt_nome_user.setText("")
            self.txt_user_user.setText("")
            self.txt_senha_user.setText("")
            self.txt_senha2_user.setText("")
            db.desconectar()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Cadastro de Usuário")
            msg.setText("Erro ao cadastrar usuário, verifique se as informações foram preenchidas corretamente!")
            msg.exec()
            db.desconectar()
            return

    def buscar_usuarios(self):
        db = Database()
        db.conectar()
        resultado = db.exibir_usuarios()

        self.tw_users.clearContents()
        self.tw_users.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tw_users.setItem(row, column, QTableWidgetItem(str(data)))

        db.desconectar()

    def atualizar_usuario(self):
        dados = []
        dados_atualizados = []

        for row in range(self.tw_users.rowCount()):
            for column in range(self.tw_users.columnCount()):
                dados.append(self.tw_users.item(row, column).text())
            dados_atualizados.append(dados)
            dados = []

        db = Database()
        db.conectar()

        for usuario in dados_atualizados:
            db.modificar_usuario(tuple(usuario))

        db.desconectar()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Usuário")
        msg.setText("Dados do usuário atualizados com sucesso")
        msg.exec()

        self.tw_users.reset()
        self.buscar_usuarios()

    def excluir_usuario(self):
        db = Database()
        db.conectar()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este usuário será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.tw_users.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.deletar_usuario(id)
            self.buscar_usuarios()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Exclusão")
            msg.setText(result)
            msg.exec()

        db.desconectar()

    def conectar_calendario(self):
        self.txt_data_prod.setDate(self.calendario_prod.selectedDate())

    def cadastrar_produto(self):
        db = Database()
        db.conectar()

        codigo = self.txt_cod_prod.text()
        descprod = self.txt_desc_prod.text()
        tipoprod = self.txt_tipo_prod.currentText()
        corprod = self.txt_cor_prod.text()
        qntdprod = self.txt_qntd_prod.text()
        precoprod = self.txt_preco_prod.text()
        data = self.txt_data_prod.text()

        nome = self.txt_nome_forn.text()
        endereco = self.txt_end_forn.text()
        cidade = self.txt_cidade_forn.text()
        bairro = self.txt_bairro_forn.text()
        uf = self.txt_uf_forn.currentText()
        cep = self.txt_cep_forn.text()
        cnpj = self.txt_cnpj_forn.text()
        telefone = self.txt_tel_forn.text()

        if self.txt_cod_prod.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Cadastro de Dados")
            msg.setText("Erro! Por favor preencha todos os campos")
            msg.exec()
        elif self.txt_cnpj_forn.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Cadastro de Dados")
            msg.setText("Erro! Por favor preencha todos os campos")
            msg.exec()
        else:
            resp = db.inserir_produto(codigo, descprod, tipoprod, corprod, qntdprod, precoprod, data)

            resp2 = db.inserir_fornecedor(nome, endereco, cidade, bairro, uf, cep, cnpj, telefone)

            if resp and resp2 == "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Cadastro de Dados")
                msg.setText("Os dados foram cadastrados com sucesso")
                msg.exec()
                self.buscar_produtos()
                self.buscar_fornecedores()
                self.tv_pesquisa_estoque()
                self.txt_cod_prod.setText("")
                self.txt_desc_prod.setText("")
                self.txt_cor_prod.setText("")
                self.txt_qntd_prod.setText("")
                self.txt_preco_prod.setText("")
                self.txt_nome_forn.setText("")
                self.txt_end_forn.setText("")
                self.txt_cidade_forn.setText("")
                self.txt_bairro_forn.setText("")
                self.txt_cep_forn.setText("")
                self.txt_cnpj_forn.setText("")
                self.txt_tel_forn.setText("")
                db.desconectar()

            elif resp != "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Erro")
                msg.setText("Erro ao cadastrar os dados, verifique se as informações foram preenchidas corretamente!")
                msg.exec()
                self.buscar_produtos()
                self.buscar_fornecedores()
                self.tv_pesquisa_estoque()
                db.desconectar()

            elif resp2 != "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Cadastro de Dados")
                msg.setText("Os dados do produto foram cadastrados com sucesso, o fornecedor já está cadastrado")
                msg.exec()
                self.buscar_produtos()
                self.buscar_fornecedores()
                self.tv_pesquisa_estoque()
                self.txt_cod_prod.setText("")
                self.txt_desc_prod.setText("")
                self.txt_cor_prod.setText("")
                self.txt_qntd_prod.setText("")
                self.txt_preco_prod.setText("")
                self.txt_nome_forn.setText("")
                self.txt_end_forn.setText("")
                self.txt_cidade_forn.setText("")
                self.txt_bairro_forn.setText("")
                self.txt_cep_forn.setText("")
                self.txt_cnpj_forn.setText("")
                self.txt_tel_forn.setText("")
                db.desconectar()

    def buscar_produtos(self):
        db = Database()
        db.conectar()
        resultado = db.exibir_produtos()

        self.tw_estoque.clearContents()
        self.tw_estoque.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tw_estoque.setItem(row, column, QTableWidgetItem(str(data)))

        db.desconectar()

    def atualizar_produto(self):
        dados = []
        update_dados = []

        for row in range(self.tw_estoque.rowCount()):
            for column in range(self.tw_estoque.columnCount()):
                dados.append(self.tw_estoque.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Database()
        db.conectar()

        for produto in update_dados:
            db.alterar_produtos(tuple(produto))

        db.desconectar()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados do produto foram atualizados com sucesso!")
        msg.exec()

        self.tw_estoque.reset()
        self.buscar_produtos()
        self.tv_pesquisa_estoque()

    def excluir_produto(self):
        db = Database()
        db.conectar()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este produto será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.tw_estoque.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.deletar_produtos(codigo)
            self.buscar_produtos()
            self.tv_pesquisa_estoque()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Exclusão")
            msg.setText(result)
            msg.exec()

        db.desconectar()

    def buscar_fornecedores(self):
        db = Database()
        db.conectar()
        resultado = db.exibir_fornecedores()

        self.tw_fornecedores.clearContents()
        self.tw_fornecedores.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tw_fornecedores.setItem(row, column, QTableWidgetItem(str(data)))

        db.desconectar()

    def atualizar_fornecedor(self):
        dados = []
        update_dados = []

        for row in range(self.tw_fornecedores.rowCount()):
            for column in range(self.tw_fornecedores.columnCount()):
                dados.append(self.tw_fornecedores.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Database()
        db.conectar()

        for fornecedor in update_dados:
            db.alterar_fornecedores(tuple(fornecedor))

        db.desconectar()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados do fornecedor foram atualizados com sucesso!")
        msg.exec()

        self.tw_fornecedores.reset()
        self.buscar_fornecedores()

    def excluir_fornecedor(self):
        db = Database()
        db.conectar()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este fornecedor será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tw_fornecedores.selectionModel().currentIndex().siblingAtColumn(6).data()
            result = db.deletar_fornecedores(cnpj)
            self.buscar_fornecedores()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Exclusão")
            msg.setText(result)
            msg.exec()

        db.desconectar()

    def gerar_excel_produtos(self):
        dados = []
        todos_dados = []

        for row in range(self.tw_estoque.rowCount()):
            for column in range(self.tw_estoque.columnCount()):
                dados.append(self.tw_estoque.item(row, column).text())

            todos_dados.append(dados)
            dados = []

        columns = ["Código", "Descrição do Produto", "Tipo", "Cor", "Quantidade no Estoque", "Preço", "Data da Compra"]

        produtos = pd.DataFrame(todos_dados, columns=columns)
        produtos.to_excel("Estoque.xlsx", sheet_name="estoque", index=False)

        msg = QMessageBox()
        msg.setWindowTitle("Relatório")
        msg.setText("Relatório Excel do estoque gerado com sucesso!")
        msg.exec()

    def gerar_excel_fornecedores(self):
        dados = []
        todos_dados = []

        for row in range(self.tw_fornecedores.rowCount()):
            for column in range(self.tw_fornecedores.columnCount()):
                dados.append(self.tw_fornecedores.item(row, column).text())

            todos_dados.append(dados)
            dados = []

        columns = ["Nome", "Endereço", "Cidade", "Bairro", "UF", "CEP", "CNPJ", "Telefone"]

        fornecedores = pd.DataFrame(todos_dados, columns=columns)
        fornecedores.to_excel("Fornecedores.xlsx", sheet_name="fornecedores", index=False)

        msg = QMessageBox()
        msg.setWindowTitle("Relatório")
        msg.setText("Relatório Excel dos fornecedores gerado com sucesso!")
        msg.exec()

    def tv_pesquisa_estoque(self):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.modelo = QSqlTableModel(db=db)
        self.tv_pesquisa_prod.setModel(self.modelo)
        self.modelo.setTable("produtos")
        self.modelo.select()

    def filtro(self, pesquisa):
        pesquisa = re.sub("[\W_]+", "", pesquisa)
        filtro = 'codigo LIKE "%{}%"'.format(pesquisa)
        self.modelo.setFilter(filtro)

if __name__ == "__main__":
    db = Database()
    db.conectar()
    db.criar_tabela_usuarios()
    db.criar_tabela_produtos()
    db.criar_tabela_fornecedores()
    db.desconectar()

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()