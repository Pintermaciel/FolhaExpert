$(document).ready(function(){
    eel.fetchalldatahrs();
});

eel.expose(action_outhrs)
function action_outhrs(competencia){
    // Função chamada quando os dados de competencia são recebidos do Python
    // Aqui você pode realizar as ações necessárias para exibir os dados na página
    competencia.forEach(showHoras);
}

function showHoras(item, index){
    // Função para exibir os dados de um registro de competencia na tabela da página
    var get_table = document.getElementById("horas");
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
    


    var btnInfo = document.createElement("button");
    var infoIcon = document.createElement("i");

    btnInfo.classList.add("btn", "btn-info", "btn-circle");
    btnInfo.setAttribute("type", "button");
    btnInfo.setAttribute("data-ripple-color", "dark");
    btnInfo.setAttribute("onclick", "btn_edit('" + id + "')");
    btnInfo.setAttribute("style", "margin:5px");

    infoIcon.classList.add("fas", "fa-info-circle");

    btnInfo.appendChild(infoIcon);

    td10.appendChild(btnInfo);

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
    get_table.appendChild(tr);
}

// Editar Admissão
async function btn_edit(id){
    // Função chamada quando o botão de edição de um registro de admissão é clicado
    // Aqui você pode realizar as ações necessárias para obter os dados do registro a ser editado e enviar ao Python
    await eel.get_hrs(id)();
    $('#editmodal').modal("show");
}

eel.expose(action_edithrs)
function action_edithrs(editcomp){
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
    } else if (index == 5) {
        document.getElementById("edithnInput").value = item;
    } else if (index == 6) {
        document.getElementById("edithe50Input").value = item;
    } else if (index == 7) {
        document.getElementById("edithe65Input").value = item;
    } else if (index == 8) {
        document.getElementById("edithe75Input").value = item;
    } else if (index == 9) {
        document.getElementById("edithe100Input").value = item;
    } else if (index == 10) {
        document.getElementById("faltadias").value = item;
    } else if (index == 11) {
        document.getElementById("faltahora").value = item;
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
        const competencia = $('#editcompetenciaInput').val();
        const hn = $('#edithnInput').val();
        const he50 = $('#edithe50Input').val();
        const he65 = $('#edithe65Input').val();
        const he75 = $('#edithe75Input').val();
        const he100 = $('#edithe100Input').val();
        const faltadias = $('#faltadias').val();
        const faltahora = $('#faltahora').val();
        const result = await eel.save_edithoras(nome, competencia, hn, he50, he65, he75, he100, faltadias, faltahora, id)();
        location.reload();
    }
}

//Deletar

let deleteCompetenciaId; // Variável global para armazenar o ID do admissao a ser excluído

async function btn_delete(id) {
    $('#deleteadmissaomodal').modal("show"); // Abre o modal de confirmação de exclusão
    deleteCompetenciaId = await eel.get_delete_competencia(id)(); // Obtém o ID do admissao a ser excluído usando a função exposta do lado do servidor
}

async function btn_submitdelete() {
    const response = await eel.delete_competencia(deleteCompetenciaId)(); // Exclui o admissao usando o ID armazenado na variável deleteAdmissaoId
    if (response === "success") {
        location.reload(); // Recarrega a página após a exclusão bem-sucedida
    } else {
        console.log("Erro ao excluir o setor."); // Exibe uma mensagem de erro caso ocorra algum problema na exclusão
    }
}