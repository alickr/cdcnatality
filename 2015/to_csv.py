import csv
import pandas as pd
from columns_2015 import list_columns_2015

f = open("data/txt/Nat2015PublicUS.c20160517.r20160907.txt", "r")

file = open('../csv/cdc_2015.csv', 'w', encoding='utf-8', newline='')
output = csv.writer(file)
output.writerow(list_columns_2015) 

 
for item in f.readlines():
    df = {}
    df['DOB_YY'] = item[8:12]
    df['DOB_MM'] = item[12:14]
    df['DOB_TT'] = item[18:22]
    df['DOB_WK'] = item[22:23]
    df['BFACIL'] = item[31:32]
    df['F_FACILITY'] = item[32:33]
    df['BFACIL3'] = item[49:50]
    df['MAGE_IMPFLG'] = item[72:73]
    df['MAGE_REPFLG'] = item[73:74]
    df['MAGER'] = item[74:76]
    df['MAGER14'] = item[76:78]
    df['MAGER9'] = item[78:79]
    df['MBSTATE_REC'] = item[83:84]
    df['RESTATUS'] = item[103:104]
    df['MRACE31'] = item[104:106]
    df['MRACE6'] = item[106:107]
    df['MRACE15'] = item[107:109]
    df['MBRACE'] = item[109:110]
    df['MRACEIMP'] = item[110:111]
    #df['MHISPX'] = item[111:112]
    df['MHISP_R'] = item[114:115]
    df['F_MHISP'] = item[115:116]
    df['MRACEHISP'] = item[116:117]
    df['MAR_P'] = item[118:119]
    df['DMAR'] = item[119:120]
    df['MAR_IMP'] = item[120:121]
    df['F_MAR_P'] = item[122:123]
    df['MEDUC'] = item[123:124]
    df['F_MEDUC'] = item[125:126]
    df['FAGERPT_FLG'] = item[141:142]
    df['FAGECOMB'] = item[146:148]
    df['FAGEREC11'] = item[148:150]
    df['FRACE31'] = item[150:152]
    df['FRACE6'] = item[152:153]
    df['FRACE15'] = item[153:155]
    #df['FHISPX'] = item[158:159]
    df['FHISP_R'] = item[159:160]
    df['F_FHISP'] = item[160:161]
    df['FRACEHISP'] = item[161:162]
    df['FEDUC'] = item[162:163]
    df['f_FEDUC'] = item[164:165]
    df['PRIORLIVE'] = item[170:172]
    df['PRIORDEAD'] = item[172:174]
    df['PRIORTERM'] = item[174:176]
    df['LBO_REC'] = item[178:179]
    df['TBO_REC'] = item[181:182]
    df['ILLB_R'] = item[197:200]
    df['ILLB_R11'] = item[200:202]
    df['ILOP_R'] = item[205:208]
    df['ILOP_R11'] = item[208:210]
    df['ILP_R'] = item[213:216]
    df['ILP_R11'] = item[216:218]
    df['PRECARE'] = item[223:225]
    df['F_MPCB'] = item[225:226]
    df['PRECARE5'] = item[226:227]
    df['PREVIS'] = item[237:239]
    df['PREVIS_REC'] = item[241:243]
    df['F_TPCV'] = item[243:244]
    df['WIC'] = item[250:251]
    df['F_WIC'] = item[251:252]
    df['CIG_0'] = item[252:254]
    df['CIG_1'] = item[254:256]
    df['CIG_2'] = item[256:258]
    df['CIG_3'] = item[258:260]
    df['CIG0_R'] = item[260:261]
    df['CIG1_R'] = item[261:262]
    df['CIG2_R'] = item[262:263]
    df['CIG3_R'] = item[263:264]
    df['F_CIGS_0'] = item[264:265]
    df['F_CIGS_1'] = item[265:266]
    df['F_CIGS_2'] = item[266:267]
    df['F_CIGS_3'] = item[267:268]
    df['CIG_REC'] = item[268:269]
    df['F_TOBACO'] = item[269:270]
    df['M_Ht_In'] = item[279:281]
    df['F_M_HT'] = item[281:282]
    df['BMI'] = item[282:286]
    df['BMI_R'] = item[286:287]
    df['PWgt_R'] = item[291:294]
    df['F_PWGT'] = item[294:295]
    df['DWgt_R'] = item[298:301]
    df['F_DWGT'] = item[302:303]
    df['WTGAIN'] = item[303:305]
    df['WTGAIN_REC'] = item[305:306]
    df['F_WTGAIN'] = item[306:307]
    df['RF_PDIAB'] = item[312:313]
    df['RF_GDIAB'] = item[313:314]
    df['RF_PHYPE'] = item[314:315]
    df['RF_GHYPE'] = item[315:316]
    df['RF_EHYPE'] = item[316:317]
    df['RF_PPTERM'] = item[317:318]
    df['F_RF_PDIAB'] = item[318:319]
    df['F_RF_GDIAB'] = item[319:320]
    df['F_RF_PHYPER'] = item[320:321]
    df['F_RF_GHYPER'] = item[321:322]
    df['F_RF_ECLAMP'] = item[322:323]
    df['F_RF_PPB'] = item[323:324]
    df['RF_INFTR'] = item[324:325]
    df['RF_FEDRG'] = item[325:326]
    df['RF_ARTEC'] = item[326:327]
    #df['f_RF_INFT'] = item[327:328]
    df['F_RF_INF_DRG'] = item[328:329]
    df['F_RF_INF_ART'] = item[329:330]
    df['RF_CESAR'] = item[330:331]
    df['RF_CESARN'] = item[331:333]
    df['F_RF_CESAR'] = item[334:335]
    df['F_RF_NCESAR'] = item[335:336]
    df['NO_RISKS'] = item[336:337]
    df['IP_GON'] = item[342:343]
    df['IP_SYPH'] = item[343:344]
    df['IP_CHLAM'] = item[344:345]
    df['IP_HEPB'] = item[345:346]
    df['IP_HEPC'] = item[346:347]
    df['F_IP_GONOR'] = item[347:348]
    df['F_IP_SYPH'] = item[348:349]
    df['F_IP_CHLAM'] = item[349:350]
    df['F_IP_HEPATB'] = item[350:351]
    df['F_IP_HEPATC'] = item[351:352]
    df['NO_INFEC'] = item[352:353]
    df['OB_ECVS']  = item[359:360]
    df['OB_ECVF'] = item[360:361]
    df['F_OB_SUCC'] = item[362:363]
    df['F_OB_FAIL'] = item[363:364]
    df['LD_INDL'] = item[382:383]
    df['LD_AUGM'] = item[383:384]
    df['LD_STER'] = item[384:385]
    df['LD_ANTB'] = item[385:386]
    df['LD_CHOR'] = item[386:387]
    df['LD_ANES'] = item[387:388]
    df['F_LD_INDL'] = item[388:389]
    df['F_LD_AUGM'] = item[389:390]
    df['F_LD_STER'] = item[390:391]
    df['F_LD_ANTB'] = item[391:392]
    df['F_LD_CHOR'] = item[392:393]
    df['F_LD_ANES'] = item[393:394]
    df['NO_LBRDLV'] = item[394:395]
    df['ME_PRES'] = item[400:401]
    df['ME_ROUT'] = item[401:402]
    df['ME_TRIAL'] = item[402:403]
    df['F_ME_PRES'] = item[403:404]
    df['F_ME_ROUT'] = item[404:405]
    df['F_ME_TRIAL'] = item[405:406]
    df['RDMETH_REC'] = item[406:407]
    df['DMETH_REC'] = item[407:408]
    df['F_DMETH_REC'] = item[408:409]
    df['MM_MTR'] = item[414:415]
    df['MM_PLAC'] = item[415:416]
    df['MM_RUPT'] = item[416:417]
    df['MM_UHYST'] = item[417:418]
    df['MM_AICU'] = item[418:419]
    df['F_MM_MTR'] = item[420:421]
    df['F_MM_PLAC'] = item[421:422]
    df['F_MM_RUPT'] = item[422:423]
    df['F_MM_UHYST'] = item[423:424]
    df['F_MM_AICU'] = item[424:425]
    df['NO_MMORB'] = item[426:427]
    df['ATTEND'] = item[432:433]
    df['MTRAN'] = item[433:434]
    df['PAY'] = item[434:435]
    df['PAY_REC'] = item[435:436]
    df['F_PAY'] = item[436:437]
    df['F_PAY_REC'] = item[437:438] 
    df['APGAR5'] = item[443:445] 
    df['APGAR5R'] = item[445:446]
    df['F_APGAR5'] = item[446:447]
    df['APGAR10'] = item[447:449]
    df['APGAR10R'] = item[449:450]
    df['DPLURAL'] = item[453:454]
    df['IMP_PLUR'] = item[455:456]
    df['SETORDER_R']  = item[458:459]
    df['SEX'] = item[474:475]
    df['IMP_SEX'] = item[475:476]
    df['DLMP_MM'] = item[476:478]
    df['DLMP_YY'] = item[480:484]
    df['COMPGST_IMP'] =  item[487:488]
    df['OBGEST_FLG'] =  item[488:489]
    df['COMBGEST'] =  item[489:491]
    df['GESTREC10'] =  item[491:493]
    df['GESTREC3']  =  item[493:494]
    df['LMPUSED'] =  item[497:498]
    df['OEGest_Comb'] = item[498:500]
    df['OEGest_R10'] = item[500:502]
    df['OEGest_R3'] = item[502:503]
    df['DBWT'] = item[503:507]
    df['BWTR12'] = item[508:510]
    df['BWTR4'] = item[510:511]
    df['AB_AVEN1'] = item[516:517]
    df['AB_AVEN6'] = item[517:518]
    df['AB_NICU'] = item[518:519]
    df['AB_SURF'] = item[519:520]
    df['AB_ANTI'] = item[520:521]
    df['AB_SEIZ'] = item[521:522]
    df['F_AB_VENT'] = item[523:524]
    df['F_AB_VENT6'] = item[524:525]
    df['F_AB_NIUC'] = item[525:526]
    df['F_AB_SURFAC'] = item[526:527]
    df['F_AB_ANTIBIO'] = item[527:528]
    df['F_AB_SEIZ'] = item[528:529]
    df['NO_ABNORM'] = item[530:531]
    df['CA_ANEN'] = item[536:537]
    df['CA_MNSB'] = item[537:538]
    df['CA_CCHD'] = item[538:539]
    df['CA_CDH'] = item[539:540]
    df['CA_OMPH'] = item[540:541]
    df['CA_GAST'] = item[541:542]
    df['F_CA_ANEN'] = item[542:543]
    df['F_CA_MENIN'] = item[543:544]
    df['F_CA_HEART']  = item[544:545]
    df['F_CA_HERNIA'] = item[545:546]
    df['F_CA_OMPHA'] = item[546:547]
    df['F_CA_GASTRO'] = item[547:548]
    df['CA_LIMB'] = item[548:549]
    df['CA_CLEFT'] = item[549:550]
    df['CA_CLPAL'] = item[550:551]
    df['CA_DOWN'] = item[551:552]
    df['CA_DISOR'] = item[552:553]
    df['CA_HYPO'] = item[553:554]
    df['F_CA_LIMB'] = item[554:555]
    df['F_CA_CLEFTLP'] = item[555:556]
    df['F_CA_CLEFT'] = item[556:557]
    df['F_CA_DOWNS'] = item[557:558]
    df['F_CA_CHROM'] = item[558:559]
    df['F_CA_HYPOS'] = item[559:560]
    df['NO_CONGEN'] = item[560:561]
    df['ITRAN'] = item[566:567]
    df['ILIVE'] = item[567:568]
    df['BFED'] = item[568:569]
    df['F_BFED'] = item[569:570]
    df['UBFACIL'] = item[1329:1330]
    df['URF_DIAB'] = item[1330:1331]
    df['URF_CHYPER'] = item[1331:1332]
    df['URF_PHYPER'] = item[1332:1333]
    df['URF_ECLAM'] = item[1333:1334]
    df['UME_FORCP'] = item[1334:1335]
    df['UME_VAC'] = item[1335:1336]
    df['UOP_INDUC'] = item[1336:1337]
    df['ULD_BREECH'] = item[1337:1338]
    df['UCA_ANEN'] = item[1339:1340]
    df['UCA_SPINA'] = item[1340:1341]
    df['UCA_OMPHA'] = item[1341:1342]
    df['UCA_CELFTLP'] = item[1342:1343]
    df['UCA_HERNIA'] = item[1343:1344]
    df['UCA_DOWNS'] = item[1344:1345]
    output.writerow(df.values())


print('done')