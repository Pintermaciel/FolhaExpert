$(document).ready(function(){
    eel.fetchalldataadm()

    $("#btn_addadm").on("click", function(){
        $("#addadmModal").modal("show");
    });
})

eel.expose(action_outadm)
function action_outadm(adm){
    //alert(registers);
    adm.forEach(showAdm)
}

function showAdm(item, index){
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
    if ($("#formadm").valid()) {
        const nome = $('#nomeInput').val();
        const cpf = $('#cpfInput').val();
        const empresa = $('#empresaInput').val();
        const setor = $('#setorInput').val();
        const salariof = $('#salariofInput').val();
        const salario = $('salarioInput')
        const result = await eel.btn_save(nome, cpf, empresa, setor, salariof, salario)();
        location.reload();
    }
};

eel.expose(save_returnadm);
function save_returnadm(status) {
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