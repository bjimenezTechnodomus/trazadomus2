-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 10.0.100.217    Database: db_trazadomus_dev
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bitacora_cambios_admin`
--

DROP TABLE IF EXISTS `bitacora_cambios_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bitacora_cambios_admin` (
  `ID_registro` int NOT NULL,
  `ID_usuario` int DEFAULT NULL,
  `Operacion` varchar(45) DEFAULT NULL,
  `Fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`ID_registro`),
  KEY `fk_bit_user_idx` (`ID_usuario`),
  CONSTRAINT `fk_bit_user` FOREIGN KEY (`ID_usuario`) REFERENCES `medida_usuarios_technodomus` (`ID_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bitacora_localizacion_paquete`
--

DROP TABLE IF EXISTS `bitacora_localizacion_paquete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bitacora_localizacion_paquete` (
  `id_registro` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int DEFAULT NULL,
  `id_equipo` int DEFAULT NULL,
  `id_registro_local` int DEFAULT NULL,
  `id_paquete` int DEFAULT NULL,
  `id_destino` int DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_registro`)
) ENGINE=InnoDB AUTO_INCREMENT=571 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bitacora_lotes`
--

DROP TABLE IF EXISTS `bitacora_lotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bitacora_lotes` (
  `id_registro` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int DEFAULT NULL,
  `id_equipo` int DEFAULT NULL,
  `id_lote` int DEFAULT NULL,
  `codigo` varchar(45) DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  `id_esterilizador` int DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `indicador` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`id_registro`),
  KEY `ID_cliente_idx` (`id_cliente`),
  KEY `ID_cliente_fk2_idx` (`id_cliente`),
  KEY `id_equipo_fk_idx` (`id_equipo`),
  CONSTRAINT `ID_cliente_fk2` FOREIGN KEY (`id_cliente`) REFERENCES `medida_clientes_usuarios` (`ID_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=146 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Informacion de lotes ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bitacora_lotes_contenido`
--

DROP TABLE IF EXISTS `bitacora_lotes_contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bitacora_lotes_contenido` (
  `id_registro` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int DEFAULT NULL,
  `id_equipo` int DEFAULT NULL,
  `id_registro_local` int DEFAULT NULL,
  `id_lote` int DEFAULT NULL,
  `id_paquete` int DEFAULT NULL,
  PRIMARY KEY (`id_registro`)
) ENGINE=InnoDB AUTO_INCREMENT=211 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bitacora_paquetes`
--

DROP TABLE IF EXISTS `bitacora_paquetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bitacora_paquetes` (
  `id_registro` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int DEFAULT NULL,
  `id_equipo` int DEFAULT NULL,
  `id_paquete` int DEFAULT NULL,
  `id_kit` int DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  `codigo` varchar(45) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `caducidad` datetime DEFAULT NULL,
  `indicador` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`id_registro`)
) ENGINE=InnoDB AUTO_INCREMENT=424 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `codigos_qr_comandos`
--

DROP TABLE IF EXISTS `codigos_qr_comandos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codigos_qr_comandos` (
  `id_comando` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(60) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_comando`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `codigos_qr_pre`
--

DROP TABLE IF EXISTS `codigos_qr_pre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codigos_qr_pre` (
  `id_pre` int NOT NULL AUTO_INCREMENT,
  `precodigo` varchar(45) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_pre`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimension_clientes_technodomus`
--

DROP TABLE IF EXISTS `dimension_clientes_technodomus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimension_clientes_technodomus` (
  `ID_cliente` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`ID_cliente`),
  KEY `stat_fk_idx` (`status`),
  CONSTRAINT `stat_fk` FOREIGN KEY (`status`) REFERENCES `dimension_status` (`id_status`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Informacion hospitales';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimension_roles`
--

DROP TABLE IF EXISTS `dimension_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimension_roles` (
  `ID_rol` int NOT NULL,
  `Descripcion_rol` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Informacion roles de permisos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimension_status`
--

DROP TABLE IF EXISTS `dimension_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimension_status` (
  `id_status` int NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimension_tipo`
--

DROP TABLE IF EXISTS `dimension_tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimension_tipo` (
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_codigos`
--

DROP TABLE IF EXISTS `medida_clientes_codigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_codigos` (
  `ID_codigo` int NOT NULL AUTO_INCREMENT,
  `ID_cliente` int DEFAULT NULL,
  `ID_pagina` int DEFAULT NULL,
  `codigo` varchar(60) DEFAULT NULL,
  `descripcion` varchar(60) DEFAULT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`ID_codigo`),
  KEY `id_cliente_fk_c_idx` (`ID_cliente`),
  KEY `id_pag_c_idx` (`ID_pagina`),
  CONSTRAINT `id_cliente_fk_c` FOREIGN KEY (`ID_cliente`) REFERENCES `dimension_clientes_technodomus` (`ID_cliente`),
  CONSTRAINT `id_pag_c` FOREIGN KEY (`ID_pagina`) REFERENCES `medida_clientes_pagina` (`ID_pagina`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Codigo QR';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_codigos_lista`
--

DROP TABLE IF EXISTS `medida_clientes_codigos_lista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_codigos_lista` (
  `id_lista` int NOT NULL AUTO_INCREMENT,
  `id_pagina` int DEFAULT NULL,
  `id_kit` int DEFAULT NULL,
  `id_itm` int DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_lista`),
  KEY `pag_list_idx` (`id_pagina`),
  KEY `cod_list_idx` (`id_kit`),
  CONSTRAINT `pag_list` FOREIGN KEY (`id_pagina`) REFERENCES `medida_clientes_pagina` (`ID_pagina`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_destinos`
--

DROP TABLE IF EXISTS `medida_clientes_destinos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_destinos` (
  `id_destino` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(60) DEFAULT NULL,
  `descripcion` varchar(60) DEFAULT NULL,
  `ID_pagina` int DEFAULT NULL,
  `ID_cliente` int DEFAULT NULL,
  PRIMARY KEY (`id_destino`),
  KEY `pag_dest_idx` (`ID_pagina`),
  KEY `cli_dest_idx` (`ID_cliente`),
  CONSTRAINT `cli_dest` FOREIGN KEY (`ID_cliente`) REFERENCES `dimension_clientes_technodomus` (`ID_cliente`),
  CONSTRAINT `pag_dest` FOREIGN KEY (`ID_pagina`) REFERENCES `medida_clientes_pagina` (`ID_pagina`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_equipos`
--

DROP TABLE IF EXISTS `medida_clientes_equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_equipos` (
  `ID_equipo` int NOT NULL AUTO_INCREMENT,
  `ID_cliente` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `ultima_actualizacion` datetime DEFAULT NULL,
  `ip` varchar(45) DEFAULT NULL,
  `mac` varchar(45) DEFAULT NULL,
  `candado1` int DEFAULT NULL,
  `candado2` int DEFAULT NULL,
  PRIMARY KEY (`ID_equipo`),
  UNIQUE KEY `ip_UNIQUE` (`ip`),
  KEY `ID_cliente_idx` (`ID_cliente`),
  CONSTRAINT `ID_clientesfk` FOREIGN KEY (`ID_cliente`) REFERENCES `medida_clientes_usuarios` (`ID_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Equipos y clientes';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_esterilizadores`
--

DROP TABLE IF EXISTS `medida_clientes_esterilizadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_esterilizadores` (
  `id_esterilizador` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(60) DEFAULT NULL,
  `descripcion` varchar(60) DEFAULT NULL,
  `ID_pagina` int DEFAULT NULL,
  `ID_cliente` int DEFAULT NULL,
  PRIMARY KEY (`id_esterilizador`),
  KEY `pag_esteri_idx` (`ID_pagina`),
  KEY `esteri_cli_idx` (`ID_cliente`),
  CONSTRAINT `esteri_cli` FOREIGN KEY (`ID_cliente`) REFERENCES `dimension_clientes_technodomus` (`ID_cliente`),
  CONSTRAINT `pag_esteri` FOREIGN KEY (`ID_pagina`) REFERENCES `medida_clientes_pagina` (`ID_pagina`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_kits`
--

DROP TABLE IF EXISTS `medida_clientes_kits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_kits` (
  `id_kit` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(60) DEFAULT NULL,
  `descripcion` varchar(60) DEFAULT NULL,
  `ID_pagina` int DEFAULT NULL,
  `ID_cliente` int DEFAULT NULL,
  `caducidad` int DEFAULT NULL,
  PRIMARY KEY (`id_kit`),
  UNIQUE KEY `codigo_UNIQUE` (`codigo`),
  KEY `pag_kit_idx` (`ID_pagina`),
  KEY `kit_cli_idx` (`ID_cliente`),
  CONSTRAINT `kit_cli` FOREIGN KEY (`ID_cliente`) REFERENCES `dimension_clientes_technodomus` (`ID_cliente`),
  CONSTRAINT `pag_kit` FOREIGN KEY (`ID_pagina`) REFERENCES `medida_clientes_pagina` (`ID_pagina`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_pagina`
--

DROP TABLE IF EXISTS `medida_clientes_pagina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_pagina` (
  `ID_pagina` int NOT NULL AUTO_INCREMENT,
  `ID_cliente` int DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `id_tipo` int DEFAULT NULL,
  PRIMARY KEY (`ID_pagina`),
  KEY `tipo_fk_idx` (`id_tipo`),
  CONSTRAINT `tipo_fk` FOREIGN KEY (`id_tipo`) REFERENCES `dimension_tipo` (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_usrs`
--

DROP TABLE IF EXISTS `medida_clientes_usrs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_usrs` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(60) DEFAULT NULL,
  `descripcion` varchar(60) DEFAULT NULL,
  `ID_pagina` int DEFAULT NULL,
  `ID_cliente` int DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  KEY `pag_usrs_idx` (`ID_pagina`),
  KEY `cliente_usr_idx` (`ID_cliente`),
  CONSTRAINT `cliente_usr` FOREIGN KEY (`ID_cliente`) REFERENCES `dimension_clientes_technodomus` (`ID_cliente`),
  CONSTRAINT `pag_usrs` FOREIGN KEY (`ID_pagina`) REFERENCES `medida_clientes_pagina` (`ID_pagina`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Usuarios de equipo de trazabilidad RPi';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_clientes_usuarios`
--

DROP TABLE IF EXISTS `medida_clientes_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_clientes_usuarios` (
  `ID_usuario_cliente` int NOT NULL AUTO_INCREMENT,
  `ID_cliente` int NOT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  `Correo` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `Rol` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`ID_usuario_cliente`),
  KEY `ID_cliente_idx` (`ID_cliente`),
  KEY `ID_rol_idx` (`Rol`),
  KEY `id_status_idx` (`status`),
  CONSTRAINT `ID_cliente_fk` FOREIGN KEY (`ID_cliente`) REFERENCES `dimension_clientes_technodomus` (`ID_cliente`),
  CONSTRAINT `ID_rol` FOREIGN KEY (`Rol`) REFERENCES `dimension_roles` (`ID_rol`),
  CONSTRAINT `id_status` FOREIGN KEY (`status`) REFERENCES `dimension_status` (`id_status`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Informacion clientes';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_usuarios_technodomus`
--

DROP TABLE IF EXISTS `medida_usuarios_technodomus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medida_usuarios_technodomus` (
  `ID_usuario` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  `Correo` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `Rol` int DEFAULT NULL,
  PRIMARY KEY (`ID_usuario`),
  KEY `ID_rolfk_idx` (`Rol`),
  CONSTRAINT `ID_rolfk` FOREIGN KEY (`Rol`) REFERENCES `dimension_roles` (`ID_rol`) ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Informacion usuarios techonodomus';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `v_clientes`
--

DROP TABLE IF EXISTS `v_clientes`;
/*!50001 DROP VIEW IF EXISTS `v_clientes`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_clientes` AS SELECT 
 1 AS `ID_cliente`,
 1 AS `Nombre`,
 1 AS `Equipos`,
 1 AS `Ciclos`,
 1 AS `Usuarios`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_equipos`
--

DROP TABLE IF EXISTS `v_equipos`;
/*!50001 DROP VIEW IF EXISTS `v_equipos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_equipos` AS SELECT 
 1 AS `ID_cliente`,
 1 AS `Nombre`,
 1 AS `ID_equipo`,
 1 AS `status`,
 1 AS `fecha`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_paginas`
--

DROP TABLE IF EXISTS `v_paginas`;
/*!50001 DROP VIEW IF EXISTS `v_paginas`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_paginas` AS SELECT 
 1 AS `ID_codigo`,
 1 AS `ID_cliente`,
 1 AS `ID_pagina`,
 1 AS `Codigo`,
 1 AS `nombre`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_usuarios`
--

DROP TABLE IF EXISTS `v_usuarios`;
/*!50001 DROP VIEW IF EXISTS `v_usuarios`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_usuarios` AS SELECT 
 1 AS `ID_cliente`,
 1 AS `ID_usuario`,
 1 AS `Nombre`,
 1 AS `Apellido`,
 1 AS `Correo`,
 1 AS `status`,
 1 AS `Rol`,
 1 AS `ID_Rol`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_clientes`
--

/*!50001 DROP VIEW IF EXISTS `v_clientes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_clientes` AS select `A`.`ID_cliente` AS `ID_cliente`,`A`.`Nombre` AS `Nombre`,(select count(distinct `B`.`ID_equipo`) from `medida_clientes_equipos` `B` where (`B`.`ID_cliente` = `A`.`ID_cliente`)) AS `Equipos`,(select count(distinct `C`.`id_registro`) from `bitacora_lotes` `C` where (`C`.`id_cliente` = `A`.`ID_cliente`)) AS `Ciclos`,(select count(distinct `D`.`ID_usuario_cliente`) from `medida_clientes_usuarios` `D` where ((`D`.`ID_cliente` = `A`.`ID_cliente`) and (`D`.`status` = 1))) AS `Usuarios` from `dimension_clientes_technodomus` `A` where (`A`.`status` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_equipos`
--

/*!50001 DROP VIEW IF EXISTS `v_equipos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_equipos` AS select `A`.`ID_cliente` AS `ID_cliente`,`B`.`Nombre` AS `Nombre`,`A`.`ID_equipo` AS `ID_equipo`,`A`.`status` AS `status`,`A`.`ultima_actualizacion` AS `fecha` from (`medida_clientes_equipos` `A` join `dimension_clientes_technodomus` `B`) where (`B`.`ID_cliente` = `A`.`ID_cliente`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_paginas`
--

/*!50001 DROP VIEW IF EXISTS `v_paginas`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_paginas` AS select `A`.`ID_codigo` AS `ID_codigo`,`A`.`ID_cliente` AS `ID_cliente`,`A`.`ID_pagina` AS `ID_pagina`,`A`.`codigo` AS `Codigo`,`B`.`nombre` AS `nombre` from (`medida_clientes_codigos` `A` join `medida_clientes_pagina` `B`) where (`B`.`ID_pagina` = `A`.`ID_pagina`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_usuarios`
--

/*!50001 DROP VIEW IF EXISTS `v_usuarios`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `v_usuarios` AS select `A`.`ID_cliente` AS `ID_cliente`,`A`.`ID_usuario_cliente` AS `ID_usuario`,`A`.`Nombre` AS `Nombre`,`A`.`Apellido` AS `Apellido`,`A`.`Correo` AS `Correo`,`A`.`status` AS `status`,`B`.`Descripcion_rol` AS `Rol`,`B`.`ID_rol` AS `ID_Rol` from (`medida_clientes_usuarios` `A` join `dimension_roles` `B`) where (`B`.`ID_rol` = `A`.`Rol`) group by `A`.`ID_usuario_cliente` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-15 13:34:39
