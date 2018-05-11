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
INSERT INTO `APPEARS_IN` VALUES ('1000000000','100000001',1,999.99),('1000000002','100000002',4,899.99),('1000000003','100000000',1,1299.99),('1000000003','100000001',2,999.99),('1000000003','100000002',3,899.99),('1000000004','100000001',3,999.99),('1000000004','100000002',1,899.99),('1000000005','100000001',9,999.99),('1000000005','100000002',8,899.99),('1000000006','100000002',6,899.99),('1000000007','111122221',1,289.99),('1000000009','999999999',1,39.99),('1000000010','111122221',2,299.99),('1000000010','999999999',2,39.99),('1000000011','244444444',1,4999.99),('1000000012','244444444',1,4999.99),('1000000015','100000001',2,999.99),('1000000016','111122221',2,289.99);
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
INSERT INTO `CART` VALUES ('1000000000','100000001','old','2345234523452345',1,'2018-04-22'),('1000000002','100000001',NULL,NULL,0,'2018-04-22'),('1000000003','100000003','NYU','1688168816881688',2,'2018-04-28'),('1000000004','100000003','NYU','8888999988889999',1,'2018-04-28'),('1000000005','100000006','laocheng','123412341234',1,'2018-04-28'),('1000000006','100000006','home','432143214321',3,'2018-04-28'),('1000000007','100000006','yizhong','123412341234',1,'2018-05-02'),('1000000008','100000007',NULL,NULL,0,'2018-04-28'),('1000000009','100000003','Harrison330','8888999988889999',1,'2018-04-29'),('1000000010','100000003','Harrison330','777888777888',4,'2018-04-29'),('1000000011','100000006','Home','123412341234',2,'2018-05-02'),('1000000012','100000006','yizhong','123412341234',1,'2018-05-03'),('1000000013','100000003',NULL,NULL,0,'2018-05-03'),('1000000014','100000010',NULL,NULL,0,'2018-05-03'),('1000000015','100000006','Home','123123',1,'2018-05-03'),('1000000016','100000006',NULL,NULL,0,'2018-05-11');
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
INSERT INTO `COMPUTER` VALUES ('233333333','i7'),('244444444','i7');
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
INSERT INTO `CREDIT_CARD` VALUES ('123123','123','shibo','master','njit','2020-02-02',0),('123412341234','1234','Jim','master','China','2020-02-02',1),('1234123412341234','1234','Shibo','Visa','Nutley NJ','2020-01-01',1),('1688168816881688','168','Jeremy Hui','ame','Harrison NJ','2021-08-08',1),('2345234523452345','2345','Yao','master','Stony Brook, NY','2019-12-12',1),('432143214321','4321','Shibo','union','Tianjin','2222-01-01',0),('456456456456','456','Jeremy','ame','Harrison NJ','2019-01-01',0),('666777888999','6789','Dimitri','master','NJIT','2020-09-09',1),('777888777888','7878','Jeremy','visa','Harrison','2020-09-09',0),('8888999988889999','8899','Jeremy Hui','master','Harrison NJ','2020-09-09',1),('999888777666','9876','Dimitri','visa','NJIT','2019-01-09',1);
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
INSERT INTO `CUSTOMER` VALUES ('100000000','admin','manager','espoyao@gmail.com','Nutley','0000000000',9,'12345'),('100000001','Shibo','Yao','sy123@njit.edu','567 Central Ave, Harrison, NJ','1233211234',0,'1234'),('100000002','Shaobo','Liu','sl638@njit.edu','435 Forest St, Kearny, NJ','2012732585',1,NULL),('100000003','Jeremy','Hui','jh123@njit.edu','Harrison','1234567890',0,'123'),('100000004','test','T','test@gmail.com','NJIT','6666777888',0,'6666777888'),('100000005','YanYi','Fong','yan@gmail.com','NY','7778889999',0,'17778889999'),('100000006','Jim','Yao','jy@gmail.com','China','1333333333',2,'1234'),('100000007','Dimitri','Theodo','dt@njit.edu','NJIT','2222333444',0,'2222333444'),('100000008','Lilian','Kuo','lk@njit.edu','NJIT','2222999900',0,'222'),('100000009','Yan','Shu','sy@ucsd.edu','Walmart','2222333333',0,'2222'),('100000010','test21','t','sy372','njit','1111111111',0,'123'),('100000011','ShaoBo','Liu','sliu36@stevens.edu','412 Central Ave, Newark','2132421111',0,'111');
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
INSERT INTO `LAPTOP` VALUES ('100000000','regular',1.90),('100000001','premium',0.99),('100000002','plus',2.10);
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
INSERT INTO `OFFER_PRODUCT` VALUES ('111122221',289.99),('233333333',3099.99);
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
INSERT INTO `PRINTER` VALUES ('111122221','blackwhite',3000000),('111122222','color',8000000),('111222333','color',3000000);
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
INSERT INTO `PRODUCT` VALUES ('100000000','Laptop','MacbookPro',1299.99,'Newest version Apple MacbookPro.',5),('100000001','Laptop','Macbook',999.99,'The newest version Apple Macbook.',20),('100000002','Laptop','Dell XPS14',899.99,'New Dell XPS14 ultrabook.',10),('111122221','Printer','Canon blackwhite',333.33,'Canon black and white light printer.',20),('111122222','Printer','Canon color Econ',444.44,'Canon black and white light printer.',30),('111222333','Printer','Canon color',666.66,'Canon colorful printer.',20),('233333333','Computer','Mac',3299.99,'Mac desktop. ',4),('244444444','Desktop','Dell workstation',4999.99,'Dell strong workstation for intencive computing.',3),('666666666','Other','Silver Membership',66.66,'Silver membership. Can enjoy some offers.',99999),('888888888','Other','Gold Membership',88.88,'Gold membership. Can enjoy all offers.',99999),('999999999','Other','Verticle Mouse',39.99,'Verticle mouse that helps relax your arm.',30);
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
INSERT INTO `SHIP_ADDRESS` VALUES ('100000001','Shibo','US','NJ','Nutley','07110','Main ST','1','myadd'),('100000001','Shibo','US','NY','Stony Brook','11790','Stony Brook Rd.','1','old'),('100000003','Jeremy','US','NJ','Harrison','07103','Harrison Ave','330','Harrison330'),('100000003','Brother','US','NY','NYC','10000','5th Ave','1','NYU'),('100000006','Yun','China','Tianjin','Tianjin','300000','Huaming','168','Home'),('100000006','Espo','China','Tianjin','Tianjin','300000','Liuzhou Road','23','laocheng'),('100000006','Jim','China','Tianjin','Tianjin','300000','Xian Road','157','yizhong'),('100000007','Dimitri','US','NJ','Newark','07102','Broadway','123','broadway'),('100000007','Dimitri','US','NJ','Newark','07102','MLK bld','3','newark');
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
INSERT INTO `SILVER_AND_ABOVE` VALUES ('100000001',2000),('100000006',3000);
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
INSERT INTO `STORED_CARD` VALUES ('1234123412341234','100000001'),('2345234523452345','100000001'),('1688168816881688','100000003'),('8888999988889999','100000003'),('123412341234','100000006'),('666777888999','100000007'),('999888777666','100000007');
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

-- Dump completed on 2018-05-11 11:11:14
