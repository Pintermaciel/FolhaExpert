$(document).ready(function(){
    eel.fetchalldata()

    $("#btn_addsetor").on("click", function(){
        $("#addsetorModal").modal("show");
    });
})

eel.expose(action_out)
function action_out(setor){
    //alert(registers);
    setor.forEach(showSetor)
}

function showSetor(item, index){
    var get_table = document.getElementById("setor");
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

    btnDelete.classList.add("btn", "btn-danger", "btn-circle");
    btnDelete.setAttribute("type", "button");
    btnDelete.setAttribute("data-ripple-color", "dark");

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

// Novo Setor
async function save_setor_js(){
    if ($("#formsetor").valid()) {
        const empresa = $('#empresaInput').val();
        const setor = $('#setorInput').val();
        const funcao = $('#funcaoInput').val();
        const lider = $('#liderInput').val();
        const result = await eel.btn_save(empresa, setor, funcao, lider)();
        location.reload();
    }
};

eel.expose(save_returnsetor);
function save_returnsetor(status) {
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