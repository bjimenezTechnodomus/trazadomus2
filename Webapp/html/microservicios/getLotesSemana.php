<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $table     = "medida_clientes_pagina";
    $id_cliente = $_POST["id_cliente"];
    //$id_cliente = $_POST["id_cliente"];
    //$id_usuario = $_POST["id_usuario"];
    $date = date('Y-m-d');
    $sql        = "SELECT DATE_FORMAT(fecha,'%Y-%m-%d') as dia,count(id_lote) as cuenta FROM bitacora_lotes WHERE id_cliente=".$id_cliente." AND fecha >= DATE_ADD('".$date."', INTERVAL(-WEEKDAY('".$date."')) DAY) GROUP BY dia;";

    $stmt1 = $conn->prepare($sql);
    $stmt1->execute();
    $resultado = $stmt1->get_result();
    $row = $resultado->fetch_assoc();
    $totzones = $resultado->num_rows;
    $j=0;
    if($totzones > 0)
    {   
        while($row)
        {
            $datosP[$j] = array("dia"=>$row["dia"],"cuenta"=>$row["cuenta"]);
            $j++;
            $row = $resultado->fetch_assoc();
        }
        $datosS = array("status"=>1,"data"=>$datosP);
    }
    else
    {
        $datosS = array("status"=>0,"msg"=>"No hay lotes esta semana");
    }
    
    $salida = json_encode($datosS);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>