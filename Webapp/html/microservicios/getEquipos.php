<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    //$user = $_POST["status"];
    $table      = "v_equipos";
    $sql        = "SELECT * FROM ".$table.";";
    $stmt1 = $conn->prepare($sql);
    $stmt1->execute();
    $resultado = $stmt1->get_result();
    $totzones = $resultado->num_rows;

    $numrecord = 0;
    if($totzones > 0)
    {   
        $row	= $resultado->fetch_assoc();
        while ($row)
        {
           $datos[$numrecord]= array("ID_cliente"=>$row["ID_cliente"],"Nombre"=>utf8_encode($row["Nombre"]),"ID_equipo"=>$row["ID_equipo"],"status"=>$row["status"],"Fecha"=>$row["fecha"]);
           $row	= $resultado->fetch_assoc();
           ++$numrecord;
        }
        $stmt1->close();
    }
    else
    {
        $datos=array("status"=>0,"err"=>"ERROR: No hay equipos");    
    }
    
    $salida = json_encode($datos);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>