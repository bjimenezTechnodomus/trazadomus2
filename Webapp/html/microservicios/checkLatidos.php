<?php
    
    include 'bdacc.php';
    // Create connection
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    date_default_timezone_set('America/Mexico_City');

    $table      = "medida_clientes_equipos";
    $sql        = "SELECT * FROM ".$table;
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
            $fecha = $row["ultima_actualizacion"];
            $date1 = date_create($fecha);
            $hoy = new DateTime(date("Y-m-d H:i:s"));
            $interval = $date1->diff($hoy);
            if($interval->i>3)
            {
                $table2      = "medida_clientes_equipos";
                $sql2        = "UPDATE ".$table2." SET status=0 WHERE ID_equipo=".$row["ID_equipo"];
                $stmt2 = $conn->prepare($sql2);
                $stmt2->execute();
            }
            $row	= $resultado->fetch_assoc();
        }
        $stmt1->close();
        $datos=array("status"=>1,"ivl"=>$interval->i);  
    }
    else
    {
        $datos=array("status"=>0,"err"=>"ERROR: No hay equipos");  
    }
    

    echo json_encode($datos);

    $conn->close();
?>