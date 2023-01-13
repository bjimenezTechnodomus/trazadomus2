-- MariaDB dump 10.19  Distrib 10.5.15-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: trazadomus
-- ------------------------------------------------------
-- Server version	10.5.15-MariaDB-0+deb11u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dimension_indicador`
--

DROP TABLE IF EXISTS `dimension_indicador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimension_indicador` (
  `id_indicador` int(11) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_indicador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimension_lotes`
--

DROP TABLE IF EXISTS `dimension_lotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimension_lotes` (
  `id_lote` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(45) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_esterilizador` int(11) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `indicador` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `status_nube` int(11) DEFAULT 0,
  PRIMARY KEY (`id_lote`),
  UNIQUE KEY `codigo_UNIQUE` (`codigo`),
  KEY `lotes_esterilizador_idx` (`id_esterilizador`),
  KEY `lotes_usuarios_idx` (`id_usuario`),
  CONSTRAINT `lotes_esterilizador` FOREIGN KEY (`id_esterilizador`) REFERENCES `medida_esterilizadores` (`id_esterilizador`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `lotes_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `medida_usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimension_pre_codigos`
--

DROP TABLE IF EXISTS `dimension_pre_codigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimension_pre_codigos` (
  `id_pre` int(11) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_pre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimension_status_paquetes`
--

DROP TABLE IF EXISTS `dimension_status_paquetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimension_status_paquetes` (
  `id_status` int(11) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_destinos`
--

DROP TABLE IF EXISTS `medida_destinos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medida_destinos` (
  `id_destino` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(45) DEFAULT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_destino`),
  UNIQUE KEY `codigo_UNIQUE` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_esterilizadores`
--

DROP TABLE IF EXISTS `medida_esterilizadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medida_esterilizadores` (
  `id_esterilizador` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_esterilizador`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_kits`
--

DROP TABLE IF EXISTS `medida_kits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medida_kits` (
  `id_kit` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `caducidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_kit`),
  UNIQUE KEY `codigo_UNIQUE` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_localizacion_paquete`
--

DROP TABLE IF EXISTS `medida_localizacion_paquete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medida_localizacion_paquete` (
  `id_registro` int(11) NOT NULL AUTO_INCREMENT,
  `id_paquete` int(11) DEFAULT NULL,
  `id_destino` int(11) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `status_nube` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_registro`),
  KEY `paquete_destino_idx` (`id_paquete`),
  KEY `destino_id_idx` (`id_destino`),
  CONSTRAINT `destino_id` FOREIGN KEY (`id_destino`) REFERENCES `medida_destinos` (`id_destino`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `paquete_destino` FOREIGN KEY (`id_paquete`) REFERENCES `medida_paquetes` (`id_paquete`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=245 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_lotes_contenido`
--

DROP TABLE IF EXISTS `medida_lotes_contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medida_lotes_contenido` (
  `id_registro` int(11) NOT NULL AUTO_INCREMENT,
  `id_lote` int(11) DEFAULT NULL,
  `id_paquete` int(11) DEFAULT NULL,
  `status_nube` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_registro`),
  KEY `contenido_lote_idx` (`id_lote`),
  KEY `contenido_paquete_idx` (`id_paquete`),
  CONSTRAINT `contenido_lote` FOREIGN KEY (`id_lote`) REFERENCES `dimension_lotes` (`id_lote`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `contenido_paquete` FOREIGN KEY (`id_paquete`) REFERENCES `medida_paquetes` (`id_paquete`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_paquetes`
--

DROP TABLE IF EXISTS `medida_paquetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medida_paquetes` (
  `id_paquete` int(11) NOT NULL AUTO_INCREMENT,
  `id_kit` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `codigo` varchar(45) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `caducidad` datetime DEFAULT NULL,
  `indicador` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `status_nube` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_paquete`),
  UNIQUE KEY `codigo_UNIQUE` (`codigo`),
  KEY `paquete_kit_idx` (`id_kit`),
  KEY `paquete_usuarios_idx` (`id_usuario`),
  CONSTRAINT `paquete_kit` FOREIGN KEY (`id_kit`) REFERENCES `medida_kits` (`id_kit`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `paquete_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `medida_usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medida_usuarios`
--

DROP TABLE IF EXISTS `medida_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medida_usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `codigo_UNIQUE` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-15 19:19:19
