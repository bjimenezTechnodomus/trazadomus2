// Vectores para manejo de clientes, usuarios y equipos.
var dataC,dataU,dataE;
var idusuario,nombre;
var activeSide = "1";

//Función inicial
$(function() 
{
    idusuario = sessionStorage.getItem("id_usuario");
    nombre = sessionStorage.getItem("nombre");
    if(idusuario === null)
    {
        var html = "https://"+ window.location.hostname + "/Administracion/login/";
        window.location = html;
    }
    $("#dnombre").html(nombre);
    llenadoClientes();
});

//Llenado de la página de clientes
function llenadoClientes()
{
    var sendData = {"status":1};
    $.post( "../microservicios/getClientes.php", sendData).done(function(data) {

        console.log(data); 
        $("#bodyClientes").html("");
        dataC = data;
        console.log(data.length)
        for( var i = 0 ; i<data.length;i++)
        {
            $("#bodyClientes").append("<tr><td>"+data[i]["ID_cliente"]+"</td><td>"+data[i]["Nombre"]+"</td><td>"+data[i]["Equipos"]+"</td><td>"+data[i]["Ciclos"]+"</td><td><a href='#' id='c"+data[i]["ID_cliente"]+"' onclick='llenadoUsuarios(this)'>"+data[i]["Usuarios"]+"</a></td><td style='width:200px;' class='text-center'><input id='ec"+i+"' type='image' onclick='editarC(this)'src='img/editar.png' name='editar' width='30' alt='editar'/></td></tr>");
        }
        
    });
}

/* Modificación de usuarios de clientes*/
function llenadoUsuarios(e)
{
    console.log(e.id);
    var id = parseInt(e.id.substring(1));
    console.log(id);
    var sendData = {"id_cliente":id};
    
    $.post( "../microservicios/getUsuarios.php", sendData).done(function(data) {
        console.log(data);
        dataU=data;
        $("#bodyUsuarios").html("");
        for( var i = 0 ; i<data.length;i++)
        {
            $("#bodyUsuarios").append("<tr><td>"+data[i].ID_usuario+"</td><td>"+data[i].Nombre+" "+data[i].Apellido+"</td><td>"+data[i].Correo+"</td><td>"+data[i].Rol+"</td><td><input id='u"+i+"' type='image' onclick='editarU(this)'src='img/editar.png' name="+id+" width='30' alt='editar'/></td></tr>");
        }
        
        $("#clientes").prop("hidden",true);
        $("#uploadNewU").prop("cid",id);
        $("#usuarios").prop("hidden",false);
        
    });
    
}

/* Funcion para mostrar pantalla de modificación de usuarios*/
function editarU(e)
{
    console.log(e.id);
    var id = dataU[parseInt(e.id.substring(1))].ID_usuario;
    var correo = dataU[parseInt(e.id.substring(1))].Correo;
    var nombre = dataU[parseInt(e.id.substring(1))].Nombre;
    var apellido = dataU[parseInt(e.id.substring(1))].Apellido;
    var rol = dataU[parseInt(e.id.substring(1))].ID_Rol;
    console.log(id);
    $("#editNombre").val(nombre);
    $("#editApellido").val(apellido);
    $("#editCorreo").val(correo);
    $("#rol"+rol).prop("checked",true);
    $("#deleteU").prop("cid",e.name);
    $("#deleteU").prop("name",id);
    $("#uploadU").prop("cid",e.name);
    $("#uploadU").prop("name",id);
    $("#usuarioModal").modal('toggle');
    
}

//Función para borrar usuarios.
function deleteU(e)
{
    console.log(e.name);
    console.log(e.cid);
    var id = e.name;
    var cid = e.cid;
    if(confirm('Estas seguro que quieres eliminar este usuario?'))
    {
        var sendData = {id_usuario:id,id_cliente:cid,operacion:3};
        $.post( "../microservicios/modifyUsuarios.php", sendData).done(function(data) {
            console.log(data);
            llenadoUsuarios(document.getElementById("c"+cid));
            /*
            $("#clientsAlert").fadeTo(2000, 500).slideUp(500, function() {
              $("#clientsAlert").slideUp(500);
            });
            */
            
        });
    }
}
//Funcion para modificar usuarios ya existentes
function uploadU(e)
{
    console.log(e.name);
    console.log(e.cid);
    var id = e.name;
    var cid = e.cid;
    var nombre = $("#editNombre").val();
    var apellido = $("#editApellido").val();
    var correo = $("#editCorreo").val();
    var rol;
    if(document.getElementById('rol1').checked) {
        rol=1;
    }else if(document.getElementById('rol2').checked) {
        rol=2;
    }
    var sendData = {id_usuario:id,id_cliente:cid,nombre:nombre,apellido:apellido,correo:correo,rol:rol,operacion:2};
    $.post( "../microservicios/modifyUsuarios.php", sendData).done(function(data) {
        console.log(data);
        llenadoUsuarios(document.getElementById("c"+cid));

    });

}

function addUserMod()
{
    $("#newusuarioModal").modal('toggle');
    
}

//Función para crear nuevos usuarios
function uploadNewU(e)
{
    console.log(e.cid);
    var cid = e.cid;
    var nombre = $("#newNombre").val();
    var apellido = $("#newApellido").val();
    var correo = $("#newCorreo").val();
    var rol;
    if(document.getElementById('newrol1').checked) {
        rol=1;
    }else if(document.getElementById('newrol2').checked) {
        rol=2;
    }
    var sendData = {id_cliente:cid,nombre:nombre,apellido:apellido,correo:correo,rol:rol,operacion:1};
    $.post( "../microservicios/modifyUsuarios.php", sendData).done(function(data) {
        console.log(data);
        llenadoUsuarios(document.getElementById("c"+cid));

    });
}
/* Funciones de modificación de clientes*/
function editarC(e)
{
    console.log(e.id);
    
    var id = dataC[parseInt(e.id.substring(2))].ID_cliente;
    var nombre = dataC[parseInt(e.id.substring(2))].Nombre;
    console.log(id);
    $("#editNombreC").val(nombre);
    $("#deleteC").prop("name",id);
    $("#uploadC").prop("name",id);
    $("#clienteModal").modal('toggle');
    
}

//Funcion para la eliminación de clientes
function deleteC(e)
{
    console.log(e.name);
    var id = e.name;
    if(confirm('Estas seguro que quieres eliminar este cliente?'))
    {
        var sendData = {id_cliente:id,operacion:3};
        $.post( "../microservicios/modifyClientes.php", sendData).done(function(data) {
            console.log(data);
            llenadoClientes()
            /*
            $("#clientsAlert").fadeTo(2000, 500).slideUp(500, function() {
              $("#clientsAlert").slideUp(500);
            });
            */
            
        });
    }
}

//Funcion para subir la modificación de clientes
function uploadC(e)
{
    console.log(e.name);
    var id = e.name;
    var nombre = $("#editNombreC").val();
    var sendData = {id_cliente:id,nombre:nombre,operacion:2};
    $.post( "../microservicios/modifyClientes.php", sendData).done(function(data) {
        console.log(data);
        llenadoClientes()
    });
}

//Funcion para mostrar el modal para creacion de clientes
function addClientMod()
{
    $("#newclienteModal").modal('toggle');
}

//Funcion de creacion de clientes
function uploadNewC(e)
{
    var nombre = $("#newNombreC").val();

    var sendData = {nombre:nombre,operacion:1};
    $.post( "../microservicios/modifyClientes.php", sendData).done(function(data) {
        console.log(data);
        llenadoClientes();

    });
}

//Funcion de manejo de clicks en sidebar.
function changeSide(e)
{
    console.log(e.id);
    $("#"+activeSide).removeClass("active");
    $("#"+e.id).addClass("active");
    activeSide = e.id;
    var id = parseInt(e.id);
    $("#usuarios").prop("hidden",true);
    switch(id)
    {
        case 1:
            llenadoClientes();
            $("#clientes").prop("hidden",false);
            $("#equipos").prop("hidden",true);
            break;
            
        case 2:
            llenadoEquipos();
            $("#clientes").prop("hidden",true);
            $("#equipos").prop("hidden",false);
            break;
            
        case 3:
            var pass = confirm("¿Seguro que quieres cerrar sesión?");
            if(pass)
            {
                sessionStorage.removeItem("id_usuario");
                var html = "https://"+ window.location.hostname + "/Administracion/login/";
                window.location = html;
            }
            break;
    }
    
}

//Funcion de llenado de tabla de equipos.
function llenadoEquipos()
{
    
    var sendData = {"status":1};
    $.post( "../microservicios/getEquipos.php", sendData).done(function(data) {

        console.log(data); 
        $("#bodyEquipos").html("");
        dataE = data;
        var status = "";
        for( var i = 0 ; i<data.length;i++)
        {
            
            if(data[i]["status"]==1)
            {
                status = "<td class='text-success'>En línea</td>";
            }
            else
            {
                status = "<td class='text-warning'>Fuera de línea</td>";
            }
            $("#bodyEquipos").append("<tr><td>"+data[i]["ID_equipo"]+"</td><td>"+data[i]["Nombre"]+"</td><td>"+data[i]["Fecha"]+"</td>"+status+"</tr>");
        }
    });
}
