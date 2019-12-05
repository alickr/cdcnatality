
/*FOLLOWING COMMANDS ARE TO BE MANIPULATED ON TERMINAL */

/* START DOCKER */
>docker run -it --rm -p 8088:8088 -p 50070:50070 -p 19888:19888 -v "$(pwd)":/home/hadoop/tutorials nycdsa/hadoop-bootcamp

/*MOVE TO HIVE*/
> cd ~/tutorials/hive/ 
> ./run-hive-jobs.sh

/*START HIVE*/
> hive

/*CREATE DATABASE

CREATE TABLES */

/* COMMANDS TO LOAD DATA TO THE DATABASE */
>LOAD DATA LOCAL INPATH '../data/csv/Nat2014us.csv' INTO TABLE tbl_nat_14;
>LOAD DATA LOCAL INPATH '../data/csv/Nat2015us.csv' INTO TABLE tbl_nat_15;
>LOAD DATA LOCAL INPATH '../data/csv/Nat2016us.csv' INTO TABLE tbl_nat_16;
>LOAD DATA LOCAL INPATH '../data/csv/Nat2017us.csv' INTO TABLE tbl_nat_17;
>LOAD DATA LOCAL INPATH '../data/csv/Nat2018us.csv' INTO TABLE tbl_nat_18;

/* QUERY TO DO GROUP BY MONTH */
select dob_mm, count(dob_mm) as number_birth from tbl_nat group by dob_mm order by number_birth DESC;

/* QUERY TO EXPORT GROUP BY DATA INTO A CSV */
>hive -e 'SELECT "month", "number_birth"
UNION ALL
SELECT CAST(dob_mm as CHAR(50)), CAST(count(dob_mm) as CHAR(50))
FROM cdc.tbl_nat
group by dob_mm' > /home/hadoop/tutorials/data/births_per_month.csv

/* select new born babies born in january */

>hive -e 'select "RF_PDIAB", "RF_GDIAB", "RF_PHYPE", "RF_GHYPE", "RF_EHYPE", "RF_PPTERM", "RF_INFTR", "RF_FEDRG", "RF_ARTEC", "RF_CESAR","RF_CESARN", "NO_RISKS", "AB_NICU"
UNION ALL
select CAST(RF_PDIAB as CHAR(50)), CAST(RF_GDIAB as CHAR(50)), CAST(RF_PHYPE as CHAR(50)), CAST(RF_GHYPE as CHAR(50)), CAST(RF_EHYPE as CHAR(50)), CAST(RF_PPTERM as CHAR(50)), CAST(RF_INFTR as CHAR(50)), CAST(RF_FEDRG as CHAR(50)), CAST(RF_ARTEC as CHAR(50)), CAST(RF_CESAR as CHAR(50)),CAST(RF_CESARN as CHAR(50)), CAST(NO_RISKS as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat 
where dob_mm = CAST(1 as CHAR(50))' > /home/hadoop/tutorials/data/natality18_january.csv


>hive -e 'select "MM_MTR", "MM_PLAC", "MM_RUPT", "MM_UHYST", "MM_AICU", "NO_MMORB", "AB_NICU"
UNION ALL
select CAST(MM_MTR as CHAR(50)), CAST(MM_PLAC as CHAR(50)), CAST(MM_RUPT as CHAR(50)), CAST(MM_UHYST as CHAR(50)), CAST(MM_AICU as CHAR(50)), CAST(NO_MMORB as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_18 
where dob_mm = CAST(1 as CHAR(50))' > /home/hadoop/tutorials/data/maternal_morbidity_18_1.csv


>hive -e 'select "IP_GON", "IP_SYPH" ,"IP_CHLAM", "IP_HEPB", "IP_HEPC", "NO_INFEC", "AB_NICU"
UNION ALL
select CAST(IP_GON as CHAR(50)), CAST(IP_SYPH as CHAR(50)), CAST(IP_CHLAM as CHAR(50)), CAST(IP_HEPB as CHAR(50)), CAST(IP_HEPC as CHAR(50)), CAST(NO_INFEC as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_18 
where dob_mm = CAST(1 as CHAR(50))' > /home/hadoop/tutorials/data/infections_18_1.csv


hive -e 'select "MM_MTR", "MM_PLAC", "MM_RUPT", "MM_UHYST", "MM_AICU", "NO_MMORB","AB_NICU"
UNION ALL
select CAST(MM_MTR as CHAR(50)), CAST(MM_PLAC as CHAR(50)), CAST(MM_RUPT as CHAR(50)), CAST(MM_UHYST as CHAR(50)), CAST(MM_AICU as CHAR(50)), CAST(NO_MMORB as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_14 
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(MM_MTR as CHAR(50)), CAST(MM_PLAC as CHAR(50)), CAST(MM_RUPT as CHAR(50)), CAST(MM_UHYST as CHAR(50)), CAST(MM_AICU as CHAR(50)), CAST(NO_MMORB as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_15 
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(MM_MTR as CHAR(50)), CAST(MM_PLAC as CHAR(50)), CAST(MM_RUPT as CHAR(50)), CAST(MM_UHYST as CHAR(50)), CAST(MM_AICU as CHAR(50)), CAST(NO_MMORB as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_16
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(MM_MTR as CHAR(50)), CAST(MM_PLAC as CHAR(50)), CAST(MM_RUPT as CHAR(50)), CAST(MM_UHYST as CHAR(50)), CAST(MM_AICU as CHAR(50)), CAST(NO_MMORB as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_17
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(MM_MTR as CHAR(50)), CAST(MM_PLAC as CHAR(50)), CAST(MM_RUPT as CHAR(50)), CAST(MM_UHYST as CHAR(50)), CAST(MM_AICU as CHAR(50)), CAST(NO_MMORB as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_18 
where dob_mm = CAST(1 as CHAR(50))' > /home/hadoop/tutorials/data/maternal_morbidity_1.csv


>hive -e 'select "IP_GON", "IP_SYPH" ,"IP_CHLAM", "IP_HEPB", "IP_HEPC", "NO_INFEC", "AB_NICU"
UNION ALL
select CAST(IP_GON as CHAR(50)), CAST(IP_SYPH as CHAR(50)), CAST(IP_CHLAM as CHAR(50)), CAST(IP_HEPB as CHAR(50)), CAST(IP_HEPC as CHAR(50)), CAST(NO_INFEC as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_14 
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(IP_GON as CHAR(50)), CAST(IP_SYPH as CHAR(50)), CAST(IP_CHLAM as CHAR(50)), CAST(IP_HEPB as CHAR(50)), CAST(IP_HEPC as CHAR(50)), CAST(NO_INFEC as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_15 
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(IP_GON as CHAR(50)), CAST(IP_SYPH as CHAR(50)), CAST(IP_CHLAM as CHAR(50)), CAST(IP_HEPB as CHAR(50)), CAST(IP_HEPC as CHAR(50)), CAST(NO_INFEC as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_16
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(IP_GON as CHAR(50)), CAST(IP_SYPH as CHAR(50)), CAST(IP_CHLAM as CHAR(50)), CAST(IP_HEPB as CHAR(50)), CAST(IP_HEPC as CHAR(50)), CAST(NO_INFEC as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_17 
where dob_mm = CAST(1 as CHAR(50))
UNION ALL
select CAST(IP_GON as CHAR(50)), CAST(IP_SYPH as CHAR(50)), CAST(IP_CHLAM as CHAR(50)), CAST(IP_HEPB as CHAR(50)), CAST(IP_HEPC as CHAR(50)), CAST(NO_INFEC as CHAR(50)), CAST(AB_NICU as CHAR(50))
from cdc.tbl_nat_18 
where dob_mm = CAST(1 as CHAR(50))' > /home/hadoop/tutorials/data/infections_1.csv