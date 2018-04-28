-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: store
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

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
-- Table structure for table `APPEARS_IN`
--

DROP TABLE IF EXISTS `APPEARS_IN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `APPEARS_IN` (
  `CARTID` char(10) NOT NULL,
  `PID` char(9) NOT NULL,
  `QUANTITY` int(11) NOT NULL,
  `PRICESOLD` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`CARTID`,`PID`),
  KEY `PID` (`PID`),
  CONSTRAINT `APPEARS_IN_ibfk_2` FOREIGN KEY (`PID`) REFERENCES `PRODUCT` (`PID`),
  CONSTRAINT `APPEARS_IN_ibfk_3` FOREIGN KEY (`CARTID`) REFERENCES `CART` (`CARTID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `APPEARS_IN`
--

LOCK TABLES `APPEARS_IN` WRITE;
/*!40000 ALTER TABLE `APPEARS_IN` DISABLE KEYS */;
INSERT INTO `APPEARS_IN` VALUES ('1000000000','100000001',1,999.99),('1000000002','100000002',4,899.99);
/*!40000 ALTER TABLE `APPEARS_IN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CART`
--

DROP TABLE IF EXISTS `CART`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CART` (
  `CARTID` char(10) NOT NULL,
  `CID` char(9) NOT NULL,
  `SANAME` varchar(15) DEFAULT NULL,
  `CCNUMBER` varchar(16) DEFAULT NULL,
  `TSTATUS` int(11) NOT NULL,
  `TDATE` date DEFAULT NULL,
  PRIMARY KEY (`CARTID`),
  KEY `CCNUMBER` (`CCNUMBER`),
  CONSTRAINT `CART_ibfk_1` FOREIGN KEY (`CCNUMBER`) REFERENCES `CREDIT_CARD` (`CARDNUMBER`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CART`
--

LOCK TABLES `CART` WRITE;
/*!40000 ALTER TABLE `CART` DISABLE KEYS */;
INSERT INTO `CART` VALUES ('1000000000','100000001','old','2345234523452345',1,'2018-04-22'),('1000000002','100000001',NULL,NULL,0,'2018-04-22');
/*!40000 ALTER TABLE `CART` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COMPUTER`
--

DROP TABLE IF EXISTS `COMPUTER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `COMPUTER` (
  `PID` char(9) NOT NULL,
  `CPUTYPE` varchar(20) NOT NULL,
  PRIMARY KEY (`PID`),
  CONSTRAINT `COMPUTER_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `PRODUCT` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COMPUTER`
--

LOCK TABLES `COMPUTER` WRITE;
/*!40000 ALTER TABLE `COMPUTER` DISABLE KEYS */;
/*!40000 ALTER TABLE `COMPUTER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CREDIT_CARD`
--

DROP TABLE IF EXISTS `CREDIT_CARD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CREDIT_CARD` (
  `CARDNUMBER` varchar(16) NOT NULL,
  `SECNUMBER` varchar(5) DEFAULT NULL,
  `OWNERNAME` varchar(15) NOT NULL,
  `CARTYPE` varchar(6) DEFAULT NULL,
  `BILLINGADDRESS` varchar(30) NOT NULL,
  `EXPDATE` date NOT NULL,
  `STORED_CARD` int(1) DEFAULT NULL,
  PRIMARY KEY (`CARDNUMBER`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CREDIT_CARD`
--

LOCK TABLES `CREDIT_CARD` WRITE;
/*!40000 ALTER TABLE `CREDIT_CARD` DISABLE KEYS */;
INSERT INTO `CREDIT_CARD` VALUES ('1234123412341234','1234','Shibo','Visa','Nutley NJ','2020-01-01',1),('2345234523452345','2345','Yao','master','Stony Brook, NY','2019-12-12',1);
/*!40000 ALTER TABLE `CREDIT_CARD` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CUSTOMER`
--

DROP TABLE IF EXISTS `CUSTOMER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CUSTOMER` (
  `CID` char(9) NOT NULL,
  `FNAME` varchar(50) NOT NULL,
  `LNAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `ADDRESS` varchar(50) NOT NULL,
  `PHONE` char(10) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `PASSWORD` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER`
--

LOCK TABLES `CUSTOMER` WRITE;
/*!40000 ALTER TABLE `CUSTOMER` DISABLE KEYS */;
INSERT INTO `CUSTOMER` VALUES ('100000000','admin','manager','espoyao@gmail.com','Nutley','0000000000',9,'12345'),('100000001','Shibo','Yao','sy123@njit.edu','567 Central Ave, Harrison, NJ','1233211234',0,'wobuzhidao'),('100000002','Shaobo','Liu','sl638@njit.edu','435 Forest St, Kearny, NJ','2012732585',1,NULL),('100000003','Jeremy','Hui','jh564@njit.edu','Harrison NJ','9999999999',0,'1234');
/*!40000 ALTER TABLE `CUSTOMER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LAPTOP`
--

DROP TABLE IF EXISTS `LAPTOP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LAPTOP` (
  `PID` char(9) NOT NULL,
  `BTYPE` varchar(8) NOT NULL,
  `WEIGHT` decimal(4,2) DEFAULT NULL,
  PRIMARY KEY (`PID`),
  CONSTRAINT `LAPTOP_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `PRODUCT` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LAPTOP`
--

LOCK TABLES `LAPTOP` WRITE;
/*!40000 ALTER TABLE `LAPTOP` DISABLE KEYS */;
INSERT INTO `LAPTOP` VALUES ('100000001','premium',0.99),('100000002','plus',2.10);
/*!40000 ALTER TABLE `LAPTOP` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OFFER_PRODUCT`
--

DROP TABLE IF EXISTS `OFFER_PRODUCT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OFFER_PRODUCT` (
  `PID` char(9) NOT NULL,
  `OFFERPRICE` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`PID`),
  CONSTRAINT `OFFER_PRODUCT_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `PRODUCT` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OFFER_PRODUCT`
--

LOCK TABLES `OFFER_PRODUCT` WRITE;
/*!40000 ALTER TABLE `OFFER_PRODUCT` DISABLE KEYS */;
/*!40000 ALTER TABLE `OFFER_PRODUCT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRINTER`
--

DROP TABLE IF EXISTS `PRINTER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PRINTER` (
  `PID` char(9) NOT NULL,
  `PRINTERTYPE` varchar(10) NOT NULL,
  `RESOLUTION` decimal(8,0) NOT NULL,
  PRIMARY KEY (`PID`),
  CONSTRAINT `PRINTER_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `PRODUCT` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRINTER`
--

LOCK TABLES `PRINTER` WRITE;
/*!40000 ALTER TABLE `PRINTER` DISABLE KEYS */;
/*!40000 ALTER TABLE `PRINTER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRODUCT`
--

DROP TABLE IF EXISTS `PRODUCT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PRODUCT` (
  `PID` char(9) NOT NULL,
  `PTYPE` varchar(20) NOT NULL,
  `PNAME` varchar(50) NOT NULL,
  `PPRICE` decimal(8,2) DEFAULT NULL,
  `DESCRIPTION` varchar(50) NOT NULL,
  `PQUANTITY` int(11) NOT NULL,
  PRIMARY KEY (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRODUCT`
--

LOCK TABLES `PRODUCT` WRITE;
/*!40000 ALTER TABLE `PRODUCT` DISABLE KEYS */;
INSERT INTO `PRODUCT` VALUES ('100000000','Laptop','MacbookPro',1299.99,'Newest version Apple MacbookPro.',5),('100000001','Laptop','Macbook',999.99,'The newest version Apple Macbook.',20),('100000002','Laptop','Dell XPS14',899.99,'New Dell XPS14 ultrabook.',10);
/*!40000 ALTER TABLE `PRODUCT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SHIP_ADDRESS`
--

DROP TABLE IF EXISTS `SHIP_ADDRESS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SHIP_ADDRESS` (
  `CID` char(9) NOT NULL,
  `RECEPIENTNAME` varchar(15) NOT NULL,
  `COUNTRY` varchar(10) NOT NULL,
  `STATE` varchar(20) NOT NULL,
  `CITY` varchar(20) NOT NULL,
  `ZIP` varchar(10) NOT NULL,
  `STREET` varchar(20) NOT NULL,
  `SNUMBER` varchar(9) NOT NULL,
  `SANAME` varchar(15) NOT NULL,
  PRIMARY KEY (`CID`,`SANAME`),
  CONSTRAINT `SHIP_ADDRESS_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `CUSTOMER` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SHIP_ADDRESS`
--

LOCK TABLES `SHIP_ADDRESS` WRITE;
/*!40000 ALTER TABLE `SHIP_ADDRESS` DISABLE KEYS */;
INSERT INTO `SHIP_ADDRESS` VALUES ('100000001','Shibo','US','NJ','Nutley','07110','Main ST','1','myadd'),('100000001','Shibo','US','NY','Stony Brook','11790','Stony Brook Rd.','1','old');
/*!40000 ALTER TABLE `SHIP_ADDRESS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SILVER_AND_ABOVE`
--

DROP TABLE IF EXISTS `SILVER_AND_ABOVE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SILVER_AND_ABOVE` (
  `CID` char(9) NOT NULL,
  `CREDITLINE` int(11) NOT NULL,
  PRIMARY KEY (`CID`),
  CONSTRAINT `SILVER_AND_ABOVE_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `CUSTOMER` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SILVER_AND_ABOVE`
--

LOCK TABLES `SILVER_AND_ABOVE` WRITE;
/*!40000 ALTER TABLE `SILVER_AND_ABOVE` DISABLE KEYS */;
INSERT INTO `SILVER_AND_ABOVE` VALUES ('100000001',2000);
/*!40000 ALTER TABLE `SILVER_AND_ABOVE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STORED_CARD`
--

DROP TABLE IF EXISTS `STORED_CARD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STORED_CARD` (
  `CCNUMBER` char(16) NOT NULL,
  `CID` char(9) NOT NULL,
  PRIMARY KEY (`CCNUMBER`),
  KEY `CID` (`CID`),
  CONSTRAINT `STORED_CARD_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `CUSTOMER` (`CID`),
  CONSTRAINT `STORED_CARD_ibfk_2` FOREIGN KEY (`CCNUMBER`) REFERENCES `CREDIT_CARD` (`CARDNUMBER`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STORED_CARD`
--

LOCK TABLES `STORED_CARD` WRITE;
/*!40000 ALTER TABLE `STORED_CARD` DISABLE KEYS */;
INSERT INTO `STORED_CARD` VALUES ('1234123412341234','100000001'),('2345234523452345','100000001');
/*!40000 ALTER TABLE `STORED_CARD` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-24 22:00:58
