df_columns = [
    "DOB_YY",
    "DOB_MM",
    "DOB_TT",
    "DOB_WK",
    "BFACIL",
    "F_FACILITY",
    "BFACIL3",
    "MAGE_IMPFLG",
    "MAGE_REPFLG",
    "MAGER",
    "MAGER14",
    "MAGER9",
    "MBSTATE_REC",
    "RESTATUS",
    "MRACE31",
    "MRACE6",
    "MRACE15",
    "MBRACE",
    "MRACEIMP",
    "MHISPX",
    "MHISP_R",
    "F_MHISP",
    "MRACEHISP",
    "MAR_P",
    "DMAR",
    "MAR_IMP",
    "F_MAR_P",
    "MEDUC",
    "F_MEDUC",
    "FAGERPT_FLG",
    "FAGECOMB",
    "FAGEREC11",
    "FRACE31",
    "FRACE6",
    "FRACE15",
    "FHISPX",
    "FHISP_R",
    "F_FHISP",
    "FRACEHISP",
    "FEDUC",
    "f_FEDUC",
    "PRIORLIVE",
    "PRIORDEAD",
    "PRIORTERM",
    "LBO_REC",
    "TBO_REC",
    "ILLB_R",
    "ILLB_R11",
    "ILOP_R",
    "ILOP_R11",
    "ILP_R",
    "ILP_R11",
    "PRECARE",
    "F_MPCB",
    "PRECARE5",
    "PREVIS",
    "PREVIS_REC",
    "F_TPCV",
    "WIC",
    "F_WIC",
    "CIG_0",
    "CIG_1",
    "CIG_2",
    "CIG_3",
    "CIG0_R",
    "CIG1_R",
    "CIG2_R",
    "CIG3_R",
    "F_CIGS_0",
    "F_CIGS_1",
    "F_CIGS_2",
    "F_CIGS_3",
    "CIG_REC",
    "F_TOBACO",
    "M_Ht_In",
    "F_M_HT",
    "BMI",
    "BMI_R",
    "Pwgt_R",
    "F_PWGT",
    "DWgt_R",
    "WTGAIN",
    "WTGAIN_REC",
    "F_WTGAIN",
    "RF_PDIAB",
    "RF_GDIAB",
    "RF_PHYPE",
    "RF_GHYPE",
    "RF_EHYPE",
    "RF_PPTERM",
    "F_RF_PDIAB",
    "F_RF_GDIAB",
    "F_RF_PHYPER",
    "F_RF_GHYPER",
    "F_RF_ECLAMP",
    "F_RF_PPB",
    "RF_INFTR",
    "RF_FEDRG",
    "RF_ARTEC",
    "f_RF_INFT",
    "F_RF_INF_DRG",
    "F_RF_INF_ART",
    "RF_CESAR",
    "RF_CESARN",
    "F_RF_CESAR",
    "F_RF_NCESAR",
    "NO_RISKS",
    "IP_GON",
    "IP_SYPH",
    "IP_CHLAM",
    "IP_HEPB",
    "IP_HEPC",
    "F_IP_GONOR",
    "F_IP_SYPH",
    "F_IP_CHLAM",
    "F_IP_HEPATB",
    "F_IP_HEPATC",
    "NO_INFEC",
    "OB_ECVS",
    "OB_ECVF",
    "F_OB_SUCC",
    "F_OB_FAIL",
    "LD_INDL",
    "LD_AUGM",
    "LD_STER",
    "LD_ANTB",
    "LD_CHOR",
    "LD_ANES",
    "F_LD_INDL",
    "F_LD_AUGM",
    "F_LD_STER",
    "F_LD_ANTB",
    "F_LD_CHOR",
    "F_LD_ANES",
    "NO_LBRDLV",
    "ME_PRES",
    "ME_ROUT",
    "ME_TRIAL",
    "F_ME_PRES",
    "F_ME_ROUT",
    "F_ME_TRIAL",
    "RDMETH_REC",
    "DMETH_REC",
    "F_DMETH_REC",
    "MM_MTR",
    "MM_PLAC",
    "MM_RUPT",
    "MM_UHYST",
    "MM_AICU",
    "F_MM_MTR",
    "F_MM_ PLAC",
    "F_MM_RUPT",
    "F_MM_UHYST",
    "F_MM_AICU",
    "NO_MMORB",
    "ATTEND",
    "MTRAN",
    "PAY",
    "PAY_REC",
    "F_PAY",
    "F_PAY_REC",
    "APGAR5",
    "APGAR5R",
    "F_APGAR5",
    "APGAR10",
    "APGAR10R",
    "DPLURAL",
    "IMP_PLUR",
    "SETORDER_R",
    "SEX",
    "IMP_SEX",
    "DLMP_MM",
    "DLMP_YY",
    "COMPGST_IMP",
    "OBGEST_FLG",
    "COMBGEST",
    "GESTREC10",
    "GESTREC3",
    "LMPUSED",
    "OEGest_Comb",
    "OEGest_R10",
    "OEGest_R3",
    "DBWT",
    "BWTR12",
    "BWTR4",
    "AB_AVEN1",
    "AB_AVEN6",
    "AB_NICU",
    "AB_SURF",
    "AB_ANTI",
    "AB_SEIZ",
    "F_AB_VENT",
    "F_AB_VENT6",
    "F_AB_NIUC",
    "F_AB_SURFAC",
    "F_AB_ANTIBIO",
    "F_AB_SEIZ",
    "NO_ABNORM",
    "CA_ANEN",
    "CA_MNSB",
    "CA_CCHD",
    "CA_CDH",
    "CA_OMPH",
    "CA_GAST",
    "F_CA_ANEN",
    "F_CA_MENIN",
    "F_CA_HEART",
    "F_CA_HERNIA",
    "F_CA_OMPHA",
    "F_CA_GASTRO",
    "CA_LIMB",
    "CA_CLEFT",
    "CA_CLPAL",
    "CA_DOWN",
    "CA_DISOR",
    "CA_HYPO",
    "F_CA_LIMB",
    "F_CA_CLEFTLP",
    "F_CA_CLEFT",
    "F_CA_DOWNS",
    "F_CA_CHROM",
    "F_CA_HYPOS",
    "NO_CONGEN",
    "ITRAN",
    "ILIVE",
    "BFED",
    "F_BFED"
    ]

# df_columns