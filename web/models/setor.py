import sqlite3

def showallrecords():
    try:
        connect = sqlite3.connect(r"C:\\Users\\pinte\\OneDrive\\Área de Trabalho\\FolhaExpert\\web\\databases\\storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM setor")
        setor = []
        for item in cursor.fetchall():
            test = item[1]
            print(test)
            setor.append(item)
        return setor
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_newsetor(empresa, setor, funcao, lider):
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        
        if empresa != "" and setor != "" and funcao != "" and lider != "":
            cursor.execute("INSERT INTO setor(empresa, setor, funcao, lider) VALUES(?,?,?,?)", (empresa,setor,funcao,lider))
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