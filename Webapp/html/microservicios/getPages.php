<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $table     = "medida_clientes_pagina";
    $idcliente = $_POST["id_cliente"];
    
    $sql        = "SELECT * FROM ".$table." WHERE ID_cliente=".$idcliente;
    $stmt1 = $conn->prepare($sql);
    $stmt1->execute();
    $resultado = $stmt1->get_result();
    $row = $resultado->fetch_assoc();
    $i=0;
    $totzones = $resultado->num_rows;
    if($totzones > 0)
    {   
        while($row)
        { 

            $pagid = $row["ID_pagina"];
            $tipo = $row["id_tipo"];
            $datosP = [];
            switch($tipo)
            {
                case "1":
                    $table = "medida_clientes_kits";
                    $sql2        = "SELECT * FROM ".$table." WHERE ID_cliente=".$idcliente." AND ID_pagina=".$pagid;
                    $stmt2 = $conn->prepare($sql2);
                    $stmt2->execute();
                    $resultado2 = $stmt2->get_result();
                    $row2 = $resultado2->fetch_assoc();
                    $j = 0;
                    while($row2)
                    {
                        $datosP[$j] = array("id_pagina"=>$row2["ID_pagina"],"codigo"=>$row2["codigo"],"descripcion"=>$row2["descripcion"]);
                        $j++;
                        $row2 = $resultado2->fetch_assoc();
                    }
                    break;
                case "2":
                    $table = "medida_clientes_usrs";
                    $sql2        = "SELECT * FROM ".$table." WHERE ID_cliente=".$idcliente." AND ID_pagina=".$pagid;
                    $stmt2 = $conn->prepare($sql2);
                    $stmt2->execute();
                    $resultado2 = $stmt2->get_result();
                    $row2 = $resultado2->fetch_assoc();
                    $j = 0;
                    while($row2)
                    {
                        $datosP[$j] = array("id_pagina"=>$row2["ID_pagina"],"codigo"=>$row2["codigo"],"descripcion"=>$row2["descripcion"]);
                        $j++;
                        $row2 = $resultado2->fetch_assoc();
                    }
                    break;
                case "3":
                    $table = "medida_clientes_esterilizadores";
                    $sql2        = "SELECT * FROM ".$table." WHERE ID_cliente=".$idcliente." AND ID_pagina=".$pagid;
                    $stmt2 = $conn->prepare($sql2);
                    $stmt2->execute();
                    $resultado2 = $stmt2->get_result();
                    $row2 = $resultado2->fetch_assoc();
                    $j = 0;
                    while($row2)
                    {
                        $datosP[$j] = array("id_pagina"=>$row2["ID_pagina"],"codigo"=>$row2["codigo"],"descripcion"=>$row2["descripcion"]);
                        $j++;
                        $row2 = $resultado2->fetch_assoc();
                    }
                    break;
                case "4":
                    $table = "medida_clientes_destinos";
                    $sql2        = "SELECT * FROM ".$table." WHERE ID_cliente=".$idcliente." AND ID_pagina=".$pagid;
                    $stmt2 = $conn->prepare($sql2);
                    $stmt2->execute();
                    $resultado2 = $stmt2->get_result();
                    $row2 = $resultado2->fetch_assoc();
                    $j = 0;
                    while($row2)
                    {
                        $datosP[$j] = array("id_pagina"=>$row2["ID_pagina"],"codigo"=>$row2["codigo"],"descripcion"=>$row2["descripcion"]);
                        $j++;
                        $row2 = $resultado2->fetch_assoc();
                    }
                    break;

            }
            $datos[$i] = array("id_pagina"=>$row["ID_pagina"],"nombre"=>$row["nombre"],"id_tipo"=>$row["id_tipo"],"datos"=>$datosP);
            $i++;
            $row = $resultado->fetch_assoc();
        }

        $datosS = array("status"=>1,"datos"=>$datos);
    }
    else
    {
        $datosS = array("status"=>0,"msg"=>"No hay hojas creadas");
    }
    $salida = json_encode($datosS);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>