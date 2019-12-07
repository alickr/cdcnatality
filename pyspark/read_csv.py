import sys
 
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row, SparkSession
from pyspark.sql.types import *
 
if __name__ == "__main__":
 
  # create Spark context with Spark configuration
  #conf = SparkConf().setAppName("Word Count - Python").set("spark.hadoop.yarn.resourcemanager.address", "192.168.0.104:8032")
  

  sparkConf = SparkConf().setAppName("Capstone Project").setMaster("local[4]").set("spark.executor.memory","2g")
  sc = SparkContext(conf=sparkConf)

  spark = SparkSession.builder.appName("Example").master("local[4]").getOrCreate()

  filePath='/Users/babu/Desktop/nyc_bootcamp/nyc/data_engineering/bootcamp/hadoop-tutorials/data/csv/Nat2018us.csv'
  #filePath='/Users/babu/Desktop/nyc_bootcamp/nyc/data_engineering/bootcamp/hadoop-tutorials/data/infections_1.csv'
  
  largeRDD = sc.textFile(filePath)
#   print('-'*50)
#   print('-'*50)
#   print(largeRDD.take(5))
#   print('-'*50)
#   print('-'*50)
   
  parts = largeRDD.map(lambda l: l.split("\t"))
  firstElem = parts.first()
  parts_filtered = parts.filter(lambda x: firstElem != x)

  

  print('-'*50)
  print('-'*50)
  x = parts_filtered.first()
  print(type(x))
  print(x)
  print('-'*50)
  print('-'*50)

 


  # Convert each line to a Row.
  
  paka = parts_filtered.map(lambda p: Row(
   DOB_YY = p[0],DOB_MM = p[1], DOB_TT = p[2], DOB_WK = p[3], BFACIL = p[4], F_FACILITY = p[5], BFACIL3 = p[6], MAGE_IMPFLG = float(p[7]), MAGE_REPFLG = float(p[8]), MAGER = p[9], MAGER14 = p[10], MAGER9 = p[11], MBSTATE_REC = p[12], RESTATUS = p[13], MRACE31 = p[14], MRACE6 = p[15], MRACE15 = p[16], MBRACE = p[17], MRACEIMP = float(p[18]), MHISPX = p[19], MHISP_R = p[20], F_MHISP = p[21], MRACEHISP = p[22], MAR_P = p[23], DMAR = p[24], MAR_IMP = float(p[25]), F_MAR_P = p[26], MEDUC = p[27], F_MEDUC = p[28], FAGERPT_FLG = float(p[29]), FAGECOMB = p[30], FAGEREC11 = p[31], FRACE31 = p[32], FRACE6 = p[33], FRACE15 = p[34], FHISPX = p[35], FHISP_R = p[36], F_FHISP = p[37], FRACEHISP = p[38], FEDUC = p[39], F_FEDUC = p[40], PRIORLIVE = p[41], PRIORDEAD = p[42], PRIORTERM = p[43], LBO_REC = p[44], TBO_REC = p[45], ILLB_R = p[46], ILLB_R11 = p[47], ILOP_R = p[48], ILOP_R11 = p[49], ILP_R = p[50], ILP_R11 = p[51], PRECARE = p[52], F_MPCB = p[53], PRECARE5 = p[54], PREVIS = p[55], PREVIS_REC = p[56], F_TPCV = p[57], WIC  = p[58], F_WIC = p[59], CIG_0 = p[60], CIG_1 = p[61], CIG_2 = p[62], CIG_3 = p[63], CIG0_R = p[64], CIG1_R = p[65], CIG2_R = p[66], CIG3_R = p[67], F_CIGS_0 = p[68], F_CIGS_1 = p[69], F_CIGS_2 = p[70], F_CIGS_3 = p[71], CIG_REC = p[72], F_TOBACO = p[73], M_Ht_In = p[74], F_M_HT = p[75], BMI = float(p[76]), BMI_R = p[77], Pwgt_R = p[78], F_PWGT = p[79], DWgt_R = p[80], F_DWGT = p[81], WTGAIN = p[82], WTGAIN_REC = p[83], F_WTGAIN = p[84], RF_PDIAB = p[85], RF_GDIAB = p[86], RF_PHYPE = p[87], RF_GHYPE = p[88], RF_EHYPE = p[89], RF_PPTERM = p[90], F_RF_PDIAB = p[91], F_RF_GDIAB = p[92], F_RF_PHYPER = p[93], F_RF_GHYPER = p[94], F_RF_ECLAMP = p[95], F_RF_PPB = p[96], RF_INFTR = p[97], RF_FEDRG = p[98], RF_ARTEC= p[99], f_RF_INFT = p[100], F_RF_INF_DRG = p[101], F_RF_INF_ART = p[102], RF_CESAR = p[103], RF_CESARN = p[104], F_RF_CESAR = p[105], F_RF_NCESAR = p[106], NO_RISKS = p[107], IP_GON = p[108], IP_SYPH  = p[109], IP_CHLAM = p[110], IP_HEPB  = p[111], IP_HEPC= p[112], F_IP_GONOR = p[113], F_IP_SYPH = p[114], F_IP_CHLAM = p[115], F_IP_HEPATB = p[116], F_IP_HEPATC = p[117], NO_INFEC = p[118], OB_ECVS = p[119], OB_ECVF = p[120], F_OB_SUCC = p[121], F_OB_FAIL = p[122], LD_INDL = p[123], LD_AUGM  = p[124], LD_STER  = p[125], LD_ANTB  = p[126], LD_CHOR  = p[127], LD_ANES  = p[128], F_LD_INDL = p[129], F_LD_AUGM = p[130], F_LD_STER = p[131], F_LD_ANTB = p[132], F_LD_CHOR = p[133], F_LD_ANES = p[134], NO_LBRDLV = p[135], ME_PRES = p[136], ME_ROUT = p[137], ME_TRIAL = p[138], F_ME_PRES = p[139], F_ME_ROUT = p[140], F_ME_TRIAL = p[141], RDMETH_REC = p[142], DMETH_REC = p[143], F_DMETH_REC = p[144], MM_MTR = p[145], MM_PLAC = p[146], MM_RUPT = p[147], MM_UHYST = p[148], MM_AICU = p[149], F_MM_MTR  = p[150], F_MM_PLAC = p[151], F_MM_RUPT = p[152], F_MM_UHYST = p[153], F_MM_AICU = p[154], NO_MMORB = p[155], ATTEND = p[156], MTRAN = p[157], PAY = p[158], PAY_REC = p[159], F_PAY = p[160], F_PAY_REC = p[161], APGAR5 = p[162], APGAR5R = p[163], F_APGAR5 = p[164], APGAR10 = p[165], APGAR10R = p[166], DPLURAL = p[167], IMP_PLUR = float(p[168]), SETORDER_R = p[169], SEX = p[170], IMP_SEX = float(p[171]), DLMP_MM = p[172], DLMP_YY = p[173], COMPGST_IMP = float(p[174]), OBGEST_FLG  = float(p[175]), COMBGEST = p[176], GESTREC10 = p[177], GESTREC3 = p[178], LMPUSED  = float(p[179]), OEGest_Comb = p[180], OEGest_R10 = p[181], OEGest_R3 = p[182], DBWT = p[183], BWTR12 = p[184], BWTR4 = p[185], AB_AVEN1 =  p[186], AB_AVEN6 =  p[187], AB_NICU =  p[188], AB_SURF =  p[189], AB_ANTI =  p[190], AB_SEIZ =  p[191], F_AB_VENT = p[192], F_AB_VENT6 = p[193], F_AB_NIUC = p[194], F_AB_SURFAC = p[195], F_AB_ANTIBIO = p[196], F_AB_SEIZ = p[197], NO_ABNORM = p[198], CA_ANEN =  p[199], CA_MNSB =  p[200], CA_CCHD =  p[201], CA_CDH =  p[202], CA_OMPH =  p[203], CA_GAST =  p[204], F_CA_ANEN = p[205], F_CA_MENIN = p[206], F_CA_HEART = p[207], F_CA_HERNIA = p[208], F_CA_OMPHA = p[209], F_CA_GASTRO = p[210], CA_LIMB =  p[211], CA_CLEFT =  p[212], CA_CLPAL =  p[213], CA_DOWN =  p[214], CA_DISOR =  p[215], CA_HYPO =  p[216], F_CA_LIMB = p[217], F_CA_CLEFTLP = p[218], F_CA_CLEFT = p[219], F_CA_DOWNS = p[220], F_CA_CHROM = p[221], F_CA_HYPOS = p[222], NO_CONGEN = p[223], ITRAN =  p[224], ILIVE =  p[225], BFED =  p[226], F_BFED = p[227]))


  pakaDF = spark.createDataFrame(paka)
  #infectionsDF.prSchema()
  #infectionsDF.show(5)

  # DataFrame.dtypes returns a list of tuples that contains the datatype of each column object.
  # pr(infectionsDF.dtypes)