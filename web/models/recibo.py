from fpdf import FPDF
import sqlite3
import os
from pathlib import Path

def consultar_tabela_sql(nome, competencia):
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
                he75,
                he100,
                faltadias,
                faltahora,
                cartao_acivale,
                farmacia,
                unimed,
                desp_unimed,
                os,
                marmita,
                reb_desp_viagens,
                multas,
                cafe,
                plantao,
                pensao,
                deslocamento,
                valor_pag_deposito
        FROM competencia c
        WHERE nome = ? AND competencia = ?
    ''', (nome, competencia))

    # Recuperar os resultados
    resultado = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    connect.close()

    return resultado

class ReciboPDF(FPDF):
    def header(self):
        # Configurações do cabeçalho
        self.set_fill_color(53, 59, 72)  # Cor de fundo azul escuro
        self.set_text_color(255, 255, 255)  # Texto branco
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "MACROFRIO EQUIPAMENTOS E ISOLAMENTOS PARA REFRIGERAÇÃO LTDA", 0, 1, "C", fill=True)
        self.ln(8)
        
        
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

    def calcular_valor_dsr75(self, valorhe75, diasuteis, feriados):
        try:
            diasuteis = int(diasuteis)
            feriados = int(feriados)
            if valorhe75 != 0 and diasuteis != 0 and feriados != 0:
                valordsr75 = (valorhe75 / diasuteis) * feriados
                return round(valordsr75, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcular_valor_hr100(self, valor_hora, horas_100):
        try:
            valor_hora = float(valor_hora)
            horas_100 = float(horas_100)
            if valor_hora != 0:
                valor_he100 = valor_hora * horas_100 * 2.0
                return round(valor_he100, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0

    def calcular_valor_dsr100(self, valorhe100, diasuteis, feriados):
        try:
            diasuteis = int(diasuteis)
            feriados = int(feriados)
            if valorhe100 != 0 and diasuteis != 0 and feriados != 0:
                valordsr100 = (valorhe100 / diasuteis) * feriados
                return round(valordsr100, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcular_total_he(self, horas_50, horas_65, horas_75, horas_100):
        try:
            horas_50 = float(horas_50)
            horas_65 = float(horas_65)
            horas_75 = float(horas_75)
            horas_100 = float(horas_100)
            if horas_50 != 0:
                total_he = horas_50 + horas_65 + horas_75 + horas_100
                return float(total_he)
            else:
                return 0
        except ValueError:
            return 0
        
    def calcular_valor_total_he(self, horas_50, horas_65, horas_75, horas_100, dsr50, dsr65, dsr75, dsr100):
        try:
            horas_50 = float(horas_50)
            horas_65 = float(horas_65)
            horas_75 = float(horas_75)
            horas_100 = float(horas_100)
            dsr50 = float(dsr50)
            dsr65 = float(dsr65)
            dsr75 = float(dsr75)
            dsr100 = float(dsr100)
            if horas_50 != 0 or horas_65 != 0 or horas_75 != 0 or horas_100 != 0:
                total_valor_he = horas_50 + horas_65 + horas_75 + horas_100 + dsr50 + dsr65 + dsr75 + dsr100
                return float(total_valor_he)
            else:
                return 0
        except ValueError:
            return 0
            
    def calcula_valor_fdias(self, faltadias, valor_hora):
        try:
            faltadias = int(faltadias)
            valor_hora = float(valor_hora)
            hora_dia = 7.33
            horas_f = (faltadias * hora_dia)
            if faltadias != 0:
                valor_fdias = horas_f * valor_hora
                return round(valor_fdias, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcula_valor_fhora(self, faltahora, valor_hora):
        try:
            faltahora = float(faltahora)
            valor_hora = float(valor_hora)
            if faltahora != 0:
                valor_fhora = faltahora * valor_hora
                return round(valor_fhora, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcula_valor_fhora(self, faltahora, valor_hora):
        try:
            faltahora = float(faltahora)
            valor_hora = float(valor_hora)
            if faltahora != 0:
                valor_fhora = faltahora * valor_hora
                return round(valor_fhora, 2)  # Arredonda para 2 casas decimais
            else:
                return 0
        except ValueError:
            return 0
        
    def calcula_total_vencimentos(self, salario, outrosrecebimentos, totalvalorhe, reembolso_desp_viagens):
        try:
            salario = float(salario)
            totalvalorhe = float(totalvalorhe)
            reembolso_desp_viagens = float(reembolso_desp_viagens)
            
            totalvencimentos = salario + totalvalorhe + reembolso_desp_viagens
            return round(totalvencimentos, 2)  # Arredonda para 2 casas decimais
        except ValueError:
            return 0
        
    def calcula_total_descontos(self, inss, irrf, outros_descontos_folha, valorfdias, valorfhora, cacivale, farmacia, unimed, desp_unimed, os, marmita, multas, cafe, plantao, pensao, deslocamento):
        try:
            # Calculate the sum of all the provided discounts
            total_descontos = float(inss) + float(irrf) + float(outros_descontos_folha) + float(valorfdias) + float(valorfhora) + float(cacivale) + float(farmacia) + float(unimed) + float(desp_unimed) + float(os) + float(marmita) + float(multas) + float(cafe) + float(plantao) + float(pensao) + float(deslocamento)
            return round(total_descontos, 2)  # Round to 2 decimal places

        except TypeError:  # Catching potential type errors
            return 0


    def calcula_liquido_receber(self, total_vencimentos, total_descontos):
        try:
            total_vencimentos = float(total_vencimentos)
            total_descontos = float(total_descontos)
            liquido_receber = total_vencimentos - total_descontos
            return round(liquido_receber, 2)  # Round to 2 decimal places
        except ValueError:
            return 0
        
    def calcula_carteira_receber(self, liquido_receber, valor_pago_deposito):
        try:
            liquido_receber = float(liquido_receber)
            valor_pago_deposito = float(valor_pago_deposito)
            carteira_receber = liquido_receber - valor_pago_deposito
            return round(carteira_receber, 2)  # Round to 2 decimal places
        except ValueError:
            return 0
        
        

def gerar_recibo(nome, competencia):
    # Executar a consulta
    resultado_consulta = consultar_tabela_sql(nome, competencia)
    pdf = ReciboPDF()
    # Atribuir os valores obtidos às variáveis da função pdf.criar_recibo()
    valor_por_hora = pdf.calcular_valor_por_hora(resultado_consulta[2], resultado_consulta[3])
    valorhe50 = pdf.calcular_valor_hr50(valor_por_hora, resultado_consulta[8])
    valordsr50 = pdf.calcular_valor_dsr50(valorhe50, resultado_consulta[9], resultado_consulta[10])
    valorhe65 = pdf.calcular_valor_hr65(valor_por_hora, resultado_consulta[11])
    valordsr65 = pdf.calcular_valor_dsr65(valorhe65, resultado_consulta[9], resultado_consulta[10])
    valorhe75 = pdf.calcular_valor_hr75(valor_por_hora, resultado_consulta[12])
    valordsr75 = pdf.calcular_valor_dsr75(valorhe75, resultado_consulta[9], resultado_consulta[10])
    valorhe100 = pdf.calcular_valor_hr100(valor_por_hora, resultado_consulta[13])
    valordsr100 = pdf.calcular_valor_dsr100(valorhe100, resultado_consulta[9], resultado_consulta[10])
    totalhe = pdf.calcular_total_he(resultado_consulta[8], resultado_consulta[11], resultado_consulta[12], resultado_consulta[13])
    totalvalorhe = pdf.calcular_valor_total_he(valorhe50, valorhe65, valorhe75, valorhe100, valordsr50, valordsr65, valordsr75, valordsr100)
    valorfdias = pdf.calcula_valor_fdias(resultado_consulta[14], valor_por_hora)
    valorfhora = pdf.calcula_valor_fhora(resultado_consulta[15], valor_por_hora)
    totalvencimentos = pdf.calcula_total_vencimentos(resultado_consulta[2], resultado_consulta[6], totalvalorhe, resultado_consulta[22])
    total_descontos = pdf.calcula_total_descontos(resultado_consulta[4],
                                                    resultado_consulta[5],
                                                    resultado_consulta[7],
                                                    valorfdias,
                                                    valorfhora,
                                                    resultado_consulta[16],
                                                    resultado_consulta[17],
                                                    resultado_consulta[18],
                                                    resultado_consulta[19],
                                                    resultado_consulta[20],
                                                    resultado_consulta[21],
                                                    resultado_consulta[23],
                                                    resultado_consulta[24],
                                                    resultado_consulta[25],
                                                    resultado_consulta[26],
                                                    resultado_consulta[27])
    liquido_receber = pdf.calcula_liquido_receber(totalvencimentos, total_descontos)
    carteira_receber = pdf.calcula_carteira_receber(liquido_receber, resultado_consulta[28])

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
            ("DSR 75%", "", str(valordsr75), ""),
            ("HORAS EXTRAS À 100%", str(resultado_consulta[13]), str(valorhe100), ""),
            ("DSR 100%", "", str(valordsr100), ""),
            ("TOTAL HORAS EXTRAS E DSR", str(totalhe), str(totalvalorhe), ""), 
            ("FALTAS EM DIAS", str(resultado_consulta[14]), "", str(valorfdias)),
            ("FALTAS EM HORAS", str(resultado_consulta[15]), "", str(valorfhora)),
            ("FALTA INJUSTIFICADA DSR SEMANAL", str(resultado_consulta[14]), "", str(valorfdias)),
            ("CARTÃO ACIVALE", "", "", str(resultado_consulta[16])),
            ("FARMACIA", "", "", str(resultado_consulta[17])),
            ("VALE", "", "", ""),
            ("UNIMED", "", "", str(resultado_consulta[18])),
            ("DESP. UNIMED", "", "", str(resultado_consulta[19])),
            ("OS", "", "", str(resultado_consulta[20])),
            ("MARMITAS", "", "", str(resultado_consulta[21])),
            ("REMBOLSO DESP. VIAGENS", "", str(resultado_consulta[22]), ""),
            ("MULTAS", "", "", str(resultado_consulta[23])),
            ("CAFÉ", "", "", str(resultado_consulta[24])),
            ("PLANTAO", "", "", str(resultado_consulta[25])),
            ("PENSAO", "", "", str(resultado_consulta[26])),
            ("DESLOCAMENTO", "", "", str(resultado_consulta[27])),
            ("FÉRIAS", "", "", ""),
            ("1/3 FÉRIAS", "", "", ""),
            ("TOTAL", "" , str(totalvencimentos), str(total_descontos))
        ],
        liquido_a_receber=str(liquido_receber),
        valor_pago_deposito=str(resultado_consulta[28]),
        valor_receber_carteira=str(carteira_receber),
        recebido_em="__________________",
        assinatura_legivel='''__________________________'''
    )

    nome = resultado_consulta[0]
    mes = resultado_consulta[1]
    print(nome, mes)
    # Obtenha o caminho para a pasta "Downloads" do cliente
    pasta_downloads = os.path.expanduser("~/Downloads")

    # Crie a pasta "recibos" dentro da pasta "Downloads" (caso não exista)
    pasta_recibos = os.path.join(pasta_downloads, "recibos")
    if not os.path.exists(pasta_recibos):
        os.makedirs(pasta_recibos)

    # Substitua o caractere "/" por "-"
    nome_arquivo = f"recibo_{nome.replace(' ', '_')}_{mes.replace('/', '-')}.pdf"
    caminho_arquivo = os.path.join(pasta_recibos, nome_arquivo)

    # Salve o PDF na pasta "recibos"
    pdf.output(caminho_arquivo, "F")
