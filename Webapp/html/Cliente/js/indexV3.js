//Variables globales
var dataC,dataU,dataE,dataMP;
var dataCheck = [];
var dataList = [];
var activeSide = "1";
var chart;
var qrcode1,qrcode2,qrcode3,qrcode4,qrcode5,qrcode6,qrcode7,qrcode8,qrcodes;
var idcliente,type,idusuario;
var paginas = ["usuario","paquetes","etiquetas","pEtiquetas","modifyP","modifyP","print","config"];



//Funcion de inicio
$(function() 
{
    idcliente = sessionStorage.getItem("id_cliente");
    idusuario = sessionStorage.getItem("id_usuario");
    rol = sessionStorage.getItem("rol");
    if(idusuario === null || idcliente === null || rol === null)
    {
        var html = "https://"+ window.location.hostname + "/Cliente/login/";
        window.location = html;
    }
    
    
    var sendData = {id_usuario:idusuario};
        $.post( "../microservicios/getNombre.php", sendData).done(function(datos) {
            
            console.log(datos);
            $("#dnombre").html(datos["nombre"]);
            $("#nombreU").html(datos["nombre"]);
        });
    
    qrcode1 = new QRCode(document.getElementById("qrcode1"),{width:100,height:100});
    qrcode2 = new QRCode(document.getElementById("qrcode2"),{width:100,height:100});
    qrcode3 = new QRCode(document.getElementById("qrcode3"),{width:100,height:100});
    qrcode4 = new QRCode(document.getElementById("qrcode4"),{width:100,height:100});
    qrcode5 = new QRCode(document.getElementById("qrcode5"),{width:100,height:100});
    qrcode6 = new QRCode(document.getElementById("qrcode6"),{width:100,height:100});
    qrcode7 = new QRCode(document.getElementById("qrcode7"),{width:100,height:100});
    qrcode8 = new QRCode(document.getElementById("qrcode8"),{width:100,height:100});
    qrcodes = [qrcode1,qrcode2,qrcode3,qrcode4,qrcode5,qrcode6,qrcode7,qrcode8];
    llenadoUsuario();
    $("#guardarConfig").click(function(){
        var cand1 = $("input[name='opcionesCandado1']:checked").val();
        var cand1State = false;
        var cand2 = $("input[name='opcionesCandado2']:checked").val();
        var cand2State = false;
        if(cand1=="1")
        {
            cand1State = true;
        }
        if(cand2=="1")
        {
            cand2State = true;
        }
        var sendData = {id_cliente:idcliente,candado1:cand1State,candado2:cand2State};
        $.post( "../microservicios/changeCandados.php", sendData).done(function(datos) {
            //console.log(datos);
        });
    });
});

function esconderPaginas()
{
    for(var x = 0; x<paginas.length;x++)
    {
        $("#"+paginas[x]).prop("hidden",true);
    }
    $(".cLabel").hide();
    $(".checkL").hide();
    $(".caducText").hide();
}
 
function chooseType()
{
    
    esconderPaginas();
    clearQR();
    
    if(document.getElementById('type1').checked) 
    {
        type=1;
        $(".checkL").show(); 
        $(".cLabel").show();
        $(".caducText").show();
    }
    else if(document.getElementById('type2').checked) 
    {
        type=2;
    }
    else if(document.getElementById('type3').checked) 
    {
        type=3;
    }
    else if(document.getElementById('type4').checked) 
    {
        type=4;
    }
    
    $("#tituloP").html("Nueva hoja");
    $("#tituloModalP").html("Crear hoja");
    $("#uploadNewP").html("Crear");
    $("#uploadNewP").attr("onclick","uploadNewP()");
    $("#buttonP").html("Registrar");
    $("#buttonP").attr("onclick","modalNewPage()");
    $("#pEtiquetas").prop("hidden",false);
    
    $('.checkL').each(function(i, obj) {
        obj.checked = false;
    });
    
    for(var i = 1;i<9;i++)
    {
        $("#txt"+i).attr("disabled",false);
    }
    $(".inptext").
      on("blur", function (ele) {
        makeCode(ele,1);
      }).
      on("keydown", function (ele) {
        if (ele.keyCode == 13) {
            makeCode(ele,1);
        }
      });
}

function clearQR()
{
    for(var i = 1; i<9;i++)
    {
        $("#txt"+i).val("");
        $("#cad"+i).val("");
        document.querySelector("#qrcode"+i+" img").style = "display:none";
    }
}
//Funcion para el llenado de la pagina del usuario
function llenadoUsuario()
{
    var sendData = {id_cliente:idcliente};
    var dataChart = [0,0,0,0,0,0,0];
    $.post( "../microservicios/getPaquetes.php", sendData).done(function(datos) {
       
        //console.log(datos);
        if(datos["status"]==1)
        {
            var data = datos["data"];
            if(data.length>4)
            {
                var cL = 5;
            }
            else
            {
                var cL = data.length;
            }
            $("#historialList").html("");
            for(var i = 0;i<cL;i++)
            {
                var fec = data[i].fecha;
                fec = fec.slice(0,10);
                //console.log(fec)
                var app = "<li class='list-group-item'><img src='img/tick.png' width='25' class='d-inline-block align-top iconR' alt='T'>"+data[i].descripcion+" </li>";
                
                $("#historialList").append(app);
            }
        }
        
    });
    
    $.post( "../microservicios/getLotesSemana.php", sendData).done(function(datos) {
        
        //console.log(datos)
        
        if(datos["status"]==1)
        {
            var data = datos["data"];
            for(var i = 0;i<data.length;i++)
            {
                var dia = new Date(data[i].dia);
                dataChart[parseInt(dia.getDay())]=parseInt(data[i].cuenta);
            }
        }

        const ctx = document.getElementById('semanaGrafica').getContext('2d');
        chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
                datasets: [{
                    data: dataChart,
                    backgroundColor: [
                      '#FF6B35'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                    display: false
                    },
                    title: {
                        display: true,
                        text: 'Lotes Procesados en la Semana',
                        font: {
                            size: 18
                        }
                    }
                }
            }
        });
    });
}

function getPaquetes()
{
    var sendData = {id_cliente:idcliente};
    $.post( "../microservicios/getPaquetes.php", sendData).done(function(datos) {
        //console.log(datos);
        return datos.data;
    });
}
//Funcion de llenado de la tabla de paquetes
function llenadoPaquetes()
{
    var sendData = {id_cliente:idcliente};
    $.post( "../microservicios/getPaquetes.php", sendData).done(function(datos) {
        console.log(datos);
        var data = datos.data;
        
        $("#bodyPaquetes").html("");
        for(var i = 0; i < data.length; i++)
        {
            var indicador = "";
            switch(data[i].indicador)
            {
                case 0:
                    indicador = "No verificado";
                    break;
                case 1:
                    indicador = "Verificado";
                    break;
                case 2:
                    indicador = "Fallido";
                    break;
            }

            $("#bodyPaquetes").append("<tr><td>"+data[i].codigo+"</td><td>"+data[i].descripcion+"</td><td>"+data[i].fecha+"</td><td>"+data[i].caducidad+"</td><td>"+data[i].usuario+"</td><td>"+indicador+"</td></tr>");
        }
        //<tr><td>1</td><td>3-4-2022</td><td>Kit general de cirugía 1</td><td>Benjamin Jimenez</td></tr>
        $('#table_id').DataTable();
    });
    
}

//Funcion de manejo de clicks en sidebar.
function changeSide(e)
{
    //console.log(e.id);
    $("#"+activeSide).removeClass("active");
    $("#"+e.id).addClass("active");
    activeSide = e.id;
    var id = parseInt(e.id);
    chart.destroy();
    switch(id)
    {
        case 1:
            llenadoUsuario();
            esconderPaginas();
            $("#usuario").prop("hidden",false);
            break;
            
        case 2:
            llenadoPaquetes();
            esconderPaginas();
            $("#paquetes").prop("hidden",false);
            break;
            
        case 3:
            esconderPaginas();
            $("#etiquetas").prop("hidden",false);
            break;
        case 4:
            esconderPaginas();
            getPages(3);
            break;
        case 5:
            esconderPaginas();
            $("#config").prop("hidden",false);
            break;
        case 6:
            var pass = confirm("¿Seguro que quieres cerrar sesión?");
            console.log(pass)
            if(pass)
            {
                sessionStorage.removeItem("id_usuario");
                sessionStorage.removeItem("id_cliente");
                sessionStorage.removeItem("rol"); 
                var html = "https://"+ window.location.hostname + "/Cliente/login/";
                window.location = html;
            }
            break;
    }
    
}

function modalPageType()
{
    $("#pageType").modal('toggle');
}

//Funcion de manejo de creacion de hojas de codigos QR
function manejoHojas(e)
{
    var id = parseInt(e.id.substr(1));
    switch(id)
    {
        case 1:
            modalPageType();
            
            break;
            
        case 2:
            getPages(1);
            break;
            
        case 3:
            getPages(2);
            //console.log(2);
            break;
    }
}

//Funcion para obtener paginas creadas por usuario
function getPages(o)
{
    var sendData = {id_cliente:idcliente};
    $.post( "../microservicios/getPages.php", sendData).done(function(datos) {
        
        //console.log(datos);
        if(datos.status==1) 
        {
            dataMP = datos.datos;
            var strapp = "";
            esconderPaginas();
            var click = "";
            if(o==1)
            {
                $("#bodyModifyP").html("");
                $("#modifyP").prop("hidden",false);
                click="'manejoEditP(this)'><img src='img/editing.png'";
            }
            else if(o==2)
            {
                $("#bodyModifyP").html("");
                $("#modifyP").prop("hidden",false);
                click="'manejoVerP(this)'><img src='img/see.png'";
            }
            else if(o==3)
            {
                $("#bodyPrint").html("");
                $("#print").prop("hidden",false);
                click="'manejoPrint(this)'><img src='img/printerOrng.png'";
            }
            //console.log(dataMP);
            for(var i = 0; i<dataMP.length;i++)
            {
                var data = dataMP[i];
                //console.log(data);
                strapp="<div class='col-4' style='margin-top:15px'><div class='card'><div class='card-body'><div class='form-check'><a href='#' class='stretched-link' id='e"+i+"' onclick="+click+" class='img-fluid imLbl' id='edit"+i+"' width=35px><label class='form-check-label' for='edit"+i+"'><h4 class='labelEtiqueta'>"+data.nombre+"</h4></label></a></div></div></div></div>";
                if(o!=3)
                {
                    $("#bodyModifyP").append(strapp); 
                }
                else
                {
                    $("#bodyPrint").append(strapp); 
                }
            }
        }
        else
        {
            $("#bodyModifyP").html("No hay hojas creadas."); 
            esconderPaginas();
            $("#modifyP").prop("hidden",false);
        }
    });   
}

//Funcion para ver hojas de QR ya creadas
function manejoVerP(e)
{
    var id = parseInt(e.id.substr(1));
    //console.log(id);
    var datos = dataMP[id];
    var data = datos.datos;
    //console.log(datos)
    esconderPaginas();
    clearQR();
    $("#tituloP").html(datos.nombre);
    $("#buttonP").html("Regresar");
    $("#buttonP").attr("onclick","changeSide(document.getElementById(3))");
    var x = 0;
    for(var i = 0;i<data.length;i++)
    {
        x = i+1;
        $("#txt"+x).val(data[i].descripcion);
        $("#txt"+x).attr("data",data[i].codigo);
        $("#txt"+x).attr("disabled",true);
        makeCode(document.getElementById("txt"+x),2);
    }
    for(var i = datos.length+1;i<9;i++)
    {
        $("#txt"+i).attr("disabled",true);
    }
    $("#pEtiquetas").prop("hidden",false);
}

//Funcion para editar hojas ya creadas 
function manejoEditP(e)
{
    var id = parseInt(e.id.substr(1));
    //console.log(id);
    var datos = dataMP[id];
    //console.log(datos)
    var data = datos.datos;
    esconderPaginas();
    clearQR();
    $("#tituloP").html(datos.nombre);
    $("#buttonP").html("Actualizar");
    $("#tituloModalP").html("Actualizar hoja");
    $("#uploadNewP").html("Guardar");
    $("#uploadNewP").attr("onclick","modifyP(this)");
    $("#uploadNewP").attr("data",datos.id_pagina);
    $("#newNombreP").val(datos.nombre);
    $("#buttonP").attr("onclick","modalNewPage()");
    var x = 0;
    for(var i = 0;i<data.length;i++)
    {
        x = i+1;
        $("#txt"+x).val(data[i].descripcion);
        $("#txt"+x).attr("disabled",false);
        $("#txt"+x).attr("data",data[i].codigo);
        makeCode(document.getElementById("txt"+x),2);
    }
    for(var i = data.length+1;i<9;i++)
    {
        $("#txt"+i).attr("disabled",false);
    }
    $("#pEtiquetas").prop("hidden",false);
    $(".inptext").
      on("blur", function (ele) {
        makeCode(ele,1);
      }).
      on("keydown", function (ele) {
        if (ele.keyCode == 13) {
            makeCode(ele,1);
        }
      });
}

// Modal para nombrado de hoja y listado de instrumentos.
function modalNewPage()
{
    //console.log(type);
    if(type==1)
    {
        var x = 0;
        $('.checkL').each(function(i, obj) {
            if(obj.checked)
            {
                //console.log(obj);
                dataCheck[x]=obj.id;
                x++;
            }
        });
        if(dataCheck.length>0)
        {
            stepCL(dataCheck[0],0);
        }
        else
        {
            $("#newPage").modal('toggle');
        }
    }
    else
    {
        $("#newPage").modal('toggle');
    }
    //$("#newPage").modal('toggle');
}

function stepCL(ele,idx)
{   
    //console.log(idx);
    //console.log(ele);
    var id = ele.substr(1);
    //console.log(id);
    var nxt = idx+1;
    
    $("#kitListT").html($("#txt"+id).val());
    $("#txt"+id).prop("check",1);
    if(idx == 0)
    {
        $("#listado").modal('toggle');
        $("#uploadCheck").off("click");
        $("#uploadCheck").click(function(){registerList(idx)});
        $("#uploadCheck").html("Siguiente");
    }
    //console.log(dataCheck[nxt])
    //HAY QUE PERMITIR QUE SE CORRA EL REGISTER LIST PARA SOLO 1 CHECKBOX
    //revisar el microservicio
    
    if(dataCheck[nxt]!=undefined)
    {
        $("#uploadCheck").off("click");
        $("#uploadCheck").click(function(){registerList(idx)});
    }
    else
    {
        //salida de modal, hacia modal de nombrado
        $("#uploadCheck").off("click");
        $("#uploadCheck").click(function(){changeMod(idx)});
        $("#uploadCheck").html("Guardar");
    }
    
}

function changeMod(q)
{
    
    var valores = [];
    var extra = 0;
    $('.listObj').each(function(i, obj) {
        if(obj.value!="")
        {
            valores.push(obj.value);
        }
        if(i>5)
        {
            extra++;
        }
    });
    $('.listObj').each(function(i, obj) {
        obj.value = "";
    });
    dataList.push(valores);
    
    $("#listado").modal('hide');
    $("#newPage").modal('toggle');
}

function registerList(c)
{
    var valores = [];
    var extra = 0;
    $('.listObj').each(function(i, obj) {
        if(obj.value!="")
        {
            valores.push(obj.value);
        }
        if(i>5)
        {
            extra++;
        }
    });
    $('.listObj').each(function(i, obj) {
        obj.value = "";
    });
    dataList.push(valores);
    stepCL(dataCheck[c+1],c+1)
}

function uploadNewP()
{
    
    var valores = [];
    var bin = [];
    var list = [];
    var c = 0;
    var titulo = $("#newNombreP").val();
    for(var i = 1 ; i<9;i++)
    {
        var txt = $("#txt"+i).val();
        
        if(txt)
        {
             valores.push(txt);
            if(type == 1)
            {
                
                if($("#txt"+i).prop("check") == 1)
                {
                    bin.push(1);
                    list.push(dataList[c]);
                    c++;
                }
                else
                {
                    bin.push(0);
                }
            }
        }
    }
    
    if(type==1)
    {
        var caducidad = []
        $('.caducText').each(function(i, obj) {
            caducidad.push(obj.value)
        });
        
        var sendData = {operacion:1,id_cliente:idcliente,titulo:titulo,datos:valores,tipo:type,bin:bin,list:list,caducidad:caducidad};
    }
    else
    {
        var sendData = {operacion:1,id_cliente:idcliente,titulo:titulo,datos:valores,tipo:type};
    }
    //console.log(sendData);
    
    $.post( "../microservicios/modifyPage.php", sendData).done(function(data) {

        //console.log(data); 
        esconderPaginas();
        $("#etiquetas").prop("hidden",false);
    });   
}

function modifyP(e)
{
    var idpag = parseInt(e.getAttribute("data"));
    var valores = [];
    var ids = [];
    var titulo = $("#newNombreP").val();
    for(var i = 1 ; i<9;i++)
    {
        var txt = $("#txt"+i).val();
        var id = $("#txt"+i).attr("data");
        if(txt)
        {
             valores.push(txt);
             ids.push(id);
        }
    }
    //console.log(type)
    var sendData = {operacion:2,id_cliente:idcliente,titulo:titulo,datos:valores,codigos:ids,id_pagina:idpag};
    //console.log(sendData);
    
    $.post( "../microservicios/modifyPage.php", sendData).done(function(data) {

        //console.log(data); 
        esconderPaginas();
        $("#etiquetas").prop("hidden",false);
    });   
    
}
//Funcion para crear codigo QR
const removeAccents = (str) => {
  return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
} 
function makeCode (el,t) {    
    if(t==1)
    {
        var e = el.currentTarget;
    }
    else
    {
        var e = el;
    }
    
    var id = parseInt(e.id.substr(3));
    qrcodes[id-1].clear();
    if(e.value != "")
    {
        //console.log(e.value)
        var txtS = removeAccents(e.value);
        qrcodes[id-1].makeCode(txtS);
    }
}

//Funcion para cambio de formato de fechas
function dateFormat(inputDate, format) 
{
    const date = new Date(inputDate);

    const day = date.getDate();
    const month = date.getMonth() + 1;
    const year = date.getFullYear();    

    format = format.replace("MM", month.toString().padStart(2,"0"));        

    if (format.indexOf("yyyy") > -1) {
        format = format.replace("yyyy", year.toString());
    } else if (format.indexOf("yy") > -1) {
        format = format.replace("yy", year.toString().substr(2,2));
    }

    format = format.replace("dd", day.toString().padStart(2,"0"));
    return format;
}

function manejoPrint(e)
{
    
    var id = parseInt(e.id.substr(1));
    //console.log(id);
    var datos = dataMP[id];
    //console.log(datos);
    clearQR();
    var x = 0;
    var doc = new jsPDF();
    doc.setFontSize(35);
    var myImage = new Image();
        myImage .src = 'img/image_1.png';
        myImage .onload = function(){
        doc.addImage(myImage, "PNG", 10, 10,140,26);
        };
    
    doc.text(datos.nombre, 35, 55);
    var data = datos.datos;
    for(var i = 0;i<data.length;i++)
    {
        x = i+1;
        $("#txt"+x).val(data[i].codigo);
        $("#txt"+x).attr("disabled",true);
        makeCode(document.getElementById("txt"+x),2);
    }
    for(var j = data.length+1;j<9;j++)
    {
        $("#txt"+j).attr("disabled",true);
    }
    //Agregar logo de tecnodomus y mejorar estilo.
    setTimeout(function(){
        doc.setFontSize(20);
        for(var z = 0;z<data.length;z++)
        {  
            x = z+1;
            var img = document.querySelector("#qrcode"+x+" img");
            var e = img.src;
            var offset = z*30;
            //console.log(img);
            //console.log(e);
            doc.addImage(e, "PNG", 30, 65+offset, 20, 20);
            doc.text(data[z].descripcion, 70, 75+offset);
        }
        doc.save(datos.nombre+'.pdf');
    }, 1000);
    
    
}


//Funcion para obtener la fecha del lunes y domingo de la semana actual
function getWeekStartFinish(){
  const today = new Date();
  const first = today.getDate() - today.getDay() + 2;
  const last = first + 6;
  const monday = new Date(today.setDate(first));
  const sunday = new Date(today.setDate(last));
  return {monday:dateFormat(monday,'yyyy-MM-dd'),sunday:dateFormat(sunday,'yyyy-MM-dd')};
}
