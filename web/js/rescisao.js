$(document).ready(function(){
    eel.fetchalldatares();

    $("#btn_addres").on("click", async function(){ // Adicione a palavra-chave 'async' aqui
        $("#addresModal").modal("show");

        await eel.get_nome_rescisao()(); // Aguarde a função assíncrona corretamente
    });
});

eel.expose(action_outres);
function action_outres(rescisao){
    // Função chamada quando os dados de rescisão são recebidos do Python
    // Aqui você pode realizar as ações necessárias para exibir os dados na página
    rescisao.forEach(showRes);
}

// Função para preencher o campo de seleção com as opções
eel.expose(nomeOptions);
function nomeOptions(selected_nome) {
  var selectElement = document.getElementById("nomeInput");

  selected_nome.forEach(function (item) {
    var option = document.createElement("option");
    option.text = item;
    selectElement.add(option);
  });
}

// Editar Rescisão
async function btn_edit(id){
    // Função chamada quando o botão de edição é clicado
    // Aqui você pode realizar as ações necessárias para obter os dados do registro a ser editado
    await eel.get_rescisao(id)();
    $('#editresmodal').modal("show");
}

eel.expose(action_editres);
function action_editres(editrescisao){
    // Função chamada quando os dados do registro a ser editado são recebidos do Python
    // Aqui você pode realizar as ações necessárias para preencher o formulário de edição com os dados
    editrescisao.forEach(get_array_values);
}

function get_array_values(item, index){
    // Função auxiliar para obter os valores dos dados do registro e preencher o formulário de edição
    if (index == 0) {
        document.getElementById("editid").value = item;
    } else if (index == 1) {
        document.getElementById("editnomeInput").value = item;
    } else if (index == 2) {
        document.getElementById("editdataresInput").value = item;
    } else if (index == 3) {
        document.getElementById("editliquidoresInput").value = item;
    } else if (index == 4) {
        document.getElementById("editcarteiraresInput").value = item;
    } else if (index == 5) {
        document.getElementById("editmotivoInput").value = item;
    }
    else {}
}

async function save_edit_js(){
    // Função chamada quando o botão de salvar edição é clicado
    // Aqui você pode realizar as ações necessárias para obter os valores dos campos de edição e enviar ao Python para atualizar o registro
    if ($("#editresform").valid()) {
        const nomeedit = $('#editnomeInput').val();
        const dataresedit = $('#editdataresInput').val();
        const liquidoresedit = $('#editliquidoresInput').val();
        const carteiraresedit = $('#editcarteiraresInput').val();
        const motivoedit = $('#editmotivoInput').val();
        const editid = $('#editid').val();
        const result = await eel.btn_saveeditres(nomeedit, dataresedit, liquidoresedit, carteiraresedit, motivoedit, editid)();
        location.reload();
    }
}

function showRes(item, index){
    // Função para exibir os dados de um registro de rescisão na tabela da página
    var get_table = document.getElementById("rescisao");
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");
    var td4 = document.createElement("td");
    var td5 = document.createElement("td");
    var td6 = document.createElement("td");
    var td7 = document.createElement("td");

    var id = item[0]
    td.innerText = item[0]
    td1.innerText = item[1]
    td2.innerText = item[2]
    td3.innerText = item[3]
    td4.innerText = item[4]
    td5.innerText = item[5]

    var btnInfo = document.createElement("button");
    var btnDelete = document.createElement("button");
    var infoIcon = document.createElement("i");
    var deleteIcon = document.createElement("i");

    btnInfo.classList.add("btn", "btn-info", "btn-circle");
    btnInfo.setAttribute("type", "button");
    btnInfo.setAttribute("data-ripple-color", "dark");
    btnInfo.setAttribute("onclick", "btn_edit('" + id + "')");
    btnInfo.setAttribute("style", "margin:5px");

    btnDelete.classList.add("btn", "btn-danger", "btn-circle");
    btnDelete.setAttribute("type", "button");
    btnDelete.setAttribute("data-ripple-color", "dark");
    btnDelete.setAttribute("onclick", "btn_delete('" + id + "')");

    infoIcon.classList.add("fas", "fa-info-circle");
    deleteIcon.classList.add("fas", "fa-trash");

    btnInfo.appendChild(infoIcon);
    btnDelete.appendChild(deleteIcon);

    td6.appendChild(btnInfo);
    td6.appendChild(btnDelete);

    tr.appendChild(td);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tr.appendChild(td6);

    get_table.appendChild(tr);
}

// Nova Rescisão
async function save_res_js(){
    // Função chamada quando o botão de salvar nova rescisão é clicado
    // Aqui você pode realizar as ações necessárias para obter os valores dos campos de novo registro e enviar ao Python para salvar
    if ($("#formres").valid()) {
        const nome = $('#nomeInput').val();
        const datares = $('#dataresInput').val();
        const liquidores = $('#liquidoresInput').val();
        const carteirares = $('#carteiraresInput').val();
        const motivo = $('#motivoInput').val();
        const result = await eel.btn_saveres(nome, datares, liquidores, carteirares, motivo)();
        location.reload();
    }
}

eel.expose(save_returnres);
function save_returnres(status) {
    // Função chamada quando o retorno do salvamento da nova rescisão é recebido do Python
    // Aqui você pode exibir uma mensagem de sucesso ou erro na página com base no status recebido
    if (status == "sucess") {
        $('#return_register').text('Novo cadastro concluído com sucesso.');
        $('#empresaInput').val('');
        $('#setorInput').val('');
        $('#funcaoInput').val('');
        $('#liderInput').val('');
    }
    if (status == "failure") {
        $('#return_register').text('Erro ao cadastrar, verifique os campos em branco.');
    }
    if (status == "falhou") {
        $('#return_register').text('Erro ao cadastrar, contate o administrador.');
    }
}

//Deletar

let deleteRescisaoId; // Variável global para armazenar o ID do recisao a ser excluído

async function btn_delete(id) {
    $('#deleterecisaomodal').modal("show"); // Abre o modal de confirmação de exclusão
    deleteRescisaoId = await eel.get_delete_rescisao(id)(); // Obtém o ID do recisao a ser excluído usando a função exposta do lado do servidor
}

async function btn_submitdelete() {
    const response = await eel.delete_rescisao(deleteRescisaoId)(); // Exclui o rescisao usando o ID armazenado na variável deleteRescisaoId
    if (response === "success") {
        location.reload(); // Recarrega a página após a exclusão bem-sucedida
    } else {
        console.log("Erro ao excluir o setor."); // Exibe uma mensagem de erro caso ocorra algum problema na exclusão
    }
}