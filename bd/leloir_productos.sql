-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: leloir
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_publicacion` date NOT NULL,
  `nombre` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `imagen` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `memo` varchar(200) NOT NULL,
  `galeria` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=267 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (263,'2023-11-25','ActoProtocolar','FLQAIR93D6H0J_VZPO8U.jpg','Los alumnos, familias y personal del colegio participamos del actoProtocolar por los 30 años de nuestro querido instituto Leloir. ¡Felices 30 años querido colegio!','[\"BU4XRHS8IP932G6AQD0F.jpg\", \"0QW5P7BS_TADK698ZUGL.jpg\", \"VOULBF64ZRHYWIQN9A3D.jpg\", \"1OM6E5X0J32Z9UYKG4RI.jpg\", \"M_PUD43T1NZSQHBFVIA2.jpg\", \"ONGJ3PM5HDR2TIU987L4.jpg\", \"6ZFXRC8SJLPAW9_G34QM.jpg\", \"UHV4OMN8D71F3TIWRPAL.jpg\", \"UM2JEO4X730_TGARV5NB.jpg\", \"HIMTJOP7G05_3F8EBYKD.jpg\", \"TDL6ARWYOE_UXM79PN0C.jpg\", \"34T9XDKHI2ABQV5JM1E_.jpg\", \"6IGSHY9NWOC1UXEZF7RL.jpg\", \"Y_L675U03DMQ82V1WXHK.jpg\", \"RUJVKQZH5C_YLMAOEDI1.jpg\", \"B94H0YTPE3OSL2F8XK5Z.jpg\"]','secundaria'),(264,'2023-11-25','Microemprendimientos','R19HCB83LTYGS76VUQKA.jpg','Como todos los años nuestros alumnos del nivel Secundario llevan a cabo la feria de microemprendimientos. Felicitaciones!!!','[\"XRSD5C7KZV9Y4F1HIQAT.jpg\", \"J1QMN45DYH0VB8XE267T.jpg\", \"64CMUGOFQT_7WRLI02BP.jpg\", \"ZKVENRS16AL0HT7B_345.jpg\", \"54D0JWB17HSY68ZKMCAG.jpg\", \"BLFVAJ6ED8HQC_OP5M43.jpg\", \"JPZT3209YLQSNIM4CU5A.jpg\", \"KA16O9PZ4FD3LIVNWMS2.jpg\", \"KJF9MYH7S8OU_61WTI5N.jpg\", \"Y39M1P8R2_V6TDJXKI5F.jpg\", \"0LVSZ2TY4BOE_6W8P3HQ.jpg\", \"SAJWMNRZVU1OQY3CHTLE.jpg\", \"B32J0ENH1T8GU5CSV6Y9.jpg\", \"T7SBELD80IARFCHPK59V.jpg\", \"R6SCPDVBX2QE1YO8J9LH.jpg\", \"NRPO8IJB3XL06WADCFHT.jpg\", \"8M5RECXHA3QTZ2F749_B.jpg\", \"8VD19H0BQI3GYF6E7RTN.j','secundaria'),(265,'2023-11-25','Muestra Primaria.','I3LOMP4FG7B82TA_RQVH.jpg','Los alumnos hicieron un excelente trabajo para la muestra anual de primaria 2023. Gracias a todas las familias que se acercaron y acompañaron a sus hijos','[\"RXV5ISW9PEUF60_7DN14.jpg\", \"ZD6G3VP_TL9M8SHEK2QI.jpg\", \"WDN_XL93MY4IS0BV7OTH.jpg\", \"5N9GM0S42WZJIRP7FOKV.jpg\", \"W6FC7AO9PTBV3LD0MHY5.jpg\", \"YB4J5FGVRP6C3_AQXHZO.jpg\", \"KHM3ROLBN4P7IXWAY90S.jpg\", \"Z1ANJ9I8XRK_G20UPSL6.jpg\", \"9EN406JKDYLWVGZ3P18Q.jpg\", \"LYRHXD9TK647A_ZCO3JG.jpg\", \"Z01TQ97IPUMC2GWXBKJ3.jpg\", \"ZSMAOTCJ5BPFND4ULVRX.jpg\", \"UPX9248ZCYBKN_QMW3LS.jpg\", \"M28I1EQHVN_9COUXY7LB.jpg\", \"GY5W9SPVNMJUADO_84TQ.jpg\", \"JA_9LQMCHZ6312IGRYXP.jpg\", \"CGQE2B1_DS8IWVKHL37R.jpg\", \"ZSJELD5KA_0PYV4MHQC3.j','primaria'),(266,'2023-11-25','Visita mamá de More.','HMZ7PRVABFKQY0SLDT8C.jpg','Fotos de la visita de la mamá de Mora que nos enseñó hacer un riquísimo helado','[\"6BUOZXS59NLHFG38JMAW.jpg\", \"UR0Y3NIVOT79M1DHWZ8B.jpg\", \"L5UV9DOC7_PF4RBT30MS.jpg\", \"KR9F8OWCN251_AJ0VL4S.jpg\", \"VHPW49YAXRQDFGCNBTEL.jpg\"]','inicial');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-07 21:57:55
