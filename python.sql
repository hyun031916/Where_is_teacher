-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: python
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `teacherseat`
--

DROP TABLE IF EXISTS `teacherseat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacherseat` (
  `seatnum` int NOT NULL,
  `teacher` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `message` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`seatnum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacherseat`
--

LOCK TABLES `teacherseat` WRITE;
/*!40000 ALTER TABLE `teacherseat` DISABLE KEYS */;
INSERT INTO `teacherseat` VALUES (1,1,1,''),(2,19,1,''),(3,17,1,''),(4,2,1,''),(5,41,1,''),(6,8,1,''),(7,32,1,''),(8,34,1,''),(9,0,-1,NULL),(10,0,-1,NULL),(11,46,1,''),(12,39,1,''),(13,4,1,''),(14,14,1,''),(15,31,1,''),(16,16,1,''),(17,0,-1,NULL),(18,0,-1,NULL),(19,10,1,''),(20,22,1,''),(21,26,1,''),(22,28,1,''),(23,33,1,''),(24,7,1,''),(25,42,1,''),(26,30,1,''),(27,0,-1,NULL),(28,0,-1,NULL),(29,23,1,''),(30,25,1,'');
/*!40000 ALTER TABLE `teacherseat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tschedule`
--

DROP TABLE IF EXISTS `tschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `Monday1` varchar(45) DEFAULT NULL,
  `Monday2` varchar(45) DEFAULT NULL,
  `Monday3` varchar(45) DEFAULT NULL,
  `Monday4` varchar(45) DEFAULT NULL,
  `Monday5` varchar(45) DEFAULT NULL,
  `Monday6` varchar(45) DEFAULT NULL,
  `Monday7` varchar(45) DEFAULT NULL,
  `Tuesday1` varchar(45) DEFAULT NULL,
  `Tuesday2` varchar(45) DEFAULT NULL,
  `Tuesday3` varchar(45) DEFAULT NULL,
  `Tuesday4` varchar(45) DEFAULT NULL,
  `Tuesday5` varchar(45) DEFAULT NULL,
  `Tuesday6` varchar(45) DEFAULT NULL,
  `Tuesday7` varchar(45) DEFAULT NULL,
  `Wednesday1` varchar(45) DEFAULT NULL,
  `Wednesday2` varchar(45) DEFAULT NULL,
  `Wednesday3` varchar(45) DEFAULT NULL,
  `Wednesday4` varchar(45) DEFAULT NULL,
  `Wednesday5` varchar(45) DEFAULT NULL,
  `Wednesday6` varchar(45) DEFAULT NULL,
  `Wednesday7` varchar(45) DEFAULT NULL,
  `Thursday1` varchar(45) DEFAULT NULL,
  `Thursday2` varchar(45) DEFAULT NULL,
  `Thursday3` varchar(45) DEFAULT NULL,
  `Thursday4` varchar(45) DEFAULT NULL,
  `Thursday5` varchar(45) DEFAULT NULL,
  `Thursday6` varchar(45) DEFAULT NULL,
  `Thursday7` varchar(45) DEFAULT NULL,
  `Friday1` varchar(45) DEFAULT NULL,
  `Friday2` varchar(45) DEFAULT NULL,
  `Friday3` varchar(45) DEFAULT NULL,
  `Friday4` varchar(45) DEFAULT NULL,
  `Friday5` varchar(45) DEFAULT NULL,
  `Friday6` varchar(45) DEFAULT NULL,
  `Friday7` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tschedule`
--

LOCK TABLES `tschedule` WRITE;
/*!40000 ALTER TABLE `tschedule` DISABLE KEYS */;
INSERT INTO `tschedule` VALUES (0,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1,'이철호',NULL,NULL,'1-4','1-6',NULL,NULL,NULL,NULL,'1-3',NULL,NULL,NULL,NULL,'1-5','1-2',NULL,'1-1','1-6',NULL,NULL,NULL,NULL,NULL,NULL,'1-4',NULL,NULL,'1-1',NULL,'1-3',NULL,'1-2',NULL,NULL,'1-5'),(2,'김영철',NULL,'1-6',NULL,'1-5',NULL,NULL,'1-1','1-5',NULL,NULL,'1-1',NULL,'1-4','1-2',NULL,NULL,'1-6','1-3','1-4',NULL,NULL,'1-1',NULL,'1-4','1-3','1-2',NULL,NULL,'1-5',NULL,NULL,'1-6','1-2',NULL,'1-3'),(3,'이대형',NULL,'1-2',NULL,'1-4','1-1',NULL,'1-6','1-3',NULL,'1-6','1-5','1-1',NULL,NULL,'1-5',NULL,NULL,'2-5','1-3',NULL,NULL,NULL,'2-3',NULL,NULL,'2-6','1-2',NULL,'2-2','1-4',NULL,'','2-4','2-1',NULL),(4,'최영진','3-5',NULL,'3-6',NULL,'소프트웨어3',NULL,'웹솔과3',NULL,'2-6',NULL,'3-6',NULL,NULL,'3-5',NULL,NULL,NULL,NULL,'2-2',NULL,NULL,NULL,'2-4',NULL,NULL,NULL,NULL,'소프트웨어3',NULL,NULL,'2-5','웹솔루션3','2-1','2-3',NULL),(5,'박향규',NULL,NULL,'2-6',NULL,NULL,'2-4',NULL,'2-4',NULL,'2-3',NULL,NULL,NULL,NULL,NULL,'2-2',NULL,NULL,'2-1',NULL,NULL,NULL,'2-5','2-6',NULL,'2-1',NULL,'2-3',NULL,NULL,NULL,'2-5','2-2',NULL,NULL),(6,'고낙은','','1-1','3-5','3-2','','1-3',NULL,NULL,'','1-5','1-6','','1-3','3-1','3-4','1-5','1-2',NULL,NULL,NULL,NULL,'','1-1','','1-6','1-4','','3-6','','1-2','3-3','','1-4',NULL,NULL),(7,'김보경','1-6',NULL,NULL,'3-5',NULL,'1-1','3-6',NULL,NULL,NULL,'1-2','1-5',NULL,NULL,NULL,'1-2',NULL,'1-4','3-3',NULL,NULL,NULL,'1-3',NULL,'1-1','1-6',NULL,NULL,'1-4','1-5',NULL,NULL,'3-4','1-3',NULL),(8,'권지웅','2-6',NULL,'2-5',NULL,NULL,NULL,'2-3',NULL,NULL,NULL,'2-2',NULL,'2-6','2-5','2-5',NULL,'2-3','2-1','2-4',NULL,NULL,'2-3',NULL,'2-4','2-1','2-2',NULL,NULL,'2-1','2-6',NULL,NULL,NULL,'2-4','2-2'),(9,'정혜선',NULL,'2-6',NULL,'2-1','디자인1',NULL,NULL,NULL,'2-1',NULL,NULL,NULL,NULL,'2-6','2-2','2-5',NULL,NULL,'디자인1',NULL,NULL,'','2-6',NULL,NULL,'2-5',NULL,'2-2','2-5',NULL,'디자인1',NULL,NULL,'2-2','2-1'),(10,'최정아','소프트웨어1','2-6',NULL,NULL,'디자인1',NULL,NULL,NULL,NULL,'소프트웨어1',NULL,'웹솔루션1',NULL,'2-6',NULL,'2-5','웹솔루션1',NULL,'디자인1',NULL,NULL,NULL,'2-6',NULL,NULL,'2-5',NULL,NULL,'2-5',NULL,'디자인1','웹솔루션1',NULL,'소프트웨어1',NULL),(11,'이은주','소프트웨어1',NULL,NULL,NULL,'디자인1',NULL,'2-4','2-3',NULL,'소프트웨어1','2-4','웹솔루션1',NULL,NULL,NULL,NULL,'웹솔루션1',NULL,'디자인1',NULL,NULL,'2-4',NULL,'2-3',NULL,NULL,NULL,NULL,NULL,'2-3','디자인1','웹솔루션1',NULL,'소프트웨어1',NULL),(12,'윤성웅',NULL,NULL,NULL,'2-1',NULL,NULL,'2-4','2-3','2-1',NULL,'2-4',NULL,NULL,NULL,'2-2',NULL,NULL,NULL,NULL,NULL,NULL,'2-4',NULL,'2-3',NULL,NULL,NULL,'2-2',NULL,'2-3',NULL,NULL,NULL,'2-2','2-1'),(13,'이세호','3-4','3-3',NULL,NULL,NULL,'3-2','3-1',NULL,NULL,'3-1',NULL,'3-4','3-3','3-2',NULL,'3-4',NULL,NULL,'3-2',NULL,NULL,NULL,NULL,NULL,'','3-3','3-1','','3-4',NULL,'','3-2','3-3',NULL,'3-1'),(14,'김지훈','소프트웨어1',NULL,NULL,'3-6','',NULL,'3-5','','3-5','소프트웨어1',NULL,'웹솔루션1',NULL,'3-6','',NULL,'웹솔루션1',NULL,'3-6',NULL,'',NULL,'3-6',NULL,'',NULL,'','3-5',NULL,'','','웹솔루션1','','소프트웨어1','3-5'),(15,'김윤환',NULL,'1-4','1-2',NULL,'1-3','1-6',NULL,NULL,'1-5',NULL,'1-4','1-2',NULL,'1-1',NULL,NULL,NULL,'1-5','1-1',NULL,NULL,'1-3','','1-6','1-2',NULL,'','1-4','1-1','',NULL,'1-5','1-3','','1-6'),(16,'송민정','웹솔루션1',NULL,'디자인1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'','디자인2','소프트웨어1','웹솔루션1',NULL,NULL,'','소프트웨어1','디자인2',NULL,'','디자인2','','소프트웨어1','',NULL,'','','디자인1','','웹솔루션1','','디자인2','디자인1',NULL),(17,'우호식',NULL,NULL,'디자인1','웹솔루션2',NULL,NULL,NULL,'소프트웨어2','웹솔루션2',NULL,NULL,NULL,'소프트웨어1',NULL,NULL,'','소프트웨어2','디자인1',NULL,NULL,'',NULL,'','소프트웨어1','웹솔루션2','','소프트웨어2','디자인1','','소프트웨어2',NULL,NULL,NULL,'디자인1','웹솔루션2'),(18,'박성래',NULL,NULL,NULL,'웹솔루션2','소프트웨어3',NULL,'웹솔루션3','소프트웨어2','웹솔루션2',NULL,NULL,'디자인2',NULL,NULL,NULL,NULL,'소프트웨어2',NULL,'디자인2',NULL,NULL,'디자인2',NULL,NULL,'웹솔루션2',NULL,'소프트웨어2','디자인3',NULL,'소프트웨어2',NULL,'웹솔루션3','디자인2',NULL,'웹솔루션2'),(19,'이호연','웹솔루션1',NULL,NULL,'웹솔루션2',NULL,NULL,NULL,'소프트웨어2','웹솔루션2',NULL,NULL,'디자인2',NULL,'웹솔루션1',NULL,NULL,'소프트웨어2',NULL,'디자인2',NULL,NULL,'디자인2',NULL,NULL,'웹솔루션2',NULL,'소프트웨어2',NULL,NULL,'소프트웨어2','웹솔루션1',NULL,'디자인2',NULL,'웹솔루션2'),(20,'이규응',NULL,NULL,NULL,NULL,NULL,'1-4','1-4',NULL,'1-4',NULL,NULL,NULL,NULL,NULL,'1-1','1-1',NULL,NULL,NULL,NULL,NULL,'1-2','1-2',NULL,NULL,'1-3','1-3',NULL,'1-3','1-1','1-2',NULL,NULL,NULL,NULL),(21,'이철희','소프트웨어3','소프트웨어3',NULL,NULL,'3-4','3-4',NULL,NULL,NULL,'웹솔루션3','웹솔루션3',NULL,NULL,NULL,NULL,'','소프트웨어3','소프트웨어3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'웹솔루션3','웹솔루션3','3-3','3-3',NULL,NULL,NULL,NULL,NULL),(22,'권오재','소프트웨어3','소프트웨어3',NULL,'1-2','1-2',NULL,NULL,NULL,NULL,'웹솔루션3','웹솔루션3',NULL,NULL,NULL,NULL,NULL,'3소','소프트웨어3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'웹솔루션3','웹솔루션3',NULL,'','1-1','1-1',NULL,NULL,NULL),(23,'이재민',NULL,NULL,NULL,NULL,'2-2',NULL,'2-1',NULL,'2-2','2-2',NULL,NULL,NULL,NULL,'2-3','2-3',NULL,NULL,NULL,NULL,NULL,'2-1','2-1',NULL,NULL,NULL,NULL,'2-4',NULL,'','2-4','2-4','2-3',NULL,NULL),(24,'이선희','3-3',NULL,'3-4','3-4',NULL,NULL,NULL,'3-3','3-3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3-4','3-4',NULL,NULL,NULL,NULL,NULL,'3-3','3-3','3-4',NULL,NULL,'3-6','3-6',NULL,NULL,'3-5','3-5',NULL),(25,'이호걸',NULL,NULL,NULL,'1-1','','2-2','2-2','1-2','1-2',NULL,NULL,NULL,NULL,NULL,'2-1','2-1',NULL,NULL,NULL,NULL,NULL,'2-2','2-2',NULL,NULL,'1-1','1-1',NULL,NULL,NULL,'2-1','2-1',NULL,NULL,'1-2'),(26,'민주리','',NULL,NULL,NULL,NULL,'1-2','1-2','1-1','1-1','',NULL,'3-1','3-1',NULL,'3-2','3-2',NULL,NULL,NULL,NULL,NULL,'',NULL,'3-1','3-1',NULL,NULL,'1-2',NULL,'3-2','3-2',NULL,'1-1',NULL,NULL),(27,'신혜정','개발과2','개발과2','개발과2',NULL,NULL,NULL,NULL,'','','1-3','1-3','','',NULL,'1-4','1-4',NULL,NULL,'',NULL,NULL,'소프트웨어3','소프트웨어3',NULL,NULL,NULL,'1-4','1-3',NULL,NULL,NULL,NULL,'소프트웨어3','소프트웨어3',NULL),(28,'백현정',NULL,NULL,NULL,'3-3',NULL,NULL,'1-3','1-4',NULL,'2-1','2-1',NULL,NULL,NULL,'1-3','1-3',NULL,NULL,NULL,NULL,NULL,'1-4','1-4',NULL,NULL,NULL,NULL,'2-1',NULL,NULL,'2-2','2-2',NULL,NULL,NULL),(29,'최규정',NULL,'3-4','3-3','3-3',NULL,NULL,NULL,'3-4','3-4',NULL,NULL,'3-3',NULL,NULL,NULL,NULL,'3-3','3-3',NULL,NULL,NULL,'소프트웨어3','소프트웨어3',NULL,NULL,NULL,NULL,NULL,NULL,'3-4','3-4',NULL,'소프트웨어3','소프트웨어3',NULL),(30,'함기훈','웹솔루션2','웹솔루션2','웹솔루션2',NULL,NULL,NULL,NULL,'3-1','3-1',NULL,NULL,'3-2','3-2',NULL,NULL,NULL,NULL,NULL,'3-1',NULL,NULL,NULL,NULL,NULL,'','3-2','3-2',NULL,'3-2',NULL,'3-1','3-1',NULL,NULL,NULL),(31,'임정훈',NULL,NULL,NULL,NULL,'2-3','2-3',NULL,NULL,NULL,NULL,NULL,'소프트웨어2','소프트웨어2','소프트웨어2',NULL,NULL,NULL,'2-3','2-3',NULL,NULL,'웹솔루션3','웹솔루션3',NULL,NULL,'2-4','2-4',NULL,'2-4','2-4',NULL,NULL,NULL,'웹솔루션3','웹솔루션3'),(32,'유병석',NULL,NULL,'3-1','3-1',NULL,NULL,NULL,'3-2','3-2',NULL,NULL,'소프트웨어2','소프트웨어2','소프트웨어2','3-1','3-1',NULL,NULL,NULL,NULL,NULL,'','','3-2','3-2','3-1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3-2'),(33,'박지우','소프트웨어2','소프트웨어2','소프트웨어2',NULL,'2-1','2-1',NULL,NULL,NULL,NULL,NULL,'웹솔루션2','웹솔루션2','웹솔루션2',NULL,NULL,'2-4','2-4',NULL,NULL,NULL,NULL,NULL,'2-2','2-2',NULL,NULL,NULL,NULL,NULL,'2-3','2-3',NULL,NULL,NULL),(34,'이형섭','소프트웨어2','소프트웨어2','소프트웨어2',NULL,'2-4',NULL,NULL,NULL,NULL,NULL,NULL,'웹솔루션2','웹솔루션2','웹솔루션2','2-4','2-4',NULL,NULL,NULL,NULL,NULL,'웹솔루션3','웹솔루션3',NULL,NULL,'2-3','2-3',NULL,'2-3',NULL,NULL,NULL,NULL,'웹솔루션3','웹솔루션3'),(35,'이종태',NULL,'3-5','3-2',NULL,NULL,'3-1',NULL,NULL,NULL,'3-2','3-2',NULL,NULL,'3-3',NULL,NULL,NULL,NULL,'3-4',NULL,NULL,'3-6',NULL,NULL,NULL,NULL,'2-5','2-5','3-1','3-1',NULL,NULL,NULL,'2-6','2-6'),(36,'이정임',NULL,NULL,'1-1','1-3','1-4',NULL,'3-2',NULL,NULL,'1-4','3-1',NULL,NULL,'1-6',NULL,NULL,'1-5',NULL,'1-2',NULL,NULL,NULL,NULL,'1-3',NULL,NULL,'1-6',NULL,'1-2',NULL,NULL,NULL,'1-5',NULL,'1-1'),(37,'김종성','1-5','1-5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1-6','1-6',NULL,'1-6','1-6','디자인3','디자인3',NULL,NULL,NULL,NULL,NULL,'1-5','1-5',NULL,NULL,NULL,NULL,NULL,'디자인3','디자인3',NULL,'',''),(38,'김명준',NULL,NULL,NULL,NULL,'디자인3','디자인3',NULL,'2-5','2-5',NULL,NULL,'디자인3','디자인3',NULL,NULL,'','2-6','2-6',NULL,NULL,NULL,'웹솔루션3','웹솔루션3',NULL,'','디자인3','디자인3','','2-6','2-5',NULL,NULL,NULL,'웹솔루션3','웹솔루션3'),(39,'김민혜','웹솔루션2','웹솔루션2','웹솔루션2',NULL,NULL,NULL,NULL,'3-5',NULL,'3-6',NULL,NULL,'1-5',NULL,'3-5','3-5',NULL,NULL,NULL,NULL,NULL,'1-6','1-6',NULL,NULL,'1-5','1-5',NULL,NULL,NULL,NULL,NULL,'1-6','3-6','3-6'),(40,'이하얀','3-6','3-6',NULL,NULL,NULL,'1-5','1-5','2-6',NULL,'3-5','3-5',NULL,'2-5',NULL,NULL,NULL,NULL,NULL,'3-5',NULL,NULL,NULL,NULL,'3-5','3-5',NULL,'2-6','2-6','1-6','1-6',NULL,NULL,'3-6',NULL,NULL),(41,'박진형',NULL,NULL,NULL,'디자인2','3-3','3-3',NULL,'','','디자인2','디자인2',NULL,'3-4','3-4','3-3','3-3','디자인3','디자인3',NULL,NULL,NULL,NULL,NULL,'3-4','3-4',NULL,NULL,NULL,NULL,NULL,'디자인3','디자인3',NULL,NULL,NULL),(42,'김민주','2-5','2-5',NULL,'','디자인3','디자인3','','1-6','1-6',NULL,NULL,'디자인3','디자인3',NULL,'2-6','2-6',NULL,NULL,NULL,NULL,NULL,'1-5','1-5',NULL,NULL,'디자인3','디자인3',NULL,NULL,NULL,'2-6','2-6',NULL,'2-5','2-5'),(43,'정하나',NULL,'1-3','1-3','디자인2',NULL,NULL,NULL,'3-6','3-6','디자인2','디자인2',NULL,NULL,NULL,'3-6','3-6',NULL,NULL,NULL,NULL,NULL,'3-5','3-5','디자인3','디자인3',NULL,NULL,NULL,'3-5','3-5',NULL,NULL,NULL,'1-4','1-4'),(44,'이승복',NULL,NULL,NULL,'','디자인2','디자인2','디자인2',NULL,NULL,'웹솔루션3','웹솔루션3','웹솔루션2','웹솔루션2','웹솔루션2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'디자인3','디자인3',NULL,'웹솔루션3','웹솔루션3',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(45,'이주현',NULL,NULL,NULL,NULL,'디자인2','디자인2','디자인2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(46,'이아람',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2-4','2-3',NULL,NULL,NULL,NULL,NULL,'2-5','2-2',NULL,NULL,NULL,NULL,NULL,'2-1','2-6',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `tschedule` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-01 23:14:13
