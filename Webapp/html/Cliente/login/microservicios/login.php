<?php
    
    include 'bdacc.php';
    // Create connection
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $user = $_POST["correo"];
    $pass = $_POST["pass"];
    $table      = "medida_clientes_usuarios";
    $sql        = "SELECT * FROM ".$table." WHERE Correo='".$user."' AND Password='".$pass."';";
    $resultado  = $conn->query($sql);
    $totzones   = $resultado->num_rows;
    $row = $resultado->fetch_assoc();
    if ($totzones > 0) 
    {
        $data = array("status"=>1,"msg"=>"Credenciales validas","rol"=>$row["Rol"],"id_cliente"=>$row["ID_cliente"],"id_usuario"=>$row["ID_usuario_cliente"]);
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