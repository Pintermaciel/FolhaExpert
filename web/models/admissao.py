import sqlite3

def showallrecordsadm():
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM admissao")
        admissao = []
        for item in cursor.fetchall():
            test = item[1]
            print(test)
            admissao.append(item)
        return admissao
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_newadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm):
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        
        if nome != "" and cpf != "" and empresa != "" and setor != "" and cargo != "" and salariof != "" and salario != "" and dataadm != "":
            cursor.execute("INSERT INTO admissao(nome, cpf, empresa, setor, cargo, salario_folha, salario, data_admissao) VALUES(?,?,?,?,?,?,?,?)", (nome,cpf,empresa,setor,cargo,salariof,salario,dataadm))
            connect.commit()
            connect.close()
            msg = "sucess"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "falhou"
        return msg