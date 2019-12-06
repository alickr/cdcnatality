import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sqlalchemy import create_engine
from importlib import reload
import reduce_columns_module as column_reducer
reload(column_reducer)

# child_2018 = pd.read_csv('data/2018_child.csv')
# child_2018.tail(5)
# del child_2018

year = 2016
prev_count = 0
while year >= 2016:

    dataFrame = pd.read_csv('data/full/Nat' + str(year) + 'us.csv')
    dataFrame.head(5)

    dataFrame1 = pd.read_csv('data/full/Nat' + str(2015) + 'us.csv')
    dataFrame1.head(5)

    start_id = prev_count + 1
    stop_id = dataFrame.shape[0] + start_id
    prev_count = dataFrame.shape[0]
    dataFrame['id'] = [i for i in range(start_id, stop_id)]
    dataFrame['child_id'] = dataFrame['id']

    cols_child = [
        'id', 'DOB_YY', 'DOB_MM', 'DOB_TT', 'DOB_WK', 'BFACIL', 'F_FACILITY', 'BFACIL3'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_child, year, "child")

    cols_apgar = [
        'child_id',
        'APGAR5', 'APGAR5R', 'F_APGAR5', 'APGAR10', 'APGAR10R', 'DPLURAL', 'IMP_PLUR', 'SETORDER_R'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_apgar, year, "apgar")

    cols_abnormal_conditions_of_the_newborn = [
        'child_id',
        'AB_AVEN1', 'AB_AVEN6', 'AB_NICU', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6', 'F_AB_NIUC',
        'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_abnormal_conditions_of_the_newborn, year, "abnormal_conditions_of_the_newborn")

    cols_congenital_anomalies_of_the_newborn = [
        'child_id',
        'CA_ANEN', 'CA_MNSB', 'CA_CCHD', 'CA_CDH', 'CA_OMPH', 'CA_GAST', 'F_CA_ANEN', 'F_CA_MENIN', 'F_CA_HEART',
        'F_CA_HERNIA', 'F_CA_OMPHA', 'F_CA_GASTRO', 'CA_LIMB', 'CA_CLEFT', 'CA_CLPAL', 'CA_DOWN', 'CA_DISOR',
        'CA_HYPO', 'F_CA_LIMB', 'F_CA_CLEFTLP', 'F_CA_CLEFT', 'F_CA_DOWNS', 'F_CA_CHROM', 'F_CA_HYPOS', 'NO_CONGEN',
        'ITRAN', 'ILIVE', 'BFED', 'F_BFED',
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_congenital_anomalies_of_the_newborn, year, "congenital_anomalies_of_the_newborn")

    cols_delivery_attendant = [
        'child_id',
        'ATTEND', 'MTRAN', 'PAY', 'PAY_REC', 'F_PAY', 'F_PAY_REC'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_delivery_attendant, year, "delivery_attendant")

    cols_characteristics_of_labor_and_delivery = [
        'child_id',
        'LD_INDL', 'LD_AUGM', 'LD_STER', 'LD_ANTB', 'LD_CHOR', 'LD_ANES', 'F_LD_INDL', 'F_LD_AUGM', 'F_LD_STER',
        'F_LD_ANTB', 'F_LD_CHOR', 'F_LD_ANES', 'NO_LBRDLV'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_characteristics_of_labor_and_delivery, year, "characteristics_of_labor_and_delivery")

    cols_data_analysed_from_history = [
        'child_id',
        'PRIORLIVE', 'PRIORDEAD', 'PRIORTERM', 'LBO_REC', 'TBO_REC', 'ILLB_R', 'ILLB_R11', 'ILOP_R', 'ILOP_R11',
        'ILP_R', 'ILP_R11'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_data_analysed_from_history, year, "data_analysed_from_history")

    cols_father = [
        'child_id',
        'FAGERPT_FLG', 'FAGECOMB', 'FAGEREC11', 'FRACE31', 'FRACE6', 'FRACE15', 'FHISPX', 'FHISP_R', 'F_FHISP',
        'FRACEHISP', 'FEDUC', 'f_FEDUC'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_father, year, "father")

    cols_infection_present = [
        'child_id',
        'IP_GON', 'IP_SYPH', 'IP_CHLAM', 'IP_HEPB', 'IP_HEPC', 'F_IP_GONOR', 'F_IP_SYPH', 'F_IP_CHLAM', 'F_IP_HEPATB',
        'F_IP_HEPATC', 'NO_INFEC'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_infection_present, year, "infection_present")

    cols_maternal_morbidity = [
        'child_id',
        'MM_MTR', 'MM_PLAC', 'MM_RUPT', 'MM_UHYST', 'MM_AICU', 'F_MM_MTR', 'F_MM_PLAC', 'F_MM_RUPT', 'F_MM_UHYST',
        'F_MM_AICU', 'NO_MMORB'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_maternal_morbidity, year, "maternal_morbidity")

    cols_method_of_delivery = [
        'child_id',
        'ME_PRES', 'ME_ROUT', 'ME_TRIAL', 'F_ME_PRES', 'F_ME_ROUT', 'F_ME_TRIAL', 'RDMETH_REC', 'DMETH_REC', 'F_DMETH_REC'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_method_of_delivery, year, "method_of_delivery")

    cols_mother = [
        'child_id',
        'MAGE_IMPFLG', 'MAGE_REPFLG', 'MAGER', 'MAGER14', 'MAGER9', 'MBSTATE_REC', 'RESTATUS', 'MRACE31', 'MRACE6',
        'MRACE15', 'MBRACE', 'MRACEIMP', 'MHISPX', 'MHISP_R', 'F_MHISP', 'MRACEHISP', 'MAR_P', 'DMAR', 'MAR_IMP',
        'F_MAR_P', 'MEDUC', 'F_MEDUC'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_mother, year, "mother")

    cols_mother_height_weight = [
        'child_id',
        'M_Ht_In', 'F_M_HT', 'BMI', 'BMI_R', 'PWgt_R', 'F_PWGT', 'DWgt_R', 'F_DWGT', 'WTGAIN', 'WTGAIN_REC', 'F_WTGAIN'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_mother_height_weight, year, "mother_height_weight")

    cols_obstetric_procedures = [
        'child_id',
        'OB_ECVS', 'OB_ECVF', 'F_OB_SUCC', 'F_OB_FAIL'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_obstetric_procedures, year, "obstetric_procedures")

    cols_precare = [
        'child_id',
        'PRECARE', 'F_MPCB', 'PRECARE5', 'PREVIS', 'PREVIS_REC', 'F_TPCV'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_precare, year, "precare")

    cols_risk_factor = [
        'child_id',
        'RF_PDIAB', 'RF_GDIAB', 'RF_PHYPE', 'RF_GHYPE', 'RF_EHYPE', 'RF_PPTERM', 'F_RF_PDIAB', 'F_RF_GDIAB',
        'F_RF_PHYPER', 'F_RF_GHYPER', 'F_RF_ECLAMP', 'F_RF_PPB', 'RF_INFTR', 'RF_FEDRG', 'RF_ARTEC', 'f_RF_INFT',
        'F_RF_INF_DRG', 'F_RF_INF_ART', 'RF_CESAR', 'RF_CESARN', 'F_RF_CESAR', 'F_RF_NCESAR', 'NO_RISKS'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_risk_factor, year, "risk_factor")

    cols_sex_record = [
        'child_id',
        'SEX', 'IMP_SEX', 'DLMP_MM', 'DLMP_YY', 'COMPGST_IMP', 'OBGEST_FLG', 'COMBGEST', 'GESTREC10', 'GESTREC3',
        'LMPUSED', 'OEGest_Comb', 'OEGest_R10', 'OEGest_R3', 'DBWT', 'BWTR12', 'BWTR4'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_sex_record, year, "sex_record")

    cols_wic = [
        'child_id',
        'WIC', 'F_WIC', 'CIG_0', 'CIG_1', 'CIG_2', 'CIG_3', 'CIG0_R', 'CIG1_R', 'CIG2_R', 'CIG3_R', 'F_CIGS_0',
        'F_CIGS_1', 'F_CIGS_2', 'F_CIGS_3', 'CIG_REC', 'F_TOBACO'
    ]
    dataFrame = column_reducer.reduce_columns(dataFrame, cols_wic, year, "wic")
    year = year - 1


#
file_lists1 = [
    # 'abnormal_conditions_of_the_newborn',
    # 'apgar',
    # 'characteristics_of_labor_and_delivery',
    # 'child',
    # 'congenital_anomalies_of_the_newborn',
    # 'data_analysed_from_history',
    # 'delivery_attendant',
    # 'father',
    # 'infection_present',
    # 'maternal_morbidity',
    # 'method_of_delivery',
    # 'mother',
    # 'mother_height_weight',
    # 'obstetric_procedures',
    # 'precare',
    # 'risk_factor',
    # 'sex_record',
    # 'wic'
]

year1 = 2016

for item1 in file_lists1:
    df = pd.read_csv('data/' + str(year1) + '_' + item1 + ".csv")
    df.drop(['Unnamed: 0'], axis=1, errors='ignore', inplace=True)
    column_reducer.store_to_sql(df, item1)
    #column_reducer.store_to_sql(df, item1, row_id=12372402)
#