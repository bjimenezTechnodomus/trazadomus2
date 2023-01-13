<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $op         = $_POST["operacion"];
        
    $table      = "dimension_clientes_technodomus";

    switch ($op) {
        case 1:
            //Insert
            $nombre  = $_POST["nombre"];
            $sql        = "INSERT INTO ".$table." (Nombre,status) VALUES('".$nombre."',1);";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            
            break;
        case 2:
            //Update
            $nombre  = $_POST["nombre"];
            $idcliente  = $_POST["id_cliente"];
            $sql        = "UPDATE ".$table." SET Nombre='".$nombre."' WHERE ID_cliente=".$idcliente.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            
            break;
        case 3:
            //Delete o disable
            $idcliente  = $_POST["id_cliente"];
            $sql        = "UPDATE ".$table." SET status=2 WHERE ID_cliente=".$idcliente.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            break;
    }
    $datos=array("status"=>1,"msg"=>"Exito");   
    $salida = json_encode($datos);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>