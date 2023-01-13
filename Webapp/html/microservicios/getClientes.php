<?php
    
    include 'bdacc.php';
    // Create connection
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    //$user = $_POST["status"];
    $table      = "v_clientes";
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
           $datos[$numrecord]= array("ID_cliente"=>$row["ID_cliente"],"Nombre"=>utf8_encode($row["Nombre"]),"Ciclos"=>$row["Ciclos"],"Equipos"=>$row["Equipos"],"Usuarios"=>$row["Usuarios"]);
           $row	= $resultado->fetch_assoc();
           ++$numrecord;
        }
        $stmt1->close();
    }
    else
    {
        $datos=array("status"=>0,"err"=>"ERROR: No hay usuarios");    
    }
    
    $salida = json_encode($datos);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>