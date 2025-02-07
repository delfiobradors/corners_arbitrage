# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:42:15 2015

@author: delfi
"""
import pandas as pd
import numpy as np
import time
import datetime

def convert_dates(analysis_df):
    analysis_df.date=analysis_df.date.apply(convert_to_datetime)
    
    #this will return dates converted to ordinal in order to be able to filter easier
    #analysis_df.date=analysis_df.date.apply(convert_toordinal)
    

def convert_to_datetime(date):
    string2=(date[4:15])
    #if there is a problem will return date 1999-01-01
    try:
        conv_time=time.strptime(string2,'%d %b %Y')
        d=datetime.date(conv_time.tm_year, conv_time.tm_mon, conv_time.tm_mday)
    except:
        d=datetime.date(1999, 1, 1)
    return d

def filter_two_teams(df,team_list):
    #select all the rows where one of the teams is involved
    #PARA MIRAR TODOS LOS PARTIDOS DD HAN ESTADO INVOLUCRADOS
    #x = df[(df['team_home'].isin(team_list)) | (df['team_away'].isin(team_list))]
    #select rows where home team played as homoe and away team played as away

    #MIRO CASA:
    x = df[(df['team_home']==team_list[0])]
    #MIRO AMBOS:
    #x = df[(df['team_home']==team_list[0]) | (df['team_away']==team_list[1])]
    #MIRO FUERA:
    #x = df[(df['team_away']==team_list[1])]
    #sort with the newest matches on top
    x=x.sort_index(by=['date'], ascending=[False])
    return x

def return_pct_last_matches(df,num_matches,team_list):
    #given a row of the dataframe, filter the dataframe only with the involved teams
    df2=filter_two_teams(df,team_list)
    #select how many matches should we look back, and select only those
    df2=df2.head(num_matches)
    try:
        #calculate percentage of trues
        num_true=float(len(df2[df2.corner9==True]))
        num_tot=float(len(df2))
        percent=float(num_true/num_tot)*float(100)
    except:
        percent=np.nan
    return percent

df=pd.read_csv('corners_append.csv')
#PREPARE THE FILE TO RUN FUNCTIONS TO ADD COLUMNS OF LAST MATCHES PCT

#filter chosen competitions
#competition_list=['2014/2015 Italian Serie A','2014-2015 Barclays Premier League','2014/2015 Spanish Primera División','2014/15 German Bundesliga, 2014/2015 German Bundesliga','2015-2016 Barclays Premier League','2015/16 German Bundesliga, 2015/2016 German Bundesliga','2015/2016 Spanish Primera División','2015/2016 Italian Serie A','2016/2017 Spanish Primera División','2016/2017 German Bundesliga','2016/2017 Italian Serie A','2016-2017 Barclays Premier League']
competition_list=['2016/2017 Spanish Primera División','2016/2017 German Bundesliga','2016/2017 Italian Serie A','2016-2017 Barclays Premier League']
df = df[(df['competition'].isin(competition_list))]
#remove any duplicate matches (id)
df=df.drop_duplicates(subset='id',take_last=True)
#drop matches without minc1
df=df.dropna(subset = ['minc1'])
#add column for corner before 9 true or false
df['corner9']=df.minc1<10
#convert dates to be able to sort and compare
convert_dates(df)
#reset indexes to be able to run the for loop
df = df.reset_index(drop=True)
'''


'''

MAL='[Málaga]'
OSA='[Osasuna]'
ALA='[Alavés]'
LEG='[Leganes]'
SEV='[Sevilla FC]'
ESP='[Espanyol]'
GET='[Getafe]'
DEP='[Deportivo La Coruña]'
RSO='[Real Sociedad]'
RAY='[Rayo Vallecano]'
VAL='[Valencia]'
ATB='[Athletic Bilbao]'
BAR='[Barcelona]'
CEL='[Celta Vigo]'
LEV='[Levante]'
GRA='[Granada]'
EIB='[Eibar]'
VIL='[Villarreal]'
ATM='[Atletico Madrid]'
SPO='[Sporting Gijón]'
RMA='[Real Madrid]'
RBE='[Real Betis]'
LPA='[Las Palmas]'

match1=[RBE,LPA]
match2=[DEP,SEV]
match3=[BAR,MAL]
match4=[EIB,CEL]
match5=[ATM,RMA]
match6=[ALA,ESP]
match7=[VAL,GRA]
match8=[SPO,RSO]
match9=[ATB,VIL]
match10=[LEG,OSA]


JUV='[Juventus]'
NAP='[Napoli]'
ASR='[AS Roma]'
LAZ='[Lazio]'
BOL='[Bologna]'
UDI='[Udinese]'
FIO='[Fiorentina]'
MIL='[AC Milan]'
ATA='[Atalanta]'
INT='[Internazionale]'
PAL='[Palermo]'
GEN='[Genoa]'
SAU='[Sassuolo]'
EMP='[Empoli]'
TOR='[Torino]'
SAM='[Sampdoria]'
CES='[Cesena]'
FRO='[Frosinone]'
GEN='[Genoa]'
VER='[Hellas Verona]'
CHI='[Chievo Verona]'
CAR='[Carpi]'
PES='[US Pescara]'
CAG='[Cagliari]'
CRO='[Crotone]'

match21=[LAZ,JUV]
match22=[NAP,MIL]
match23=[INT,PAL]
match24=[TOR,BOL]
match25=[SAM,ATA]
match26=[SAU,PES]
match27=[CAG,ASR]
match28=[FIO,CHI]
match29=[GEN,CRO]
match30=[UDI,EMP]

MAN='[Manchester United]'
NCS='[Newcastle United]'
CPL='[Crystal Palace]'
ASV='[Aston Villa]'
LEI='[Leicester City]'
TOT='[Tottenham Hotspur]'
NOR='[Norwich City]'
STO='[Stoke City]'
SUN='[Sunderland]'
SWA='[Swansea City]'
WHM='[West Ham United]'
BMT='[AFC Bournemouth]'
WBR='[West Bromwich Albion]'
CHE='[Chelsea]'
EVE='[Everton]'
MCT='[Manchester City]'
WFD='[Watford]'
SOU='[Southampton]'
ARS='[Arsenal]'
LIV='[Liverpool]'
HUL='[Hull City]'
MID='[Middlesbrough]'
BUR='[Burnley]'

match41=[MAN,ARS]
match42=[LEI,SWA]
match43=[CPL,BMT]
match44=[WFD,ARS]
match45=[SOU,SUN]
match46=[EVE,STO]
match47=[CHE,BUR]
match48=[HUL,MAN]
match49=[WBR,MID]
match50=[MCT,WHM]

FRE='[FREIBURG]'
LPZ='[LEIPZIG]'

MAI='[Mainz]'
HOF='[TSG Hoffenheim]'
COL='[FC Cologne]'
BMO='[Borussia Monchengladbach]'
HAM='[Hamburg SV]'
FRA='[Eintracht Frankfurt]'
WOL='[VfL Wolfsburg]'
HBE='[Hertha Berlin]'
STU='[VfB Stuttgart]'
SCH='[Schalke 04]'
BDO='[Borussia Dortmund]'
BLE='[Bayer Leverkusen]'
WER='[Werder Bremen]'
ING='[FC Ingolstadt 04]'
DAR='[SV Darmstadt 98]'
BMU='[Bayern Munich]'
AUG='[FC Augsburg]'
HAN='[Hannover 96]'

match61=[BMU,WER]
match62=[BDO,MAI]
match63=[COL,DAR]
match64=[HAM,ING]
match65=[AUG,WOL]
match66=[FRA,SCH]
match67=[BMO,BLE]
match68=[HBE,FRE]
match69=[HOF,LPZ]

#perform the calculation at once for several matches
#print return_pct_last_matches(df,30,team_list)

matches_list=[match1,match2,match3,match4,match5,match6,match7,match8,match9,match10,match21,match22,match23,match24,match25,match26,match27,match28,match29,match30,match41,match42,match43,match44,match45,match46,match47,match48,match49,match50,match61,match62,match63,match64,match65,match66,match67,match68,match69]

for match in matches_list:
    print match
    print return_pct_last_matches(df,30,match)
    print len(filter_two_teams(df,match))
print filter_two_teams(df,match41)
#con el len() de esto podria mirar si tengo o no los 30 partidos
   
#para intentar hacer el filtro de df a partir de una fecha
#def filter_newer_dates(date)
#df = df[df.date < date]
