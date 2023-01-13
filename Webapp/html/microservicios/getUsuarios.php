<?php
    
    include 'bdacc.php';
    // Create connection
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $cliente = $_POST["id_cliente"];
    //$cliente = 1;
    $table      = "v_usuarios";
    $sql        = "SELECT * FROM ".$table." WHERE ID_cliente=".$cliente." AND status=1";
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
           $datos[$numrecord]= array("ID_usuario"=>$row["ID_usuario"],"Nombre"=>utf8_encode($row["Nombre"]),"Apellido"=>utf8_encode($row["Apellido"]),"Correo"=>$row["Correo"],"Rol"=>$row["Rol"],"ID_Rol"=>$row["ID_Rol"]);
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