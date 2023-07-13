from fpdf import FPDF


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
        # Verifica se todas as colunas têm valor
        if not (base_calculo or vencimentos or descontos):
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

    def criar_recibo(self, nome, mes, tabela_valores, total, liquido_a_receber, valor_pago_deposito, valor_receber_carteira,
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

        # Centraliza a célula de total
        self.set_x(table_start_x)  # Centraliza horizontalmente a célula
        self.set_font("Arial", "B", 12)
        self.cell(130, 8, "TOTAL", 1, 0, "C", True)
        self.cell(40, 8, total, 1, 1, "R", True)
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



# Exemplo de uso
pdf = ReciboPDF()
pdf.criar_recibo(
    nome="Vinicius Roden Alberton",
    mes="Julho 2023",
    tabela_valores=[
        ("DESCRIÇÃO", "BASE CALCULO", "VENCIMENTOS", "DESCONTOS"),
        ("SALÁRIO", "2.262,00", "2.262,00", ""),
        ("HORAS MENSAIS", "220,00", "", ""),
        ("VALOR POR HORA", "10,28", "", ""),
        ("R$ INSS", None, None, None),
        ("R$ IRRF", None, None, None),
        ("OUTROS RECEBIMENTOS", None, None, None),
        ("OUTROS DESCONTOS EM FOLHA", None, None, None),
        ("HORAS EXTRAS À 50%", "6,00", "", "92,54"),
        ("DSR 50%", "", "", "#REF!"),
        ("HORAS EXTRAS À 65%", "1,85", "", "31,39"),
        ("DSR 65%", "", "", "#REF!"),
        ("HORAS EXTRAS À 75%", None, None, None),
        ("DSR 75%", "", "", "#REF!"),
        ("HORAS EXTRAS À 100%", None, None, None),
        ("DSR 100%", "", "", "#REF!"),
        ("TOTAL HORAS EXTRAS E DSR", "7,85", "", "#REF!"),
        ("FALTAS EM DIAS", None, None, None),
        ("FALTAS EM HORAS", None, None, None),
        ("FALTA INJUSTIFICADA DSR SEMANAL", None, None, None),
        ("CARTÃO ACIVALE", None, None, None),
        ("FARMACIA", None, None, None),
        ("VALE", None, None, None),
        ("UNIMED", None, None, None),
        ("DESP. UNIMED", None, None, None),
        ("OS", "14,85", "", ""),
        ("MARMITAS", None, None, None),
        ("REMBOLSO DESP. VIAGENS", None, None, None),
        ("MULTAS", None, None, None),
        ("DESCONTO", None, None, None),
        ("CAFÉ", "10,00", "", ""),
        ("PLANTAO", None, None, None),
        ("PENSAO", None, None, None),
        ("DESLOCAMENTO", None, None, None),
        ("FÉRIAS", None, None, None),
        ("1/3 FÉRIAS", None, None, None),
    ],
    total="#REF!",
    liquido_a_receber="#REF!",
    valor_pago_deposito="1.653,00",
    valor_receber_carteira="#REF!",
    recebido_em="#REF!",
    assinatura_legivel=""
)

pdf.output("recibo.pdf", "F")
