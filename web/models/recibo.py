from fpdf import FPDF
import sqlite3

def consultar_tabela_sql():
    # Conectar ao banco de dados
    connect = sqlite3.connect(r"/home/matheushmfp/Documentos/FolhaExpert1/web/databases/storage.db")
    cursor = connect.cursor()
    # Consulta SQL
    cursor.execute('''
        SELECT  nome,
                competencia,
                (SELECT salario FROM admissao a WHERE a.nome = c.nome) as salario, 
                hn,
                valor_inss,
                valor_irrf,
                outros_recebimentos,
                outros_descontos,
                he50,
                diasuteis,
                feriados,
                he65,
                he75
        FROM competencia c
        WHERE nome = "Matheus Henrique Pinter Maciel" AND competencia = "03/2023"
    ''')

    # Recuperar os resultados
    resultado = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    connect.close()

    return resultado

# Executar a consulta
resultado_consulta = consultar_tabela_sql()

class ReciboPDF(FPDF):
    def header(self):
        # Configurações do cabeçalho
        self.set_fill_color(53, 59, 72)  # Cor de fundo azul escuro
        self.set_text_color(255, 255, 255)  # Texto branco
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "MACROFRIO EQUIPAMENTOS E ISOLAMENTOS PARA REFRIGERAÇÃO LTDA", 0, 1, "C", fill=True)
        self.ln(8)
        self.set_font("Arial", "", 10)
        self.cell(0, 10, "Recibo de Pagamento", 0, 1, "C")
        self.ln(10)

    def footer(self):
        # Configurações do rodapé
        self.set_y(-15)
        self.set_font("Arial", "", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def add_table_row(self, descricao, base_calculo, vencimentos, descontos):
        # Verifica se a linha contém cabeçalhos
        if descricao == "DESCRIÇÃO" and base_calculo == "BASE CALCULO" and vencimentos == "VENCIMENTOS" and descontos == "DESCONTOS":
            return

        # Verifica se todas as colunas têm valor (non-zero)
        try:
            if float(base_calculo or 0) == 0 and float(vencimentos or 0) == 0 and float(descontos or 0) == 0:
                return
        except ValueError:
            return


        # Configurações da tabela
        self.set_fill_color(255, 255, 255)  # Fundo branco
        self.set_text_color(0, 0, 0)  # Texto preto
        self.set_font("Arial", "", 10)

        # Adiciona os valores na tabela
        self.cell(65, 8, descricao, 1, 0, "C", True)
        self.cell(40, 8, base_calculo or "", 1, 0, "C", True)
        self.cell(40, 8, vencimentos or "", 1, 0, "C", True)
        self.cell(40, 8, descontos or "", 1, 1, "C", True)

    def criar_recibo(self, nome, mes, tabela_valores, liquido_a_receber, valor_pago_deposito, valor_receber_carteira,
                     recebido_em, assinatura_legivel):
        # Configurações da página
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", "", 10)

        # Informações do recibo
        self.set_text_color(53, 59, 72)  # Texto azul escuro
        self.set_font("Arial", "B", 18)
        self.cell(0, 10, f"Recibo de Pagamento - {mes}", 0, 1, "C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Nome: {nome}", 0, 1, "C")
        self.ln(8)

        # Centraliza a tabela horizontalmente
        table_start_x = (self.w - 185) / 2  # 185 é a largura total das células da tabela
        self.set_x(table_start_x)

        # Tabela de valores
        self.set_fill_color(255, 255, 255)  # Fundo branco
        self.set_text_color(0, 0, 0)  # Texto preto
        self.set_font("Arial", "B", 12)

        # Adiciona as linhas na tabela
        self.cell(65, 8, "Descrição", 1, 0, "C", True)
        self.cell(40, 8, "Base Cálculo", 1, 0, "C", True)
        self.cell(40, 8, "Vencimentos", 1, 0, "C", True)
        self.cell(40, 8, "Descontos", 1, 1, "C", True)
        self.set_font("Arial", "", 10)
        for linha in tabela_valores:
            self.set_x(table_start_x)  # Centraliza horizontalmente a célula
            self.add_table_row(linha[0], linha[1], linha[2], linha[3])

        # Linha horizontal após a tabela
        self.set_x(table_start_x)  # Centraliza horizontalmente a célula
        self.cell(185, 0, "", "T")
        self.ln(8)

        # Outras informações
        self.set_text_color(53, 59, 72)  # Texto azul escuro
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Líquido a Receber: {liquido_a_receber}", 0, 1)
        self.cell(0, 10, f"Valor Pago por Depósito: {valor_pago_deposito}", 0, 1)
        self.cell(0, 10, f"Valor a Receber em Carteira: {valor_receber_carteira}", 0, 1)
        self.cell(0, 10, f"Recebido em: {recebido_em}", 0, 1)
        self.cell(0, 10, "Assinatura Legível:", 0, 1, "L")
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, assinatura_legivel, 0, 1, "L")
        
    def calcular_valor_por_hora(self, base_calculo, horas_mensais):
        try:
            base_calculo = float(base_calculo)
            horas_mensais = float(horas_mensais)
            if horas_mensais != 0:
                valor_por_hora = base_calculo / horas_mensais
                return round(valor_por_hora, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcular_valor_hr50(self, valor_hora, horas_50):
        try:
            valor_hora = float(valor_hora)
            horas_50 = float(horas_50)
            if valor_hora != 0:
                valor_he50 = valor_hora * horas_50 * 1.5
                return round(valor_he50, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcular_valor_dsr50(self, valorhe50, diasuteis, feriados):
        try:
            diasuteis = int(diasuteis)
            feriados = int(feriados)
            if valorhe50 != 0 and diasuteis != 0 and feriados != 0:
                valordsr50 = (valorhe50 / diasuteis) * feriados
                return round(valordsr50, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0

    def calcular_valor_hr65(self, valor_hora, horas_65):
        try:
            valor_hora = float(valor_hora)
            horas_65 = float(horas_65)
            if valor_hora != 0:
                valor_he65 = valor_hora * horas_65 * 1.65
                return round(valor_he65, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0

    def calcular_valor_dsr65(self, valorhe65, diasuteis, feriados):
        try:
            diasuteis = int(diasuteis)
            feriados = int(feriados)
            if valorhe65 != 0 and diasuteis != 0 and feriados != 0:
                valordsr65 = (valorhe65 / diasuteis) * feriados
                return round(valordsr65, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcular_valor_hr75(self, valor_hora, horas_75):
        try:
            valor_hora = float(valor_hora)
            horas_75 = float(horas_75)
            if valor_hora != 0:
                valor_he75 = valor_hora * horas_75 * 1.75
                return round(valor_he75, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0

    def calcular_valor_dsr65(self, valorhe65, diasuteis, feriados):
        try:
            diasuteis = int(diasuteis)
            feriados = int(feriados)
            if valorhe65 != 0 and diasuteis != 0 and feriados != 0:
                valordsr65 = (valorhe65 / diasuteis) * feriados
                return round(valordsr65, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0

# Exemplo de uso
pdf = ReciboPDF()
# Atribuir os valores obtidos às variáveis da função pdf.criar_recibo()
valor_por_hora = pdf.calcular_valor_por_hora(resultado_consulta[2], resultado_consulta[3])
valorhe50 = pdf.calcular_valor_hr50(valor_por_hora, resultado_consulta[8])
valordsr50 = pdf.calcular_valor_dsr50(valorhe50, resultado_consulta[9], resultado_consulta[10])
valorhe65 = pdf.calcular_valor_hr65(valor_por_hora, resultado_consulta[11])
valordsr65 = pdf.calcular_valor_dsr50(valorhe65, resultado_consulta[11], resultado_consulta[10])
valorhe75 = pdf.calcular_valor_hr75(valor_por_hora, resultado_consulta[12])
valordsr65 = pdf.calcular_valor_dsr50(valorhe65, resultado_consulta[11], resultado_consulta[10])


pdf.criar_recibo(
    nome=resultado_consulta[0],
    mes=resultado_consulta[1],
    tabela_valores=[
        ("DESCRIÇÃO", "BASE CALCULO", "VENCIMENTOS", "DESCONTOS"),
        ("SALÁRIO", str(resultado_consulta[2]), str(resultado_consulta[2]), ""),
        ("HORAS MENSAIS", str(resultado_consulta[3]), "", ""),
        ("VALOR POR HORA", str(valor_por_hora), "", ""),
        ("OUTROS RECEBIMENTOS", "", str(resultado_consulta[6]), ""),
        ("R$ INSS", "", "", str(resultado_consulta[4])),
        ("R$ IRRF", "", "", str(resultado_consulta[5])),
        ("OUTROS DESCONTOS EM FOLHA", "", "", str(resultado_consulta[7])),
        ("HORAS EXTRAS À 50%", str(resultado_consulta[8]), str(valorhe50), ""),
        ("DSR 50%", "", str(valordsr50), ""),
        ("HORAS EXTRAS À 65%", str(resultado_consulta[11]), str(valorhe65), ""),
        ("DSR 65%", "", str(valordsr65), ""),
        ("HORAS EXTRAS À 75%",str(resultado_consulta[12]), str(valorhe75), ""),
        ("DSR 75%", "", "", str(resultado_consulta[1])),
        ("HORAS EXTRAS À 100%", "", "", str(resultado_consulta[1])),
        ("DSR 100%", "", "", str(resultado_consulta[1])),
        ("TOTAL HORAS EXTRAS E DSR", "", "", ""), # linha que soma o total
        ("FALTAS EM DIAS", "", "", str(resultado_consulta[1])),
        ("FALTAS EM HORAS", "", "", str(resultado_consulta[1])),
        ("FALTA INJUSTIFICADA DSR SEMANAL", "", "", ""),
        ("CARTÃO ACIVALE", "", "", str(resultado_consulta[1])),
        ("FARMACIA", "", "", str(resultado_consulta[1])),
        ("VALE", "", "", ""),
        ("UNIMED", "", "", ""),
        ("DESP. UNIMED", "", "", ""),
        ("OS", "", "", str(resultado_consulta[1])),
        ("MARMITAS", "", "", str(resultado_consulta[1])),
        ("REMBOLSO DESP. VIAGENS", "", "", ""),
        ("MULTAS", "", "", str(resultado_consulta[1])),
        ("DESCONTO", "", "", str(resultado_consulta[1])),
        ("CAFÉ", "", "", str(resultado_consulta[1])),
        ("PLANTAO", "", "", str(resultado_consulta[1])),
        ("PENSAO", "", "", ""),
        ("DESLOCAMENTO", "", "", ""),
        ("FÉRIAS", "", "", ""),
        ("1/3 FÉRIAS", "", "", ""),
        ("TOTAL", "" , "", "")
    ],
    liquido_a_receber=str(resultado_consulta[1]),
    valor_pago_deposito=str(resultado_consulta[1]),
    valor_receber_carteira=str(resultado_consulta[1]),
    recebido_em="__________________",
    assinatura_legivel='''__________________________'''
)

pdf.output("recibo.pdf", "F")
