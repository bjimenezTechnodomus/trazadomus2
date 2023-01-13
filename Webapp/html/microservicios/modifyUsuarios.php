<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $op         = $_POST["operacion"];
        
    $table      = "medida_clientes_usuarios";

    switch ($op) {
        case 1:
            //Insert
            $nombre  = $_POST["nombre"];
            $apellido  = $_POST["apellido"];
            $correo  = $_POST["correo"];
            $idcliente  = $_POST["id_cliente"];
            $rol  = $_POST["rol"];
            $idcliente  = $_POST["id_cliente"];
            $sql        = "INSERT INTO ".$table." (ID_cliente,Nombre,Apellido,Correo,Password,Rol,status) VALUES(".$idcliente.",'".$nombre."','".$apellido."','".$correo."','temporal1',".$rol.",1);";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            
            break;
        case 2:
            
            //Update
            $nombre  = $_POST["nombre"];
            $apellido  = $_POST["apellido"];
            $correo  = $_POST["correo"];
            $idcliente  = $_POST["id_cliente"];
            $idusuario  = $_POST["id_usuario"];
            $rol  = $_POST["rol"];
            $sql        = "UPDATE ".$table." SET Nombre='".$nombre."',Apellido='".$apellido."',Correo='".$correo."',Rol=".$rol." WHERE ID_cliente=".$idcliente." AND ID_usuario_cliente=".$idusuario.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            $resultado = $stmt1->get_result();
            break;
        case 3:
            //Delete
            $idcliente  = $_POST["id_cliente"];
            $idusuario  = $_POST["id_usuario"];
            $sql        = "UPDATE ".$table." SET status=2 WHERE ID_cliente=".$idcliente." AND ID_usuario_cliente=".$idusuario.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            break;
    }

    $datos=array("status"=>1,"msg"=>"Exito", "res"=>$sql);   
    $salida = json_encode($datos);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>