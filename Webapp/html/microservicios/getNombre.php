<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $usuario = $_POST["id_usuario"];

    $table      = "medida_clientes_usuarios";
    $sql        = "SELECT * FROM ".$table." WHERE ID_usuario_cliente=".$usuario;
    $stmt1 = $conn->prepare($sql);
    $resultado  = $conn->query($sql);
    $row = $resultado->fetch_assoc();
    $nombre = $row["Nombre"]." ".$row["Apellido"];
    $datos=array("status"=>1,"nombre"=>$nombre);    
    
    $salida = json_encode($datos);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>