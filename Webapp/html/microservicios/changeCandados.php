<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $cliente = $_POST["id_cliente"];
    $candado1 = $_POST["candado1"];
    $candado2 = $_POST["candado2"];

    $table      = "medida_clientes_equipos";
    $sql        = "UPDATE ".$table." SET candado1=".$candado1.",candado2=".$candado2." WHERE id_cliente=".$cliente.";";
    $stmt1 = $conn->prepare($sql);
    $stmt1->execute();

    $datos=array("status"=>1,"msg"=>"Candados actualizados.");    
    
    $salida = json_encode($datos);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>