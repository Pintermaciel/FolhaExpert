$(document).ready(function(){
    eel.fetchalldatares()

    $("#btn_addres").on("click", function(){
        $("#addresModal").modal("show");
    });
})

eel.expose(action_outres)
function action_outres(rescisao){
    //alert(registers);
    rescisao.forEach(showRes)
}

eel.expose(action_editres)
function action_editres(editrescisao){
    //alert(editrescisao);  
    editrescisao.forEach(get_array_values)
}

function get_array_values(item, index){
    //alert(item);
    //alert(index);
    if (index == 1) {
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

function showRes(item, index){
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

    btnDelete.classList.add("btn", "btn-danger", "btn-circle");
    btnDelete.setAttribute("type", "button");
    btnDelete.setAttribute("data-ripple-color", "dark");

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
    if ($("#formres").valid()) {
        const nome = $('#nomeInput').val();
        const datares = $('#dataresInput').val();
        const liquidores = $('#liquidoresInput').val();
        const carteirares = $('#carteiraresInput').val();
        const motivo = $('#motivoInput').val();
        const result = await eel.btn_saveres(nome, datares, liquidores, carteirares, motivo)();
        location.reload();
    }
};

eel.expose(save_returnres);
function save_returnres(status) {
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

// Editar Rescisão
async function btn_edit(id){
    await  eel.get_rescisao(id)();
    $('#editresmodal').modal("show");
}