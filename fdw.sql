-- MySQL dump 10.13  Distrib 5.5.32, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: fdw
-- ------------------------------------------------------
-- Server version	5.5.32-0ubuntu0.12.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add website',7,'add_website'),(20,'Can change website',7,'change_website'),(21,'Can delete website',7,'delete_website'),(25,'Can add theme',9,'add_theme'),(26,'Can change theme',9,'change_theme'),(27,'Can delete theme',9,'delete_theme'),(28,'Can add image',10,'add_image'),(29,'Can change image',10,'change_image'),(30,'Can delete image',10,'delete_image');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$R93QavDF2G4p$OynrmDH4uRIwK880H9NcbaX0vzH3DLtN41NvhkNqlEw=','2015-11-08 03:41:00',1,'pisskidney','','','a@a.com',1,1,'2015-10-13 05:34:47'),(2,'pbkdf2_sha256$20000$JTw7LaIDefMu$2EcbHpTRGBmqoUa+wgeOz9jPrPRkoGIZVlCqdxRla/k=',NULL,0,'petisnnake','','','aaa@aaa.com',0,1,'2015-10-20 18:02:29'),(4,'pbkdf2_sha256$20000$4PaCKCYj55K6$QV/E46oGHYAPhJiupxNvgwt2NmnB+QiZiopGUbSOHuQ=',NULL,0,'petisnnake2','','','aaa2@aaa.com',0,1,'2015-10-20 18:16:12'),(5,'pbkdf2_sha256$20000$IZK1h9Jf5vlO$4Eu3JRSgBZ84SdrEfL1qQPp/vNMH6EPW4mT1+jhRzQY=','2015-10-31 01:29:12',0,'ffs','','','ffs@ffs.com',0,1,'2015-10-20 18:18:02'),(6,'pbkdf2_sha256$20000$YsWhhzXqiGUI$UY4CawSpfOHxTgajmh2zzgK7V8giBSIBrImxTYJa/Wk=','2015-10-20 18:48:54',0,'abc','','','abc@asdas.com',0,1,'2015-10-20 18:48:54'),(7,'pbkdf2_sha256$20000$vMFJxosv9poU$t3cAUO40XvECCiSn8eU2gNsrQl0gvV25Q6PJxNko1RY=','2015-10-20 18:53:50',0,'muie','','','muie@muie.com',0,1,'2015-10-20 18:53:50'),(8,'pbkdf2_sha256$20000$7RBydxKW0yzJ$q7rYx/oiFWphAwf+by/nAHdHsQGacvbwmvAEZdtD3yU=','2015-10-20 18:55:32',0,'dasdsad','','','asdad@cascsc.com',0,1,'2015-10-20 18:55:32');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `builder_image`
--

DROP TABLE IF EXISTS `builder_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `builder_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(64) DEFAULT NULL,
  `full` varchar(1024),
  `preview` varchar(1024),
  `thumbnail` varchar(1024),
  `type` varchar(64),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `builder_image`
--

LOCK TABLES `builder_image` WRITE;
/*!40000 ALTER TABLE `builder_image` DISABLE KEYS */;
INSERT INTO `builder_image` VALUES (35,'nature','imgs/bg/forest4.jpg','imgs/bg/forest4_preview.jpg','imgs/bg/forest4_thumb.png','bg'),(36,'nature','imgs/bg/forest1.jpg','imgs/bg/forest1_preview.jpg','imgs/bg/forest1_thumb.png','bg'),(37,'night','imgs/bg/night2.jpg','imgs/bg/night2_preview.jpg','imgs/bg/night2_thumb.png','bg'),(39,'night','imgs/bg/night1.jpg','imgs/bg/night1_preview.jpg','imgs/bg/night1_thumb.png','bg'),(40,'night','imgs/bg/night3.jpg','imgs/bg/night3_preview.jpg','imgs/bg/night3_thumb.png','bg'),(41,'social','imgs/bg/bar1.jpg','imgs/bg/bar1_preview.jpg','imgs/bg/bar1_thumb.png','bg'),(42,'nature','imgs/bg/mountain.jpg','imgs/bg/mountain_preview.jpg','imgs/bg/mountain_thumb.png','bg');
/*!40000 ALTER TABLE `builder_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `builder_theme`
--

DROP TABLE IF EXISTS `builder_theme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `builder_theme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `color1` varchar(7) NOT NULL,
  `color2` varchar(7) NOT NULL,
  `color4` varchar(7) NOT NULL,
  `color5` varchar(7) NOT NULL,
  `color3` varchar(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `builder_theme`
--

LOCK TABLES `builder_theme` WRITE;
/*!40000 ALTER TABLE `builder_theme` DISABLE KEYS */;
INSERT INTO `builder_theme` VALUES (1,'Midnight','#000000','#1EAD29','#000000','#324E59','#F8F8F8'),(2,'Clean','#F8F8F8','#F8F8F8','#AC4A00','#000000','#000000'),(3,'Boulgari','#FFC2CE','#FD6E8A','#A2122F','#693726','#693726'),(4,'Sky','#17649A','#40B3DF','#EEEEEE','#FFFFFF','#A8CB17'),(5,'Etsy','#DC4E00','#929487','#F4F5ED','#89CEDE','#C7C9BE'),(6,'Yelp','#C00F00','#B4B0E3','#181411','#FFFFFF','#FFFFE5');
/*!40000 ALTER TABLE `builder_theme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `builder_website`
--

DROP TABLE IF EXISTS `builder_website`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `builder_website` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `contact_email` varchar(255) NOT NULL,
  `contact_address` varchar(1024) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `home_description` varchar(2048) NOT NULL,
  `home_motto` varchar(1024) NOT NULL,
  `domain_name` varchar(255),
  `domain_type` smallint(6),
  `build_stage` smallint(6),
  `theme_id` int(11),
  PRIMARY KEY (`id`),
  KEY `builder_website_owner_id_6bbf0bda_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `builder_website_owner_id_6bbf0bda_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `builder_website`
--

LOCK TABLES `builder_website` WRITE;
/*!40000 ALTER TABLE `builder_website` DISABLE KEYS */;
/*!40000 ALTER TABLE `builder_website` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-11-06 08:54:25','1','Theme object',1,'',9,1),(2,'2015-11-06 20:03:37','1','Theme object',2,'Changed color5.',9,1),(3,'2015-11-06 20:33:58','2','Theme object',1,'',9,1),(4,'2015-11-06 20:35:12','3','Theme object',1,'',9,1),(5,'2015-11-06 20:36:34','4','Theme object',1,'',9,1),(6,'2015-11-06 20:37:29','5','Theme object',1,'',9,1),(7,'2015-11-06 20:37:59','6','Theme object',1,'',9,1),(8,'2015-11-07 02:35:43','1','Image object',1,'',10,1),(9,'2015-11-07 02:36:03','2','Image object',1,'',10,1),(10,'2015-11-07 02:36:23','3','Image object',1,'',10,1),(11,'2015-11-07 02:36:41','4','Image object',1,'',10,1),(12,'2015-11-07 02:49:21','5','Image object',1,'',10,1),(13,'2015-11-07 02:49:33','6','Image object',1,'',10,1),(14,'2015-11-07 04:05:29','7','Image object',1,'',10,1),(15,'2015-11-07 04:05:41','8','Image object',1,'',10,1),(16,'2015-11-07 04:05:52','9','Image object',1,'',10,1),(17,'2015-11-07 04:06:04','10','Image object',1,'',10,1),(18,'2015-11-07 04:06:19','10','Image object',2,'Changed path.',10,1),(19,'2015-11-07 04:06:44','11','Image object',1,'',10,1),(20,'2015-11-07 04:06:58','12','Image object',1,'',10,1),(21,'2015-11-07 04:08:02','13','Image object',1,'',10,1),(22,'2015-11-07 04:08:13','14','Image object',1,'',10,1),(23,'2015-11-07 04:08:28','15','Image object',1,'',10,1),(24,'2015-11-07 04:08:38','16','Image object',1,'',10,1),(25,'2015-11-07 04:16:48','1','Image object',2,'Changed path.',10,1),(26,'2015-11-07 04:17:00','2','Image object',2,'Changed path.',10,1),(27,'2015-11-07 04:30:05','17','Image object',1,'',10,1),(28,'2015-11-07 04:30:16','18','Image object',1,'',10,1),(29,'2015-11-07 22:29:11','19','Image object',1,'',10,1),(30,'2015-11-07 23:20:47','19','Image object',2,'Changed type.',10,1),(31,'2015-11-08 00:11:31','19','Image object',3,'',10,1),(32,'2015-11-08 00:11:31','18','Image object',3,'',10,1),(33,'2015-11-08 00:11:31','17','Image object',3,'',10,1),(34,'2015-11-08 00:11:31','16','Image object',3,'',10,1),(35,'2015-11-08 00:11:31','15','Image object',3,'',10,1),(36,'2015-11-08 00:11:31','14','Image object',3,'',10,1),(37,'2015-11-08 00:11:31','13','Image object',3,'',10,1),(38,'2015-11-08 00:11:31','12','Image object',3,'',10,1),(39,'2015-11-08 00:11:31','11','Image object',3,'',10,1),(40,'2015-11-08 00:11:31','10','Image object',3,'',10,1),(41,'2015-11-08 00:11:31','9','Image object',3,'',10,1),(42,'2015-11-08 00:11:31','8','Image object',3,'',10,1),(43,'2015-11-08 00:11:31','7','Image object',3,'',10,1),(44,'2015-11-08 00:11:31','6','Image object',3,'',10,1),(45,'2015-11-08 00:11:31','5','Image object',3,'',10,1),(46,'2015-11-08 00:11:31','4','Image object',3,'',10,1),(47,'2015-11-08 00:11:31','3','Image object',3,'',10,1),(48,'2015-11-08 00:11:31','2','Image object',3,'',10,1),(49,'2015-11-08 00:11:31','1','Image object',3,'',10,1),(50,'2015-11-08 00:18:33','28','Image object',3,'',10,1),(51,'2015-11-08 00:18:33','27','Image object',3,'',10,1),(52,'2015-11-08 00:19:13','31','Image object',2,'Changed topic.',10,1),(53,'2015-11-08 00:19:20','21','Image object',2,'Changed topic.',10,1),(54,'2015-11-08 03:41:12','34','Image object',3,'',10,1),(55,'2015-11-08 03:41:12','33','Image object',3,'',10,1),(56,'2015-11-08 03:41:12','32','Image object',3,'',10,1),(57,'2015-11-08 03:41:12','31','Image object',3,'',10,1),(58,'2015-11-08 03:41:12','30','Image object',3,'',10,1),(59,'2015-11-08 03:41:12','29','Image object',3,'',10,1),(60,'2015-11-08 03:41:12','26','Image object',3,'',10,1),(61,'2015-11-08 03:41:12','25','Image object',3,'',10,1),(62,'2015-11-08 03:41:12','24','Image object',3,'',10,1),(63,'2015-11-08 03:41:12','23','Image object',3,'',10,1),(64,'2015-11-08 03:41:12','22','Image object',3,'',10,1),(65,'2015-11-08 03:41:12','21','Image object',3,'',10,1),(66,'2015-11-08 03:41:12','20','Image object',3,'',10,1),(67,'2015-11-08 04:09:29','38','Image object',3,'',10,1),(68,'2015-11-08 04:11:19','41','Image object',2,'Changed topic.',10,1),(69,'2015-11-08 04:11:25','40','Image object',2,'Changed topic.',10,1),(70,'2015-11-08 04:11:33','39','Image object',2,'Changed topic.',10,1),(71,'2015-11-08 04:11:37','37','Image object',2,'Changed topic.',10,1),(72,'2015-11-08 04:14:38','1','Theme object',2,'Changed color1 and color2.',9,1),(73,'2015-11-08 04:19:21','1','Theme object',2,'Changed color3 and color4.',9,1),(74,'2015-11-08 05:16:37','3','Theme object',2,'Changed name.',9,1),(75,'2015-11-08 05:17:43','3','Theme object',2,'Changed color2.',9,1),(76,'2015-11-08 05:18:05','3','Theme object',2,'Changed color3.',9,1),(77,'2015-11-08 05:21:14','2','Theme object',2,'Changed name, color1, color2 and color3.',9,1),(78,'2015-11-08 05:21:54','2','Theme object',2,'Changed name.',9,1),(79,'2015-11-08 19:58:26','1','Theme object',2,'Changed color5.',9,1),(80,'2015-11-08 19:59:15','1','Theme object',2,'Changed color3.',9,1),(81,'2015-11-08 20:49:19','1','Theme object',2,'Changed color4.',9,1),(82,'2015-11-08 22:57:28','32','Website object',3,'',7,1),(83,'2015-11-08 22:57:28','31','Website object',3,'',7,1),(84,'2015-11-08 22:57:28','30','Website object',3,'',7,1),(85,'2015-11-08 22:57:28','29','Website object',3,'',7,1),(86,'2015-11-08 22:57:28','28','Website object',3,'',7,1),(87,'2015-11-08 22:57:28','27','Website object',3,'',7,1),(88,'2015-11-08 22:57:28','26','Website object',3,'',7,1),(89,'2015-11-08 22:57:28','25','Website object',3,'',7,1),(90,'2015-11-08 22:57:28','24','Website object',3,'',7,1),(91,'2015-11-08 22:57:28','23','Website object',3,'',7,1),(92,'2015-11-08 22:57:28','22','Website object',3,'',7,1),(93,'2015-11-08 22:57:28','21','Website object',3,'',7,1),(94,'2015-11-08 22:57:28','20','Website object',3,'',7,1),(95,'2015-11-08 22:57:28','19','Website object',3,'',7,1),(96,'2015-11-08 22:57:28','18','Website object',3,'',7,1),(97,'2015-11-08 22:57:28','17','Website object',3,'',7,1),(98,'2015-11-08 22:57:28','16','Website object',3,'',7,1),(99,'2015-11-08 22:57:28','15','Website object',3,'',7,1),(100,'2015-11-08 22:57:28','14','Website object',3,'',7,1),(101,'2015-11-08 22:57:28','13','Website object',3,'',7,1),(102,'2015-11-08 22:57:28','12','Website object',3,'',7,1),(103,'2015-11-08 22:57:28','11','Website object',3,'',7,1),(104,'2015-11-08 22:57:28','10','Website object',3,'',7,1),(105,'2015-11-08 22:57:28','9','Website object',3,'',7,1),(106,'2015-11-08 22:57:28','8','Website object',3,'',7,1),(107,'2015-11-08 22:57:28','7','Website object',3,'',7,1),(108,'2015-11-08 22:57:28','6','Website object',3,'',7,1),(109,'2015-11-08 22:57:28','5','Website object',3,'',7,1),(110,'2015-11-08 22:57:28','4','Website object',3,'',7,1),(111,'2015-11-08 22:57:28','3','Website object',3,'',7,1),(112,'2015-11-08 22:57:28','2','Website object',3,'',7,1),(113,'2015-11-08 22:57:28','1','Website object',3,'',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(10,'builder','image'),(9,'builder','theme'),(7,'builder','website'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-10-12 21:18:12'),(2,'auth','0001_initial','2015-10-12 21:18:12'),(3,'admin','0001_initial','2015-10-12 21:18:12'),(4,'contenttypes','0002_remove_content_type_name','2015-10-12 21:18:12'),(5,'auth','0002_alter_permission_name_max_length','2015-10-12 21:18:12'),(6,'auth','0003_alter_user_email_max_length','2015-10-12 21:18:12'),(7,'auth','0004_alter_user_username_opts','2015-10-12 21:18:12'),(8,'auth','0005_alter_user_last_login_null','2015-10-12 21:18:12'),(9,'auth','0006_require_contenttypes_0002','2015-10-12 21:18:12'),(10,'sessions','0001_initial','2015-10-12 21:18:12'),(11,'builder','0001_initial','2015-10-13 05:21:20'),(12,'builder','0002_auto_20151105_2301','2015-11-05 23:01:51'),(13,'builder','0003_auto_20151105_2339','2015-11-05 23:39:12'),(14,'builder','0004_auto_20151106_0010','2015-11-06 00:10:24'),(15,'builder','0005_website_build_stage','2015-11-06 01:13:07'),(16,'builder','0006_theme','2015-11-06 08:50:45'),(17,'builder','0007_auto_20151106_1914','2015-11-06 19:14:43'),(18,'builder','0008_auto_20151107_0042','2015-11-07 00:42:48'),(19,'builder','0009_image_type','2015-11-07 02:25:23'),(20,'builder','0010_auto_20151107_2311','2015-11-07 23:11:56'),(21,'builder','0011_auto_20151107_2320','2015-11-07 23:20:27');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('b26c8fu887bmb7blf0t3l4nhmoogaf8o','NWJhMjZlYTMxODAzNzQyMmRlM2RjNWJhNTExMTViZTg4YmJhNGQ0MTp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsIl9hdXRoX3VzZXJfaGFzaCI6ImNlZmVkNzU2N2I2OTNhZGQzZWRiZjlmNWFiNTBiMmYyNjdlMDQzOTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-11-01 01:29:12'),('c55281y7dgpd5oy5kx3y9vdlm9pvxvbx','MWE0NTIxMjJiMmM3ODRiMzc0MmRlZTZiNzk2MzlkMmJlYjU0NmRhMTp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsIl9hdXRoX3VzZXJfaGFzaCI6IjAzYjA5MGU5NDdiNDFiYTg1NWZkZmY0NDY3ZDRlOWE5YzM1ODNmNTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-11-07 08:52:21'),('eh9in9r3dkwxh58j5rxcegpaqocwer2j','NWJhMjZlYTMxODAzNzQyMmRlM2RjNWJhNTExMTViZTg4YmJhNGQ0MTp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsIl9hdXRoX3VzZXJfaGFzaCI6ImNlZmVkNzU2N2I2OTNhZGQzZWRiZjlmNWFiNTBiMmYyNjdlMDQzOTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-10-25 00:45:49'),('fgqkyrca7k7vabnjwsr5k7mriserstxv','MWE0NTIxMjJiMmM3ODRiMzc0MmRlZTZiNzk2MzlkMmJlYjU0NmRhMTp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsIl9hdXRoX3VzZXJfaGFzaCI6IjAzYjA5MGU5NDdiNDFiYTg1NWZkZmY0NDY3ZDRlOWE5YzM1ODNmNTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-11-09 03:41:00'),('s3iztcugdaqpdxpmhfbzy56is03e7o69','YjAyMmY2MTBmNGI4YmM5NjdjOTU5YWYwZTczNWNiYjZjOGNlMDdlZDp7Il9zZXNzaW9uX2V4cGlyeSI6NjA0ODAwLCJfYXV0aF91c2VyX2hhc2giOiI5MDFlNmE2MzY3MzEzZjNhZWM4MDJmMjU1YzAxZmI3YWJkODVhMWUyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiOCJ9','2015-10-27 18:55:32');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-08 23:14:02
