# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.5.5-10.4.8-MariaDB)
# Database: nycds_project
# Generation Time: 2019-11-27 19:53:11 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table abnormal_conditions_of_the_newborn
# ------------------------------------------------------------

DROP TABLE IF EXISTS `abnormal_conditions_of_the_newborn`;

CREATE TABLE `abnormal_conditions_of_the_newborn` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `AB_AVEN1` varchar(11) DEFAULT NULL,
  `AB_AVEN6` varchar(11) DEFAULT NULL,
  `AB_NICU` varchar(11) DEFAULT NULL,
  `AB_SURF` varchar(11) DEFAULT NULL,
  `AB_ANTI` varchar(11) DEFAULT NULL,
  `AB_SEIZ` varchar(11) DEFAULT NULL,
  `F_AB_VENT` int(11) DEFAULT NULL,
  `F_AB_VENT6` int(11) DEFAULT NULL,
  `F_AB_NIUC` int(11) DEFAULT NULL,
  `F_AB_SURFAC` int(11) DEFAULT NULL,
  `F_AB_ANTIBIO` int(11) DEFAULT NULL,
  `F_AB_SEIZ` int(11) DEFAULT NULL,
  `NO_ABNORM` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table apgar
# ------------------------------------------------------------

DROP TABLE IF EXISTS `apgar`;

CREATE TABLE `apgar` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `APGAR5` int(11) DEFAULT NULL,
  `APGAR5R` int(11) DEFAULT NULL,
  `F_APGAR5` int(11) DEFAULT NULL,
  `APGAR10` int(11) DEFAULT NULL,
  `APGAR10R` int(11) DEFAULT NULL,
  `DPLURAL` int(11) DEFAULT NULL,
  `IMP_PLUR` int(11) DEFAULT NULL,
  `SETORDER_R` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table congenital_anomalies_of_the_newborn
# ------------------------------------------------------------

DROP TABLE IF EXISTS `congenital_anomalies_of_the_newborn`;

CREATE TABLE `congenital_anomalies_of_the_newborn` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `CA_ANEN` varchar(11) DEFAULT NULL,
  `CA_MNSB` varchar(11) DEFAULT NULL,
  `CA_CCHD` varchar(11) DEFAULT NULL,
  `CA_CDH` varchar(11) DEFAULT NULL,
  `CA_OMPH` varchar(11) DEFAULT NULL,
  `CA_GAST` varchar(11) DEFAULT NULL,
  `F_CA_ANEN` int(11) DEFAULT NULL,
  `F_CA_MENIN` int(11) DEFAULT NULL,
  `F_CA_HEART` int(11) DEFAULT NULL,
  `F_CA_HERNIA` int(11) DEFAULT NULL,
  `F_CA_OMPHA` int(11) DEFAULT NULL,
  `F_CA_GASTRO` int(11) DEFAULT NULL,
  `CA_LIMB` varchar(11) DEFAULT NULL,
  `CA_CLEFT` varchar(11) DEFAULT NULL,
  `CA_CLP_AL` varchar(11) DEFAULT NULL,
  `CA_DOWN` varchar(11) DEFAULT NULL,
  `CA_DISOR` varchar(11) DEFAULT NULL,
  `CA_HYPO` varchar(11) DEFAULT NULL,
  `F_CA_LIMB` int(11) DEFAULT NULL,
  `F_CA_CLEFTLP` int(11) DEFAULT NULL,
  `F_CA_CLEFT` int(11) DEFAULT NULL,
  `F_CA_DOWNS` int(11) DEFAULT NULL,
  `F_CA_CHROM` int(11) DEFAULT NULL,
  `F_CA_HYPOS` int(11) DEFAULT NULL,
  `NO_CONGEN` int(11) DEFAULT NULL,
  `ITRAN` varchar(11) DEFAULT NULL,
  `ILIVE` varchar(11) DEFAULT NULL,
  `BFED` varchar(11) DEFAULT NULL,
  `F_BFED` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table delivery_attendant
# ------------------------------------------------------------

DROP TABLE IF EXISTS `delivery_attendant`;

CREATE TABLE `delivery_attendant` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `ATTEND` int(11) DEFAULT NULL,
  `MTRAN` int(11) DEFAULT NULL,
  `PAY` int(11) DEFAULT NULL,
  `PAY_REC` int(11) DEFAULT NULL,
  `F_PAY` int(11) DEFAULT NULL,
  `F_PAY_REC` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table characteristics_of_labor_and_delivery
# ------------------------------------------------------------

DROP TABLE IF EXISTS `characteristics_of_labor_and_delivery`;

CREATE TABLE `characteristics_of_labor_and_delivery` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `LD_INDL` varchar(11) DEFAULT NULL,
  `LD_AUGM` varchar(11) DEFAULT NULL,
  `LD_STER` varchar(11) DEFAULT NULL,
  `LD_ANTB` varchar(11) DEFAULT NULL,
  `LD_CHOR` varchar(11) DEFAULT NULL,
  `LD_ANES` varchar(11) DEFAULT NULL,
  `F_LD_INDL` int(11) DEFAULT NULL,
  `F_LD_AUGM` int(11) DEFAULT NULL,
  `F_LD_STER` int(11) DEFAULT NULL,
  `F_LD_ANTB` int(11) DEFAULT NULL,
  `F_LD_CHOR` int(11) DEFAULT NULL,
  `F_LD_ANES` int(11) DEFAULT NULL,
  `NO_LBRDLV` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table child
# ------------------------------------------------------------

DROP TABLE IF EXISTS `child`;

CREATE TABLE `child` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `DOB_YY` int(11) DEFAULT NULL,
  `DOB_MM` int(11) DEFAULT NULL,
  `DOB_TT` int(11) DEFAULT NULL,
  `DOB_WK` int(11) DEFAULT NULL,
  `BFACIL` int(11) DEFAULT NULL,
  `F_FACILITY` int(11) DEFAULT NULL,
  `BFACIL3` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table data_analysed_from_history
# ------------------------------------------------------------

DROP TABLE IF EXISTS `data_analysed_from_history`;

CREATE TABLE `data_analysed_from_history` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) DEFAULT NULL,
  `PRIORLIVE` int(11) DEFAULT NULL,
  `PRIORDEAD` int(11) DEFAULT NULL,
  `PRIORTERM` int(11) DEFAULT NULL,
  `LBO_REC` int(11) DEFAULT NULL,
  `TBO_REC` int(11) DEFAULT NULL,
  `ILLB_R` int(11) DEFAULT NULL,
  `ILLB_R11` int(11) DEFAULT NULL,
  `ILOP_R` int(11) DEFAULT NULL,
  `ILOP_R11` int(11) DEFAULT NULL,
  `ILP_R` int(11) DEFAULT NULL,
  `ILP_R11` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table father
# ------------------------------------------------------------

DROP TABLE IF EXISTS `father`;

CREATE TABLE `father` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `FAGERPT_FLG` int(11) DEFAULT NULL,
  `FAGECOMB` int(11) DEFAULT NULL,
  `FAGEREC11` int(11) DEFAULT NULL,
  `FRACE31` int(11) DEFAULT NULL,
  `FRACE6` int(11) DEFAULT NULL,
  `FRACE15` int(11) DEFAULT NULL,
  `FHISPX` int(11) DEFAULT NULL,
  `FHISP_R` int(11) DEFAULT NULL,
  `F_FHISP` int(11) DEFAULT NULL,
  `FRACEHISP` int(11) DEFAULT NULL,
  `FEDUC` int(11) DEFAULT NULL,
  `f_FEDUC` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table infection_present
# ------------------------------------------------------------

DROP TABLE IF EXISTS `infection_present`;

CREATE TABLE `infection_present` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `IP_GON` varchar(11) DEFAULT NULL,
  `IP_SYPH` varchar(11) DEFAULT NULL,
  `IP_CHLAM` varchar(11) DEFAULT NULL,
  `IP_HEPB` varchar(11) DEFAULT NULL,
  `IP_HEPC` varchar(11) DEFAULT NULL,
  `F_IP_GONOR` int(11) DEFAULT NULL,
  `F_IP_SYPH` int(11) DEFAULT NULL,
  `F_IP_CHLAM` int(11) DEFAULT NULL,
  `F_IP_HEPATB` int(11) DEFAULT NULL,
  `F_IP_HEPATC` int(11) DEFAULT NULL,
  `NO_INFEC` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table maternal_morbidity
# ------------------------------------------------------------

DROP TABLE IF EXISTS `maternal_morbidity`;

CREATE TABLE `maternal_morbidity` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `MM_MTR` varchar(11) DEFAULT NULL,
  `MM_PLAC` varchar(11) DEFAULT NULL,
  `MM_RUPT` varchar(11) DEFAULT NULL,
  `MM_UHYST` varchar(11) DEFAULT NULL,
  `MM_AICU` varchar(11) DEFAULT NULL,
  `F_MM_MTR` int(11) DEFAULT NULL,
  `F_MM_PLAC` int(11) DEFAULT NULL,
  `F_MM_RUPT` int(11) DEFAULT NULL,
  `F_MM_UHYST` int(11) DEFAULT NULL,
  `F_MM_AICU` int(11) DEFAULT NULL,
  `NO_MMORB` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table method_of_delivery
# ------------------------------------------------------------

DROP TABLE IF EXISTS `method_of_delivery`;

CREATE TABLE `method_of_delivery` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `ME_PRES` int(11) DEFAULT NULL,
  `ME_ROUT` int(11) DEFAULT NULL,
  `ME_TRIAL` varchar(11) DEFAULT NULL,
  `F_ME_PRES` int(11) DEFAULT NULL,
  `F_ME_ROUT` int(11) DEFAULT NULL,
  `F_ME_TRIAL` int(11) DEFAULT NULL,
  `RDMETH_REC` int(11) DEFAULT NULL,
  `DMETH_REC` int(11) DEFAULT NULL,
  `F_DMETH_REC` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table mother
# ------------------------------------------------------------

DROP TABLE IF EXISTS `mother`;

CREATE TABLE `mother` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) DEFAULT NULL,
  `MAGE_IMPFLG` int(11) DEFAULT NULL,
  `MAGE_REPFLG` int(11) DEFAULT NULL,
  `MAGER` int(11) DEFAULT NULL,
  `MAGER14` int(11) DEFAULT NULL,
  `MAGER9` int(11) DEFAULT NULL,
  `MBSTATE_REC` int(11) DEFAULT NULL,
  `RESTATUS` int(11) DEFAULT NULL,
  `MRACE31` int(11) DEFAULT NULL,
  `MRACE6` int(11) DEFAULT NULL,
  `MRACE15` int(11) DEFAULT NULL,
  `MBRACE` int(11) DEFAULT NULL,
  `MRACEIMP` int(11) DEFAULT NULL,
  `MHISPX` int(11) DEFAULT NULL,
  `MHISP_R` int(11) DEFAULT NULL,
  `F_MHISP` int(11) DEFAULT NULL,
  `MRACEHISP` int(11) DEFAULT NULL,
  `MAR_P` varchar(11) DEFAULT NULL,
  `DMAR` int(11) DEFAULT NULL,
  `MAR_IMP` int(11) DEFAULT NULL,
  `F_MAR_P` int(11) DEFAULT NULL,
  `MEDUC` int(11) DEFAULT NULL,
  `F_MEDUC` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table mother_heigh_weight
# ------------------------------------------------------------

DROP TABLE IF EXISTS `mother_heigh_weight`;

CREATE TABLE `mother_heigh_weight` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `M_Ht_In` int(11) DEFAULT NULL,
  `F_M_HT` int(11) DEFAULT NULL,
  `BMI` int(11) DEFAULT NULL,
  `BMI_R` int(11) DEFAULT NULL,
  `PWgt_R` int(11) DEFAULT NULL,
  `F_PWGT` int(11) DEFAULT NULL,
  `DWgt_R` int(11) DEFAULT NULL,
  `F_DWGT` int(11) DEFAULT NULL,
  `WTGAIN` int(11) DEFAULT NULL,
  `WTGAIN_REC` int(11) DEFAULT NULL,
  `F_WTGAIN` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table obstetric_procedures
# ------------------------------------------------------------

DROP TABLE IF EXISTS `obstetric_procedures`;

CREATE TABLE `obstetric_procedures` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `OB_ECVS` varchar(11) DEFAULT NULL,
  `OB_ECVF` varchar(11) DEFAULT NULL,
  `F_OB_SUCC` int(11) DEFAULT NULL,
  `F_OB_FAIL` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table precare
# ------------------------------------------------------------

DROP TABLE IF EXISTS `precare`;

CREATE TABLE `precare` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `PRECARE` int(11) DEFAULT NULL,
  `F_MPCB` int(11) DEFAULT NULL,
  `PRECARE5` int(11) DEFAULT NULL,
  `PREVIS` int(11) DEFAULT NULL,
  `PREVIS_REC` int(11) DEFAULT NULL,
  `F_TPCV` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table risk_factor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `risk_factor`;

CREATE TABLE `risk_factor` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `RF_PDIAB` int(11) DEFAULT NULL,
  `RF_GDIAB` int(11) DEFAULT NULL,
  `RF_PHYPE` int(11) DEFAULT NULL,
  `RF_GHYPE` int(11) DEFAULT NULL,
  `RF_EHYPE` int(11) DEFAULT NULL,
  `RF_PPTERM` int(11) DEFAULT NULL,
  `F_RF_PDIAB` int(11) DEFAULT NULL,
  `F_RF_GDIAB` int(11) DEFAULT NULL,
  `F_RF_PHYPER` int(11) DEFAULT NULL,
  `F_RF_GHYPER` int(11) DEFAULT NULL,
  `F_RF_ECLAMP` int(11) DEFAULT NULL,
  `F_RF_PPB` int(11) DEFAULT NULL,
  `RF_INFTR` varchar(11) DEFAULT NULL,
  `RF_FEDRG` varchar(11) DEFAULT NULL,
  `RF_ARTEC` varchar(11) DEFAULT NULL,
  `f_RF_INFT` int(11) DEFAULT NULL,
  `F_RF_INF_DRG` int(11) DEFAULT NULL,
  `F_RF_INF_ART` int(11) DEFAULT NULL,
  `RF_CESAR` varchar(11) DEFAULT NULL,
  `RF_CESARN` int(11) DEFAULT NULL,
  `F_RF_CESAR` int(11) DEFAULT NULL,
  `F_RF_NCESAR` int(11) DEFAULT NULL,
  `NO_RISKS` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table sex_record
# ------------------------------------------------------------

DROP TABLE IF EXISTS `sex_record`;

CREATE TABLE `sex_record` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) unsigned DEFAULT NULL,
  `SEX` varchar(11) DEFAULT NULL,
  `IMP_SEX` varchar(11) DEFAULT NULL,
  `DLMP_MM` int(11) DEFAULT NULL,
  `DLMP_YY` int(11) DEFAULT NULL,
  `COMPGST_IMP` int(11) DEFAULT NULL,
  `OBGEST_FLG` int(11) DEFAULT NULL,
  `COMBGEST` int(11) DEFAULT NULL,
  `GESTREC10` int(11) DEFAULT NULL,
  `GESTREC3` int(11) DEFAULT NULL,
  `LMPUSED` int(11) DEFAULT NULL,
  `OEGest_Comb` int(11) DEFAULT NULL,
  `OEGest_R10` int(11) DEFAULT NULL,
  `OEGest_R3` int(11) DEFAULT NULL,
  `DBWT` int(11) DEFAULT NULL,
  `BWTR12` int(11) DEFAULT NULL,
  `BWTR4` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table wic
# ------------------------------------------------------------

DROP TABLE IF EXISTS `wic`;

CREATE TABLE `wic` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `child_id` int(11) DEFAULT NULL,
  `WIC` int(11) DEFAULT NULL,
  `F_WIC` int(11) DEFAULT NULL,
  `CIG_0` int(11) DEFAULT NULL,
  `CIG_1` int(11) DEFAULT NULL,
  `CIG_2` int(11) DEFAULT NULL,
  `CIG_3` int(11) DEFAULT NULL,
  `CIG0_R` int(11) DEFAULT NULL,
  `CIG1_R` int(11) DEFAULT NULL,
  `CIG2_R` int(11) DEFAULT NULL,
  `CIG3_R` int(11) DEFAULT NULL,
  `F_CIGS_0` int(11) DEFAULT NULL,
  `F_CIGS_1` int(11) DEFAULT NULL,
  `F_CIGS_2` int(11) DEFAULT NULL,
  `F_CIGS_3` int(11) DEFAULT NULL,
  `CIG_REC` int(11) DEFAULT NULL,
  `F_TOBACO` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
