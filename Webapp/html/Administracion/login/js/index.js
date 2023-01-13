$( document ).ready(function() {
    //Llamada de login a BD
    $("#login").click(function() {
        
        var sendData = {"correo":$("#correo").val(),"pass":$("#pass").val()};
        console.log(sendData); 
        $.post( "microservicios/login.php", sendData).done(function( data ) {
            
            var html = "https://"+ window.location.hostname + "/Administracion/";
            console.log(html)
            if( data.status == 1 )
            {
                sessionStorage.setItem("id_usuario",data["id_usuario"]);
                sessionStorage.setItem("nombre",data["nombre"]);
                window.location = html;
            }
            else
            {
                $("#alert").html("Usuario o contraseña incorrecta. Intente de nuevo.")
            }
            
        });

        
    });
    
});
