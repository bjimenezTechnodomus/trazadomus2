<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $id_cliente = $_POST["id_cliente"];

    $sql        = "SELECT *,(SELECT descripcion FROM medida_clientes_usrs AS B WHERE B.id_usuario = A.id_usuario) as usuario FROM bitacora_paquetes AS A WHERE A.id_cliente = ".$id_cliente." ORDER BY A.fecha desc;";

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
            $datosP[$j] = array("id_paquete"=>$row["id_paquete"],"codigo"=>$row["codigo"],"usuario"=>$row["usuario"],"descripcion"=>$row["descripcion"],"fecha"=>$row["fecha"],"caducidad"=>$row["caducidad"],"indicador"=>$row["indicador"]);
            $j++;
            $row = $resultado->fetch_assoc();
        }
        $datosS = array("status"=>1,"data"=>$datosP);
    }
    else
    {
        $datosS = array("status"=>0,"msg"=>"No hay paquetes para ese usuario y cliente");
    }
    
    $salida = json_encode($datosS);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>