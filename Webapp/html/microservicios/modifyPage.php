<?php
    
    include 'bdacc.php';
    $conn = new mysqli($servername, $username, $passdb, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    
    $tablePagina     = "medida_clientes_pagina";
    $tableKits     = "medida_clientes_kits";
    $tableEsteri     = "medida_clientes_esterilizadores";
    $tableUsrs     = "medida_clientes_usrs";
    $tableDestino     = "medida_clientes_destinos";
    $tableKitsCont     = "medida_clientes_codigos_lista";
    $tableEquipos     = "medida_clientes_equipos";
//    $json = file_get_contents("php://input");
//    $decoded = json_decode($json);
//    $op         = $decoded->operacion;
    $op = $_POST["operacion"];
    switch ($op) {
        case 1:
            //Insert
            $titulo = $_POST["titulo"];
            $datos = $_POST["datos"];
            $tipo = $_POST["tipo"];
            $caducidad = $_POST["caducidad"];
            $idcliente = $_POST["id_cliente"];
            

            $sql        = "INSERT INTO ".$tablePagina." (ID_cliente,nombre,id_tipo) VALUES(".$idcliente.",'".$titulo."',".$tipo.");";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            $pagid = $conn->insert_id;
            switch($tipo)
            {
                case 1:
                    $sql        = "SELECT MAX(id_kit) as lastCode FROM ".$tableKits." WHERE ID_cliente = ".$idcliente.";";
                    $stmt1 = $conn->prepare($sql);
                    $stmt1->execute();
                    $resultado = $stmt1->get_result();
                    $tot = $resultado->num_rows;
                    $row	= $resultado->fetch_assoc();
                    if((int)$row["lastCode"] > 0)
                    {   
                        
                        $startingCode = (int)$row["lastCode"];
                        $startingCode++;
                        $startingCode = "1101".$startingCode;
                    }
                    else
                    {
                        $startingCode = "11011";
                    }
                    
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        $sqlx        = "INSERT INTO ".$tableKits." (ID_cliente,ID_pagina,codigo,descripcion,caducidad) VALUES(".$idcliente.",".$pagid.",'".$startingCode."','".$datos[$i]."',".$caducidad[$i].");";
                        $stmtx = $conn->prepare($sqlx);
                        $stmtx->execute();
                        $codigos[$i] = $conn->insert_id;
                        $startingCode++;
                    }

                    $bin = $_POST["bin"];
                    $list = $_POST["list"];
                    $cont = 0;
                    for($i = 0;$i<sizeof($bin);$i++)
                    {
                        if($bin[$i]=="1")
                        {

                            $temp = $list[$cont];
                            $cont++;
                            for($j = 0 ; $j<sizeof($temp);$j++)
                            {
                                $sqlx        = "INSERT INTO ".$tableKitsCont." (id_pagina,id_kit,id_itm,descripcion) VALUES(".$pagid.",".$codigos[$i].",".($j+1).",'".$temp[$j]."');";
                                $stmtx = $conn->prepare($sqlx);
                                $stmtx->execute();
                            }
                        }
                    }
                    
                    $datos=array("status"=>1,"msg"=>"Pagina de kits creada");
                    break;
                case 2:
                    $sql        = "SELECT MAX(id_usuario) as lastCode FROM ".$tableUsrs." WHERE ID_cliente = ".$idcliente.";";
                    $stmt1 = $conn->prepare($sql);
                    $stmt1->execute();
                    $resultado = $stmt1->get_result();
                    $tot = $resultado->num_rows;
                    $row	= $resultado->fetch_assoc();
                    if((int)$row["lastCode"] > 0)
                    {   
                        
                        $startingCode = (int)$row["lastCode"];
                        $startingCode++;
                        $startingCode = "1102".$startingCode;
                    }
                    else
                    {
                        $startingCode = "11021";
                    }
                    
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        $sqlx        = "INSERT INTO ".$tableUsrs." (ID_cliente,ID_pagina,codigo,descripcion) VALUES(".$idcliente.",".$pagid.",'".$startingCode."','".$datos[$i]."');";
                        $stmtx = $conn->prepare($sqlx);
                        $stmtx->execute();
                        $codigos[$i] = $conn->insert_id;
                        $startingCode++;
                    }
                    
                    $datos=array("status"=>1,"msg"=>"Pagina de usuarios creada");
                    break;
                case 3:
                    $sql        = "SELECT MAX(id_esterilizador) as lastCode FROM ".$tableEsteri." WHERE ID_cliente = ".$idcliente.";";
                    $stmt1 = $conn->prepare($sql);
                    $stmt1->execute();
                    $resultado = $stmt1->get_result();
                    $tot = $resultado->num_rows;
                    $row	= $resultado->fetch_assoc();
                    if((int)$row["lastCode"] > 0)
                    {   
                        $startingCode = (int)$row["lastCode"];
                        $startingCode++;
                        $startingCode = "1103".$startingCode;
                    }
                    else
                    {
                        $startingCode = "11031";
                    }
                    
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        $sqlx        = "INSERT INTO ".$tableEsteri." (ID_cliente,ID_pagina,codigo,descripcion) VALUES(".$idcliente.",".$pagid.",'".$startingCode."','".$datos[$i]."');";
                        $stmtx = $conn->prepare($sqlx);
                        $stmtx->execute();
                        $codigos[$i] = $conn->insert_id;
                        $startingCode++;
                    }
                    $datos=array("status"=>1,"msg"=>"Pagina de esterilizadores creada");
                    break;
                case 4:
                    $sql        = "SELECT MAX(id_destino) as lastCode FROM ".$tableDestino." WHERE ID_cliente = ".$idcliente.";";
                    $stmt1 = $conn->prepare($sql);
                    $stmt1->execute();
                    $resultado = $stmt1->get_result();
                    $tot = $resultado->num_rows;
                    $row	= $resultado->fetch_assoc();
                    if((int)$row["lastCode"] > 0)
                    {   
                        $startingCode = (int)$row["lastCode"];
                        $startingCode++;
                        $startingCode = "1106".$startingCode;
                    }
                    else
                    {
                        $startingCode = "11061";
                    }
                    
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        $sqlx        = "INSERT INTO ".$tableDestino." (ID_cliente,ID_pagina,codigo,descripcion) VALUES(".$idcliente.",".$pagid.",'".$startingCode."','".$datos[$i]."');";
                        $stmtx = $conn->prepare($sqlx);
                        $stmtx->execute();
                        $startingCode++;
                    }
                    $datos=array("status"=>1,"msg"=>"Pagina de destinos creada","sqlx"=>$sqlx,"sql"=>$sql);
                    break;
                    
            }
            $sql        = "UPDATE ".$tableEquipos." SET status=0 WHERE ID_cliente=".$idcliente.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            
            
            break;
        case 2:
            
            //Update
            $titulo = $_POST["titulo"];
            $datos = $_POST["datos"];
            $ids = $_POST["codigos"];
            $idcliente = $_POST["id_cliente"];
            $idpag = $_POST["id_pagina"];
            
            $sql        = "SELECT * FROM ".$tablePagina." WHERE ID_cliente = ".$idcliente." AND ID_pagina=".$idpag.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            $resultado = $stmt1->get_result();
            $row	= $resultado->fetch_assoc();
            $type = $row["id_tipo"];
            
            $sql        = "UPDATE ".$tablePagina." SET nombre='".$titulo."' WHERE ID_pagina=".$idpag.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            
            switch($type)
            {
                case "1":
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        if($ids[$i])
                        {
                            $sqlx        = "UPDATE ".$tableKits." SET descripcion='".$datos[$i]."',caducidad=".$caducidad[$i]." WHERE codigo='".$ids[$i]."';";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute();
                        }
                        else
                        {
                            $sql        = "SELECT MAX(id_kit) as lastCode FROM ".$tableKits." WHERE ID_cliente = ".$idcliente.";";
                            $stmt1 = $conn->prepare($sql);
                            $stmt1->execute();
                            $resultado = $stmt1->get_result();
                            $tot = $resultado->num_rows;
                            $row	= $resultado->fetch_assoc();
                            $startingCode = (int)$row["lastCode"];
                            $startingCode++;
                            $startingCode = "1101".$startingCode;
                            
                            $sqlx        = "INSERT INTO ".$tableKits." (ID_cliente,ID_pagina,codigo,descripcion,caducidad) VALUES(".$idcliente.",".$idpag.",'".$startingCode."','".$datos[$i]."',".$caducidad[$i].");";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute();
                        }
                    }
                    break;
                case "2":
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        if($ids[$i])
                        {
                           $sqlx        = "UPDATE ".$tableUsrs." SET descripcion='".$datos[$i]."' WHERE codigo='".$ids[$i]."';";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute(); 
                        }
                        else
                        {
                            $sql        = "SELECT MAX(id_usuario) as lastCode FROM ".$tableUsrs." WHERE ID_cliente = ".$idcliente.";";
                            $stmt1 = $conn->prepare($sql);
                            $stmt1->execute();
                            $resultado = $stmt1->get_result();
                            $row	= $resultado->fetch_assoc();
                            $startingCode = (int)$row["lastCode"];
                            $startingCode++;
                            $startingCode = "1102".$startingCode;
                            
                            $sqlx        = "INSERT INTO ".$tableUsrs." (ID_cliente,ID_pagina,codigo,descripcion) VALUES(".$idcliente.",".$idpag.",'".$startingCode."','".$datos[$i]."');";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute();
                        }
                        
                    }
                    break;
                case "3":
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        if($ids[$i])
                        {
                            $sqlx        = "UPDATE ".$tableEsteri." SET descripcion='".$datos[$i]."' WHERE codigo='".$ids[$i]."';";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute();
                        }
                        else
                        {
                            $sql        = "SELECT MAX(id_esterilizador) as lastCode FROM ".$tableEsteri." WHERE ID_cliente = ".$idcliente.";";
                            $stmt1 = $conn->prepare($sql);
                            $stmt1->execute();
                            $resultado = $stmt1->get_result();
                            $row	= $resultado->fetch_assoc();
                            $startingCode = (int)$row["lastCode"];
                            $startingCode++;
                            $startingCode = "1103".$startingCode;
                            
                            $sqlx        = "INSERT INTO ".$tableEsteri." (ID_cliente,ID_pagina,codigo,descripcion) VALUES(".$idcliente.",".$idpag.",'".$startingCode."','".$datos[$i]."');";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute();
                        }
                        
                    }
                    break;
                case "4":
                    for($i = 0;$i<sizeof($datos);$i++)
                    {
                        if($ids[$i])
                        {
                            $sqlx        = "UPDATE ".$tableDestino." SET descripcion='".$datos[$i]."' WHERE codigo='".$ids[$i]."';";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute();
                        }
                        else
                        {
                            $sql        = "SELECT MAX(id_destino) as lastCode FROM ".$tableDestino." WHERE ID_cliente = ".$idcliente.";";
                            $stmt1 = $conn->prepare($sql);
                            $stmt1->execute();
                            $resultado = $stmt1->get_result();
                            $row	= $resultado->fetch_assoc();
                            $startingCode = (int)$row["lastCode"];
                            $startingCode++;
                            $startingCode = "1104".$startingCode;
                            
                            $sqlx        = "INSERT INTO ".$tableDestino." (ID_cliente,ID_pagina,codigo,descripcion) VALUES(".$idcliente.",".$idpag.",'".$startingCode."','".$datos[$i]."');";
                            $stmtx = $conn->prepare($sqlx);
                            $stmtx->execute();
                        }
                        
                    }
                    break;
            }
            $datos=array("status"=>1,"msg"=>"Pagina actualizada","id_pagina"=>$idpag);
            $sql        = "UPDATE ".$tableEquipos." SET status=0 WHERE ID_cliente=".$idcliente.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            break;
        case 3:
            //Delete
            $idcliente  = $_POST["id_cliente"];
            $idusuario  = $_POST["id_usuario"];
            $sql        = "UPDATE ".$tablePagina." SET status=2 WHERE ID_cliente=".$idcliente." AND ID_usuario_cliente=".$idusuario.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            $sql        = "UPDATE ".$tableEquipos." SET status=0 WHERE ID_cliente=".$idcliente.";";
            $stmt1 = $conn->prepare($sql);
            $stmt1->execute();
            break;
    }

    
    $salida = json_encode($datos);
    header($_SERVER["SERVER_PROTOCOL"]." 200 OK"); 
    header('Content-Type: application/json; charset=utf-8');
    echo $salida;

    $conn->close();
?>