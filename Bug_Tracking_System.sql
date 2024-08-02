CREATE DATABASE  IF NOT EXISTS `bug_tracking_system` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `bug_tracking_system`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: bug_tracking_system
-- ------------------------------------------------------
-- Server version	5.5.55

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
-- Table structure for table `bug`
--

DROP TABLE IF EXISTS `bug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bug` (
  `bugId` int(11) NOT NULL AUTO_INCREMENT,
  `bugPostingDate` datetime DEFAULT NULL,
  `custLoginId` varchar(10) NOT NULL,
  `bugStatus` varchar(20) DEFAULT 'New Bug',
  `productName` varchar(45) NOT NULL,
  `bugDesc` text NOT NULL,
  `expertAssignedDate` datetime DEFAULT NULL,
  `expertLoginId` varchar(10) DEFAULT NULL,
  `bugSolvedDate` datetime DEFAULT NULL,
  `solution` text,
  PRIMARY KEY (`bugId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bug`
--

LOCK TABLES `bug` WRITE;
/*!40000 ALTER TABLE `bug` DISABLE KEYS */;
INSERT INTO `bug` VALUES (1,'2023-07-14 14:07:01','CU2001','New Bug','Laptop','Screen is flickring',NULL,NULL,NULL,NULL),(2,'2023-07-14 14:07:01','CU2001','Assigned','Mobile','Keyboard not working.','2023-07-14 14:05:58','EX3001',NULL,NULL),(3,'2023-07-14 14:07:01','CU2003','New Bug','Laptop','Wifi connection issues',NULL,NULL,NULL,NULL),(4,NULL,'CU2005','Assigned','Laptop','Poor Battery','2023-07-14 14:04:05','EX1234','2023-07-14 05:05:52','battery change'),(5,NULL,'CU2003','solved','T.V.','GLitch',NULL,NULL,'2023-07-14 13:53:09','restart the T.V.');
/*!40000 ALTER TABLE `bug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `custLoginId` varchar(10) NOT NULL,
  `custPassword` varchar(20) DEFAULT NULL,
  `custName` varchar(45) DEFAULT NULL,
  `custAge` int(11) DEFAULT NULL,
  `custPhone` varchar(10) DEFAULT NULL,
  `custEmail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`custLoginId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('CU2001','password','Mohit',12,'1234123577','mohit@demo.com'),('CU2002','dark','Chintu',18,'0921874361','chintu@demo.com'),('CU2003','pastword','Pooja',23,'9847578776','pooja@demo.com'),('CU2004','postword','Rohit',25,'8959578776','rohit@demo.com'),('CU2005','pistacio','Nikhil',20,'7024485803','nikhil@demo.com'),('CU2006','panda','Ishita Bhatt',18,'9876543210','ishita@demo.com'),('CU2007','QWERTYUIOP','Vaishnavi Singh Parihar',18,'9401345674','vaishnavi@demo.com'),('CU2008','cust','Naina',23,'9743478736','naina@demo.com');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `empLoginId` varchar(10) NOT NULL,
  `empPassword` varchar(20) DEFAULT NULL,
  `empType` varchar(20) DEFAULT NULL,
  `empName` varchar(45) DEFAULT NULL,
  `empPhone` varchar(10) DEFAULT NULL,
  `empEmail` varchar(45) DEFAULT NULL,
  `empStatus` varchar(20) DEFAULT 'ACTIVE',
  PRIMARY KEY (`empLoginId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('AD1001','password','ADMIN','Priti Singh','9998887776','help@admin.com','ACTIVE'),('EX1234','pussword','EXPERT','Poornima','9273446432','poornima@demo.com','ACTIVE'),('EX3001','pissword','EXPERT','DemoUser','4444444','expert@admin.com','ACTIVE'),('EX3002','pastaword','EXPERT','Divyanka Lakhwani','1357908642','Div@demo.com','INACTIVE'),('ex3003','password','EXPERT','Shaily','3478965215','shaily@demo.com','ACTIVE');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-16 23:28:58
