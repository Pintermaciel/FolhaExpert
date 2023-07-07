import eel
import pyautogui
from web.models.setor import showallrecords, save_newsetor, show_selectedSetor, update_setor, show_selectedeleteSetor, show_deleteSetor
from web.models.admissao import showallrecordsadm, save_newadm, show_selectedAdmissao, update_adm, show_selectedeleteAdmissao, show_deleteAdmissao, show_selectedEmpAdmissao, show_selectedSetorAdmissao, show_selectedCargoAdmissao
from web.models.rescisao import showallrecordsres, save_newres, show_selectedRescisao, update_res, show_selectedeleteRescisao, show_deleteRescisao, show_selectedNomeRescisao
from web.models.competencia import showallrecordscompetencia, save_newcomp, show_selectedCompetencia, show_selectedeleteCompetencia, show_deleteCompetencia
from web.models.horas import showallrecordshrs, show_selectedhrs, update_horas
from web.models.convenios import showallrecordsconv, show_selectedconv, update_conv
from web.models.descontos import showallrecordsdesc, show_selecteddesc, update_desc
import sys

# Set sys.stdout and sys.stderr to writable objects
sys.stdout = open('stdout.log', 'w')
sys.stderr = open('stderr.log', 'w')


eel.init('web')

"""SETOR"""

@eel.expose
def fetchalldata():
    """
    Função que busca todos os registros na tabela de Setor e exibe o resultado na interface.
    """
    select_reg = showallrecords()
    eel.action_out(select_reg)

@eel.expose
def btn_save(empresa, setor, funcao, lider):
    """
    Função que salva um novo registro de Setor no banco de dados.

    Args:
        empresa (str): Nome da empresa.
        setor (str): Nome do setor.
        funcao (str): Função do setor.
        lider (str): Líder do setor.
    """
    print("Chamando a função btn_save")
    msg = save_newsetor(empresa, setor, funcao, lider)
    eel.save_returnsetor(str(msg))
    
@eel.expose
def get_setor(id):
    """
    Função que busca um registro de Admissão pelo ID e exibe os dados na interface de edição.

    Args:
        id (int): ID do registro de Admissão.
    """
    selected_adm = show_selectedSetor(id)
    eel.action_editsetor(selected_adm)

@eel.expose
def save_editsetor(empresa, setor, funcao, lider, id):
    """
    Atualiza um registro de admissão existente no banco de dados.

    Args:
        empresa (str): Novo nome da empresa.
        setor (str): Novo setor do funcionário.
        funcao (str): Nova função do funcionário.
        lider (str): Novo líder do setor.
        id (int): ID do registro de admissão a ser atualizado.
    """
    print("Chamando a função save_editsetor")
    msg = update_setor(empresa, setor, funcao, lider, id)

@eel.expose
def get_delete_setor(id):
    """
    Função exposta para obter o setor a ser excluído com base no ID fornecido.

    Args:
        id: O ID do setor a ser excluído.

    Returns:
        int or None: O ID do setor a ser excluído ou None se o setor não existir.
    """
    select_del_setor = show_selectedeleteSetor(id)
    print(id)
    return select_del_setor

@eel.expose
def delete_setor(id):
    """
    Função exposta para excluir um setor com base no ID fornecido.

    Args:
        id: O ID do setor a ser excluído.

    Returns:
        str: Uma mensagem indicando o resultado da exclusão ("success" em caso de sucesso, "Error" em caso de erro).
    """
    result = show_deleteSetor(id)
    return result

"""ADMISSAO"""

@eel.expose
def fetchalldataadm():
    """
    Função que busca todos os registros na tabela de Admissão e exibe o resultado na interface.
    """
    select_reg = showallrecordsadm()
    print(select_reg)
    eel.action_outadm(select_reg)

@eel.expose
def btn_saveadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm):
    """
    Função que salva um novo registro de Admissão no banco de dados.

    Args:
        nome (str): Nome do funcionário.
        cpf (str): CPF do funcionário.
        empresa (str): Nome da empresa.
        setor (str): Nome do setor.
        cargo (str): Cargo do funcionário.
        salariof (float): Salário fixo.
        salario (float): Salário atual.
        dataadm (str): Data de admissão.
    """
    print("Chamando a função btn_save")
    msg = save_newadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm)
    eel.save_returnadm(str(msg))

@eel.expose
def get_admissao(id):
    """
    Função que busca um registro de Admissão pelo ID e exibe os dados na interface de edição.

    Args:
        id (int): ID do registro de Admissão.
    """
    selected_adm = show_selectedAdmissao(id)
    eel.action_editadm(selected_adm)
    
@eel.expose
def get_emp_admissao():
    """
    Obtém a empresa de admissão selecionada e envia as opções para o frontend.
    """
    selected_adm = show_selectedEmpAdmissao()
    print(selected_adm)
    eel.empresaOptions(selected_adm)

@eel.expose
def get_setor_admissao(empresa):
    """
    Obtém a empresa selecionada e retorna as opções de setor relacionadas para o frontend.
    
    Args:
        empresa: A empresa selecionada.
    """
    selected_setor = show_selectedSetorAdmissao(empresa)
    print(selected_setor)
    eel.setorOptions(selected_setor)

@eel.expose
def get_cargo_admissao(setor):
    """
    Obtém o setor selecionado e retorna as opções de cargo relacionadas para o frontend.
    
    Args:
        setor: O setor selecionado.
    """
    selected_cargo = show_selectedCargoAdmissao(setor)
    print(selected_cargo)
    eel.cargoOptions(selected_cargo)

@eel.expose
def save_editadm(nomeedit, cpfedit, empresaedit, setoredit, cargoedit, salariofedit, salarioedit, dataadmedit, editid):
    """
    Função que atualiza um registro de Admissão no banco de dados.

    Args:
        nomeedit (str): Novo nome do funcionário.
        cpfedit (str): Novo CPF do funcionário.
        empresaedit (str): Nova empresa.
        setoredit (str): Novo setor.
        cargoedit (str): Novo cargo.
        salariofedit (float): Novo salário fixo.
        salarioedit (float): Novo salário.
        dataadmedit (str): Nova data de admissão.
        editid (int): ID do registro de Admissão a ser atualizado.
    """
    print("Chamando a função btn_saveeditadm")
    msg = update_adm(nomeedit, cpfedit, empresaedit, setoredit, cargoedit, salariofedit, salarioedit, dataadmedit, editid)
    
@eel.expose
def get_delete_admissao(id):
    """
    Função exposta para obter o admissao a ser excluído com base no ID fornecido.

    Args:
        id: O ID do admissao a ser excluído.

    Returns:
        int or None: O ID do admissao a ser excluído ou None se o admissao não existir.
    """
    select_del_admissao = show_selectedeleteAdmissao(id)
    print(id)
    return select_del_admissao

@eel.expose
def delete_admissao(id):
    """
    Função exposta para excluir um admissao com base no ID fornecido.

    Args:
        id: O ID do admissao a ser excluído.

    Returns:
        str: Uma mensagem indicando o resultado da exclusão ("success" em caso de sucesso, "Error" em caso de erro).
    """
    result = show_deleteAdmissao(id)
    return result


"""RESCISAO"""

@eel.expose
def fetchalldatares():
    """
    Função que busca todos os registros na tabela de Rescisão e exibe o resultado na interface.
    """
    select_reg = showallrecordsres()
    eel.action_outres(select_reg)

@eel.expose
def btn_saveres(nome, datares, liquidores, carteirares, motivo):
    """
    Função que salva um novo registro de Rescisão no banco de dados.

    Args:
        nome (str): Nome do funcionário.
        datares (str): Data de rescisão.
        liquidores (float): Valor líquido da rescisão.
        carteirares (str): Número da carteira de rescisão.
        motivo (str): Motivo da rescisão.
    """
    print("Chamando a função btn_save")
    msg = save_newres(nome, datares, liquidores, carteirares, motivo)
    eel.save_returnres(str(msg))

@eel.expose
def get_rescisao(id):
    """
    Função que busca um registro de Rescisão pelo ID e exibe os dados na interface.

    Args:
        id (int): ID do registro de Rescisão.
    """
    selected_rescisao = show_selectedRescisao(id)
    eel.action_editres(selected_rescisao)

@eel.expose
def btn_saveeditres(nomeedit, dataresedit, liquidoresedit, carteiraresedit, motivoedit, editid):
    """
    Função que atualiza um registro de Rescisão no banco de dados.

    Args:
        nomeedit (str): Novo nome do funcionário.
        dataresedit (str): Nova data de rescisão.
        liquidoresedit (float): Novo valor líquido da rescisão.
        carteiraresedit (str): Novo número da carteira de rescisão.
        motivoedit (str): Novo motivo da rescisão.
        editid (int): ID do registro de Rescisão a ser atualizado.
    """
    print("Chamando a função btn_saveeditres")
    msg = update_res(nomeedit, dataresedit, liquidoresedit, carteiraresedit, motivoedit, editid)

@eel.expose
def get_delete_rescisao(id):
    """
    Função exposta para obter a rescisao a ser excluído com base no ID fornecido.

    Args:
        id: O ID do rescisao a ser excluído.

    Returns:
        int or None: O ID do rescisao a ser excluído ou None se o rescisao não existir.
    """
    select_del_rescisao = show_selectedeleteRescisao(id)
    print(id)
    return select_del_rescisao

@eel.expose
def delete_rescisao(id):
    """
    Função exposta para excluir um recisao com base no ID fornecido.

    Args:
        id: O ID do rescisao a ser excluído.

    Returns:
        str: Uma mensagem indicando o resultado da exclusão ("success" em caso de sucesso, "Error" em caso de erro).
    """
    result = show_deleteRescisao(id)
    return result

@eel.expose
def get_nome_rescisao():
    """
    Obtém o nome de rescisão selecionado e envia as opções para o frontend.
    """
    selected_adm = show_selectedNomeRescisao()
    print(selected_adm)
    eel.nomeOptions(selected_adm)

"""COMPETENCIA"""

@eel.expose
def fetchalldatacompetencia():
    """
    Função que busca todos os registros na tabela de Competencia e exibe o resultado na interface.
    """
    select_reg = showallrecordscompetencia()
    print(select_reg)
    eel.action_outCompetencia(select_reg)

@eel.expose
def btn_savecomp(comp, dias, feriados):
    """
    Função que salva um novo registro de Admissão no banco de dados.

    Args:
        nome (str): Nome do funcionário.
        cpf (str): CPF do funcionário.
        empresa (str): Nome da empresa.
        setor (str): Nome do setor.
        cargo (str): Cargo do funcionário.
        salariof (float): Salário fixo.
        salario (float): Salário atual.
        dataadm (str): Data de admissão.
    """
    print("Chamando a função btn_save")
    msg = save_newcomp(comp, dias, feriados)

@eel.expose
def get_competencia(id):
    """
    Função que busca um registro de Admissão pelo ID e exibe os dados na interface de edição.

    Args:
        id (int): ID do registro de Admissão.
    """
    selected_comp = show_selectedCompetencia(id)
    eel.action_editcomp(selected_comp)

@eel.expose
def get_delete_competencia(id):
    """
    Função exposta para obter o admissao a ser excluído com base no ID fornecido.

    Args:
        id: O ID do admissao a ser excluído.

    Returns:
        int or None: O ID do admissao a ser excluído ou None se o admissao não existir.
    """
    select_del_admissao = show_selectedeleteCompetencia(id)
    print(id)
    return select_del_admissao

@eel.expose
def delete_competencia(id):
    """
    Função exposta para excluir um admissao com base no ID fornecido.

    Args:
        id: O ID do admissao a ser excluído.

    Returns:
        str: Uma mensagem indicando o resultado da exclusão ("success" em caso de sucesso, "Error" em caso de erro).
    """
    result = show_deleteCompetencia(id)
    return result

"""HORAS"""

@eel.expose
def fetchalldatahrs():
    """
    Função que busca todos os registros na tabela de Competencia e exibe o resultado na interface.
    """
    select_reg = showallrecordshrs()
    print(select_reg)
    eel.action_outhrs(select_reg)

@eel.expose
def get_hrs(id):
    """
    Função que busca um registro de Admissão pelo ID e exibe os dados na interface de edição.

    Args:
        id (int): ID do registro de Admissão.
    """
    selected_comp = show_selectedhrs(id)
    eel.action_edithrs(selected_comp)
    
@eel.expose
def save_edithoras(editnome, editcompetencia, edithn, edithe50, edithe65, edithe75, edithe100, editfaltadias, editfaltahora, editid):
    """
    Função que atualiza um registro de Admissão no banco de dados.

    Args:
        nomeedit (str): Novo nome do funcionário.
        cpfedit (str): Novo CPF do funcionário.
        empresaedit (str): Nova empresa.
        setoredit (str): Novo setor.
        cargoedit (str): Novo cargo.
        salariofedit (float): Novo salário fixo.
        salarioedit (float): Novo salário.
        dataadmedit (str): Nova data de admissão.
        editid (int): ID do registro de Admissão a ser atualizado.
    """
    print("Chamando a função btn_saveeditadm")
    msg = update_horas(editnome, editcompetencia, edithn, edithe50, edithe65, edithe75, edithe100, editfaltadias, editfaltahora, editid)

"""CONVENIOS"""

@eel.expose
def fetchalldataconv():
    """
    Função que busca todos os registros na tabela de Competencia e exibe o resultado na interface.
    """
    select_reg = showallrecordsconv()
    print(select_reg)
    eel.action_outconv(select_reg)

@eel.expose
def get_conv(id):
    """
    Função que busca um registro de Admissão pelo ID e exibe os dados na interface de edição.

    Args:
        id (int): ID do registro de Admissão.
    """
    selected_comp = show_selectedconv(id)
    eel.action_editconv(selected_comp)
    
@eel.expose
def save_editconv(editnome, editcompetencia, editcartaoacivale, editunimed, editdesp_unimed, editfarmacia, editid):
    """
    Função que atualiza um registro de Admissão no banco de dados.

    Args:
        nomeedit (str): Novo nome do funcionário.
        cpfedit (str): Novo CPF do funcionário.
        empresaedit (str): Nova empresa.
        setoredit (str): Novo setor.
        cargoedit (str): Novo cargo.
        salariofedit (float): Novo salário fixo.
        salarioedit (float): Novo salário.
        dataadmedit (str): Nova data de admissão.
        editid (int): ID do registro de Admissão a ser atualizado.
    """
    print("Chamando a função btn_saveeditadm")
    msg = update_conv(editnome, editcompetencia, editcartaoacivale, editunimed, editdesp_unimed, editfarmacia, editid)
    
"""DESCONTOS"""

@eel.expose
def fetchalldatadesc():
    """
    Função que busca todos os registros na tabela de Competencia e exibe o resultado na interface.
    """
    select_reg = showallrecordsdesc()
    print(select_reg)
    eel.action_outdesc(select_reg)
    
@eel.expose
def get_desc(id):
    """
    Função que busca um registro de Admissão pelo ID e exibe os dados na interface de edição.

    Args:
        id (int): ID do registro de Admissão.
    """
    selected_comp = show_selecteddesc(id)
    eel.action_editdesc(selected_comp)
    
@eel.expose
def save_editdesc(editnome, editcompetencia, editcartaoacivale, editunimed, editdesp_unimed, editfarmacia, editid):
    """
    Função que atualiza um registro de Admissão no banco de dados.

    Args:
        editnome (str): Novo nome do funcionário.
        editcompetencia (str): Nova competência.
        editcartaoacivale (str): Novo valor do cartão Acivale.
        editunimed (str): Novo valor do Unimed.
        editdesp_unimed (str): Nova despesa da Unimed.
        editfarmacia (str): Novo valor da farmácia.
        editid (int): ID do registro de Admissão a ser atualizado.
    """
    print("Chamando a função save_editdesc")
    msg = update_desc(editnome, editcompetencia, editcartaoacivale, editunimed, editdesp_unimed, editfarmacia, editid)

"""START"""

eel.start(
    'competencia.html',
    size=pyautogui.size(),
)
