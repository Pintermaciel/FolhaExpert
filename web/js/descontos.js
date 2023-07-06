$(document).ready(function(){
    eel.fetchalldatadesc();
});

eel.expose(action_outdesc)
function action_outdesc(competencia){
    // Função chamada quando os dados de competencia são recebidos do Python
    // Aqui você pode realizar as ações necessárias para exibir os dados na página
    competencia.forEach(showDesc);
}

function showDesc(item, index){
    // Função para exibir os dados de um registro de competencia na tabela da página
    var get_table = document.getElementById("descontos");
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
    var td10 = document.createElement("td");
    var td11 = document.createElement("td");
    var td12 = document.createElement("td");
    var td13 = document.createElement("td");
    var td14 = document.createElement("td");
    var td15 = document.createElement("td");
    var td16 = document.createElement("td");

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
    td9.innerText = item[9]
    td10.innerText = item[9]
    td11.innerText = item[9]
    td12.innerText = item[9]
    td13.innerText = item[9]
    td14.innerText = item[9]
    td15.innerText = item[9]
    


    var btnInfo = document.createElement("button");
    var infoIcon = document.createElement("i");

    btnInfo.classList.add("btn", "btn-info", "btn-circle");
    btnInfo.setAttribute("type", "button");
    btnInfo.setAttribute("data-ripple-color", "dark");
    btnInfo.setAttribute("onclick", "btn_edit('" + id + "')");
    btnInfo.setAttribute("style", "margin:5px");

    infoIcon.classList.add("fas", "fa-info-circle");

    btnInfo.appendChild(infoIcon);

    td16.appendChild(btnInfo);

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
    tr.appendChild(td10);
    tr.appendChild(td11);
    tr.appendChild(td12);
    tr.appendChild(td13);
    tr.appendChild(td14);
    tr.appendChild(td15);
    tr.appendChild(td16);
    get_table.appendChild(tr);
}

// Editar Admissão
async function btn_edit(id){
    // Função chamada quando o botão de edição de um registro de admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os dados do registro a ser editado e enviar ao Python
    await eel.get_conv(id)();
    $('#editmodal').modal("show");
}

eel.expose(action_editdesc)
function action_editdesc(editcomp){
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
    } else if (index == 4) {
        document.getElementById("editcompetenciaInput").innerText = item;
    } else if (index == 14) {
        document.getElementById("editcartaoacivale").value = item;
    } else if (index == 15) {
        document.getElementById("editunimed").value = item;
    } else if (index == 16) {
        document.getElementById("editdesp_unimed").value = item;
    } else if (index == 17) {
        document.getElementById("farmacia").value = item;
    }
    else {}
}

// Salvar Edição de Admissão
async function save_edit_js(){
    // Função chamada quando o botão de salvar edição de admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os valores dos campos editados e enviar ao Python para salvar
    if ($("#editadmform").valid()) {
        const id = $('#editid').val();
        const nome = $('#editnomeInput').text();
        const competencia = $('#editcompetenciaInput').text();
        const cartaoacivale = $('#editcartaoacivale').val();
        const unimed = $('#editunimed').val();
        const desp_unimed = $('#edidesp_unimed').val();
        const farmacia = $('#farmacia').val();
        const result = await eel.save_editconv(nome, competencia, cartaoacivale, unimed, desp_unimed, farmacia, id)();
        location.reload();
    }
}