import eel
import pyautogui
from web.models.setor import showallrecords, save_newsetor
from web.models.admissao import showallrecordsadm, save_newadm
from web.models.rescisao import showallrecordsres, save_newres, show_selectedRescisao, update_res

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


"""ADMISSAO"""

@eel.expose
def fetchalldataadm():
    """
    Função que busca todos os registros na tabela de Admissão e exibe o resultado na interface.
    """
    select_reg = showallrecordsadm()
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


"""START"""

eel.start(
    'rescisao.html',
    size=pyautogui.size(),
)
