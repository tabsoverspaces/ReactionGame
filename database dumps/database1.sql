-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: reaction_game
-- ------------------------------------------------------
-- Server version	5.5.54-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ranked_matches`
--

DROP TABLE IF EXISTS `ranked_matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ranked_matches` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `player1` varchar(30) DEFAULT NULL,
  `player2` varchar(30) DEFAULT NULL,
  `player1score` int(11) DEFAULT NULL,
  `player2score` int(11) DEFAULT NULL,
  `winner` varchar(30) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ranked_matches`
--

LOCK TABLES `ranked_matches` WRITE;
/*!40000 ALTER TABLE `ranked_matches` DISABLE KEYS */;
INSERT INTO `ranked_matches` VALUES (1,'Dragan','John',3,2,'Dragan','2017-04-21'),(2,'Trynd','Urgot',3,0,'Trynd','2017-04-22'),(5,'Daniel','Ted',3,2,'Daniel','2017-04-22'),(6,'Ron','Swanson',3,2,'Ron','2017-04-22'),(7,'Cable','Deadpool',3,1,'Cable','2017-04-22'),(8,'Superman','Batman',3,2,'Superman','2017-04-22'),(9,'Goku','Saitama',3,0,'Goku','2017-04-22'),(10,'Kennen','Shen',3,2,'Kennen','2017-04-22'),(11,'Ian','McGregor',3,2,'Ian','2017-04-22');
/*!40000 ALTER TABLE `ranked_matches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ranking`
--

DROP TABLE IF EXISTS `ranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ranking` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `best_time` decimal(15,3) DEFAULT NULL,
  `avg_time` decimal(15,3) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ranking`
--

LOCK TABLES `ranking` WRITE;
/*!40000 ALTER TABLE `ranking` DISABLE KEYS */;
INSERT INTO `ranking` VALUES (1,0.234,0.319,'Dragan'),(2,0.222,0.299,'John'),(3,0.252,0.365,'Michael'),(4,0.301,0.355,'Trinity'),(5,0.205,0.442,'Aaron\n'),(6,0.372,0.307,'Aatrox\n'),(7,0.357,0.293,'Benny\n'),(8,0.333,0.460,'Baron\n'),(9,0.270,0.299,'Crystal\n'),(10,0.394,0.448,'Caroline\n'),(11,0.241,0.390,'Dmitri\n'),(12,0.280,0.408,'Evan\n'),(13,0.339,0.298,'Fernando\n'),(14,0.276,0.311,'Ian\n'),(15,0.397,0.368,'Jupiter\n'),(16,0.289,0.393,'Jun\n'),(17,0.380,0.419,'Ken\n'),(18,0.323,0.365,'Kristen\n'),(19,0.203,0.324,'Mowgli\n'),(20,0.309,0.372,'Negan\n'),(21,0.388,0.261,'Onyr\n'),(22,0.379,0.426,'Risto\n'),(23,0.317,0.345,'Peng\n'),(24,0.202,0.356,'Wallace\n'),(25,0.327,0.421,'Wladimir\n'),(26,0.335,0.273,'Xiyah\n'),(27,0.289,0.257,'Zed'),(29,0.283,0.283,'Urgot'),(32,0.187,0.235,'Edgar'),(33,0.173,0.181,'Daniel'),(34,0.169,0.179,'Ron'),(35,0.181,0.186,'Cable'),(36,0.162,0.178,'Superman'),(37,0.171,0.564,'Goku'),(38,0.140,0.498,'Kennen'),(39,0.314,0.727,'Ian');
/*!40000 ALTER TABLE `ranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tournaments`
--

DROP TABLE IF EXISTS `tournaments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tournaments` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `p1` varchar(30) DEFAULT NULL,
  `p2` varchar(30) DEFAULT NULL,
  `p3` varchar(30) DEFAULT NULL,
  `p4` varchar(30) DEFAULT NULL,
  `p5` varchar(30) DEFAULT NULL,
  `p6` varchar(30) DEFAULT NULL,
  `p7` varchar(30) DEFAULT NULL,
  `p8` varchar(30) DEFAULT NULL,
  `winner` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tournaments`
--

LOCK TABLES `tournaments` WRITE;
/*!40000 ALTER TABLE `tournaments` DISABLE KEYS */;
/*!40000 ALTER TABLE `tournaments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-22 16:43:17
