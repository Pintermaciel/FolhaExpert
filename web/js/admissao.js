$(document).ready(function(){
    eel.fetchalldataadm()

    $("#btn_addadm").on("click", function(){
        $("#addadmModal").modal("show");
    });
})

eel.expose(action_outadm)
function action_outadm(adm){
    // Função chamada quando os dados de admissão são recebidos do Python
    // Aqui você pode realizar as ações necessárias para exibir os dados na página
    adm.forEach(showAdm)
}

function showAdm(item, index){
    // Função para exibir os dados de um registro de admissão na tabela da página
    var get_table = document.getElementById("adm");
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");
    var td4 = document.createElement("td");
    var td5 = document.createElement("td");
    var td6 = document.createElement("td");
    var td7 = document.createElement("td");
    var td8 = document.createElement("td");
    var td9 = document.createElement("td");

    var id = item[0]
    td.innerText = item[0]
    td1.innerText = item[1]
    td2.innerText = item[2]
    td3.innerText = item[3]
    td4.innerText = item[4]
    td5.innerText = item[5]
    td6.innerText = item[6]
    td7.innerText = item[7]
    td8.innerText = item[8]

    var btnInfo = document.createElement("button");
    var btnDelete = document.createElement("button");
    var infoIcon = document.createElement("i");
    var deleteIcon = document.createElement("i");

    btnInfo.classList.add("btn", "btn-info", "btn-circle");
    btnInfo.setAttribute("type", "button");
    btnInfo.setAttribute("data-ripple-color", "dark");
    btnInfo.setAttribute("onclick", "btn_edit('" + id + "')");

    btnDelete.classList.add("btn", "btn-danger", "btn-circle");
    btnDelete.setAttribute("type", "button");
    btnDelete.setAttribute("data-ripple-color", "dark");

    infoIcon.classList.add("fas", "fa-info-circle");
    deleteIcon.classList.add("fas", "fa-trash");

    btnInfo.appendChild(infoIcon);
    btnDelete.appendChild(deleteIcon);

    td9.appendChild(btnInfo);
    td9.appendChild(btnDelete);

    tr.appendChild(td);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tr.appendChild(td6);
    tr.appendChild(td7);
    tr.appendChild(td8);
    tr.appendChild(td9);

    get_table.appendChild(tr);
}

// Nova Admissão
async function save_adm_js(){
    // Função chamada quando o botão de salvar nova admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os valores dos campos de novo registro e enviar ao Python para salvar
    if ($("#formadm").valid()) {
        const nome = $('#nomeInput').val();
        const cpf = $('#cpfInput').val();
        const empresa = $('#empresaInput').val();
        const setor = $('#setorInput').val();
        const cargo = $('#cargoInput').val();
        const salariof = $('#salariofInput').val();
        const salario = $('#salarioInput').val();
        const dataadm = $('#dataadmInput').val();
        const result = await eel.btn_saveadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm)();
        location.reload();
    }
};

eel.expose(save_returnadm);
function save_returnadm(status) {
    // Função chamada quando o retorno do Python para o salvamento de nova admissão é recebido
    // Aqui você pode realizar as ações necessárias para exibir uma mensagem de retorno na página
    if (status == "sucess") {
        $('#return_register').text('Novo cadastro concluido com sucesso.');
        $('#empresaInput').val('');
        $('#setorInput').val('');
        $('#funcaoInput').val('');
        $('#liderInput').val('');
    }
    if (status == "failure") {
        $('#return_register').text('Erro ao cadastrar, verifique os campos em branco.')
    }
    if (status == "falhou") {
        $('#return_register').text('Erro ao cadastrar, contate o administrador.')
    }
};

// Editar Admissão
async function btn_edit(id){
    // Função chamada quando o botão de edição de um registro de admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os dados do registro a ser editado e enviar ao Python
    await eel.get_admissao(id)();
    $('#editadmmodal').modal("show");
}

eel.expose(action_editadm)
function action_editadm(editadm){
    // Função chamada quando os dados do registro a ser editado são recebidos do Python
    // Aqui você pode realizar as ações necessárias para exibir os dados na modal de edição
    editadm.forEach(get_array_values);
}

function get_array_values(item, index){
    // Função para preencher os campos da modal de edição com os dados do registro
    if (index == 0) {
        document.getElementById("editid").value = item;
    } else if (index == 1) {
        document.getElementById("editnomeInput").value = item;
    } else if (index == 2) {
        document.getElementById("editcpfInput").value = item;
    } else if (index == 3) {
        document.getElementById("editempresaInput").value = item;
    } else if (index == 4) {
        document.getElementById("editsetorInput").value = item;
    } else if (index == 5) {
        document.getElementById("editcargoInput").value = item;
    } else if (index == 6) {
        document.getElementById("editsalariofInput").value = item;
    } else if (index == 7) {
        document.getElementById("editsalarioInput").value = item;
    } else if (index == 8) {
        document.getElementById("editdataadmInput").value = item;
    }
    else {}
}

// Salvar Edição de Admissão
async function save_edit_js(){
    // Função chamada quando o botão de salvar edição de admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os valores dos campos editados e enviar ao Python para salvar
    if ($("#editadmform").valid()) {
        const id = $('#editid').val();
        const nome = $('#editnomeInput').val();
        const cpf = $('#editcpfInput').val();
        const empresa = $('#editempresaInput').val();
        const setor = $('#editsetorInput').val();
        const cargo = $('#editcargoInput').val();
        const salariof = $('#editsalariofInput').val();
        const salario = $('#editsalarioInput').val();
        const dataadm = $('#editdataadmInput').val();
        const result = await eel.save_editadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm, id)();
        location.reload();
    }
}

eel.expose(save_returneditadm);
function save_returneditadm(status) {
    // Função chamada quando o retorno do Python para o salvamento de edição de admissão é recebido
    // Aqui você pode realizar as ações necessárias para exibir uma mensagem de retorno na página
    if (status == "sucess") {
        $('#return_editadm').text('Edição concluída com sucesso.');
    }
    if (status == "failure") {
        $('#return_editadm').text('Erro ao editar, verifique os campos em branco.')
    }
    if (status == "falhou") {
        $('#return_editadm').text('Erro ao editar, contate o administrador.')
    }
};
