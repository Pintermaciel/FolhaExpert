$(document).ready(function(){
    eel.fetchalldatacompetencia();
});

// Nova competencia
async function new_comp(){
    // Função chamada quando o botão de edição de um registro de admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os dados do registro a ser editado e enviar ao Python
    $('#competenciammodal').modal("show");
}

async function save_comp_js(){
    // Função chamada quando o botão de salvar nova admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os valores dos campos de novo registro e enviar ao Python para salvar
        const comp = $('#compInput').val();
        const dias = $('#diasuteisInput').val();
        const feriados = $('#feriadosInput').val();
        const result = await eel.btn_savecomp(comp, dias, feriados)();
        alert("cadastrado competência: " + comp + " com " + dias + " Dias Uteis e " + feriados + " Feriados");
        location.reload();
};

eel.expose(action_outCompetencia)
function action_outCompetencia(competencia){
    // Função chamada quando os dados de competencia são recebidos do Python
    // Aqui você pode realizar as ações necessárias para exibir os dados na página
    competencia.forEach(showCompetencia)
};

function showCompetencia(item, index){
    // Função para exibir os dados de um registro de competencia na tabela da página
    var get_table = document.getElementById("competencia");
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");
    var td4 = document.createElement("td");
    var td5 = document.createElement("td");

    var id = item[0]
    td.innerText = item[0]
    td1.innerText = item[1]
    td2.innerText = item[2]
    td3.innerText = item[3]
    td4.innerText = item[4]

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

    td5.appendChild(btnInfo);
    td5.appendChild(btnDelete);

    tr.appendChild(td);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    get_table.appendChild(tr);
}

// Editar Admissão
async function btn_edit(id){
    // Função chamada quando o botão de edição de um registro de admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os dados do registro a ser editado e enviar ao Python
    await eel.get_competencia(id)();
    $('#editmodal').modal("show");
}

eel.expose(action_editcomp)
function action_editcomp(editcomp){
    // Função chamada quando os dados do registro a ser editado são recebidos do Python
    // Aqui você pode realizar as ações necessárias para exibir os dados na modal de edição
    editcomp.forEach(get_array_values);
}

function get_array_values(item, index){
    // Função para preencher os campos da modal de edição com os dados do registro
    if (index == 0) {
        document.getElementById("editid").value = item;
    } else if (index == 1) {
        document.getElementById("editnomeInput").innerText = item;
    } else if (index == 2) {
        document.getElementById("editsetorInput").innerText = item;
    } else if (index == 3) {
        document.getElementById("editfuncaoInput").innerText = item;
    } else if (index == 4) {
        document.getElementById("editcompetenciaInput").innerText = item;
    }
    else {}
}