<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $user = $_POST["correo"];
    $pass = $_POST["pass"];
    $table      = "medida_usuarios_technodomus";
    $sql        = "SELECT * FROM ".$table." WHERE Correo='".$user."' AND Password='".$pass."';";
    $resultado  = $conn->query($sql);
    $totzones   = $resultado->num_rows;
    $row = $resultado->fetch_assoc();
    if ($totzones > 0) 
    {
        $nombre = $row["Nombre"]." ".$row["Apellido"];
        $data = array("status"=>1,"msg"=>"Credenciales validas","nombre"=>$nombre,"id_usuario"=>$row["ID_usuario"]);
    }
    else
    {
        $data = array("status"=>0,"Credenciales invalidas");
    }

    $salida = json_encode($data);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

$conn->close();
    
?>