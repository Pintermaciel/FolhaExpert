import sqlite3

def showallrecordsres():
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM rescisao")
        recisao = []
        for item in cursor.fetchall():
            test = item[1]
            print(test)
            recisao.append(item)
        return recisao
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_newres(nome, datares, liquidores, carteirares, motivo):
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        
        if nome != "" and datares != "" and liquidores != "" and carteirares != "" and motivo != "":
            cursor.execute("INSERT INTO rescisao(nome, datares, liquidores, carteirares, motivo) VALUES(?,?,?,?,?)", (nome,datares,liquidores,carteirares,motivo))
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