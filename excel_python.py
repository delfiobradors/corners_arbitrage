# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:43:41 2016

@author: delfi
"""

import openpyxl
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
    
def delete_first_last(a):
    return (a[1:-1])

def convert_totcorners(df):
    #remove first and last character from total corners columns
    df.corners_home=df.corners_home.apply(delete_first_last)
    #convert times to number, since they are a string
    df.corners_home=df.corners_home.convert_objects(convert_numeric=True)
    df.corners_away=df.corners_away.apply(delete_first_last)
    df.corners_away=df.corners_away.convert_objects(convert_numeric=True)


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

def filter_two_teams_home(df,team_list):
    #MIRO CASA:
    x = df[(df['team_home']==team_list[0])]
    x=x.sort_index(by=['date'], ascending=[False])
    return x

def filter_two_teams_both(df,team_list):
    #MIRO AMBOS:
    x = df[(df['team_home']==team_list[0]) | (df['team_away']==team_list[1])]
    x=x.sort_index(by=['date'], ascending=[False])
    return x

def filter_two_teams_away(df,team_list):
    #MIRO FUERA:
    x = df[(df['team_away']==team_list[1])]
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

def return_pct_last_matches_home(df,num_matches,team_list):
    #given a row of the dataframe, filter the dataframe only with the involved teams
    df2=df[(df['team_home']==team_list[0])]
    df2=df2.sort_index(by=['date'], ascending=[False])
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
    
def return_pct_last_matches_both(df,num_matches,team_list):
    #given a row of the dataframe, filter the dataframe only with the involved teams
    df2=df[(df['team_home']==team_list[0]) | (df['team_away']==team_list[1])]
    df2=df2.sort_index(by=['date'], ascending=[False])
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
    
def return_pct_last_matches_away(df,num_matches,team_list):
    #given a row of the dataframe, filter the dataframe only with the involved teams
    df2=df[(df['team_away']==team_list[1])]
    df2=df2.sort_index(by=['date'], ascending=[False])
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

match1=[LPA,VIL]
match2=[EIB,ESP]
match3=[ATB,RMA]
match4=[ALA,RSO]
match5=[RBE,OSA]
match6=[LEG,MAL]
match7=[ATM,SEV]
match8=[SPO,GRA]
match9=[DEP,CEL]
match10=[BAR,VAL]

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

match21=[TOR,INT]
match22=[MIL,GEN]
match23=[EMP,NAP]
match24=[BOL,CHI]
match25=[ATA,PES]
match26=[CAG,LAZ]
match27=[SAM,JUV]
match28=[CRO,FIO]
match29=[UDI,PAL]
match30=[ASR,SAU]

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

match41=[WBR,ARS]
match42=[STO,CHE]
match43=[EVE,HUL]
match44=[SUN,BUR]
match45=[CPL,WFD]
match46=[WHM,LEI]
match47=[BMT,SWA]
match48=[MID,MAN]
match49=[TOT,SOU]
match50=[MCT,LIV]

LPZ='[RB Leipzig]'
FRE='[SC Freiburg]'
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

match61=[BDO,ING]
match62=[WOL,DAR]
match63=[COL,HBE]
match64=[AUG,FRE]
match65=[WER,LPZ]
match66=[HOF,BLE]
match67=[FRA,HAM]
match68=[MAI,SCH]
match69=[BMO,BMU]

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
#converts number of corners to number in order to be able to calculate totals later
convert_totcorners(df)
#reset indexes to be able to run the for loop
df = df.reset_index(drop=True)

wb = openpyxl.load_workbook('excelcalc.xlsx')
sheet = wb.get_sheet_by_name('Hoja1')

matches_list=[match1,match2,match3,match4,match5,match6,match7,match8,match9,match10,match21,match22,match23,match24,match25,match26,match27,match28,match29,match30,match41,match42,match43,match44,match45,match46,match47,match48,match49,match50,match61,match62,match63,match64,match65,match66,match67,match68,match69]

fila=2
for match in matches_list:
    sheet["A" + str(fila)] = match[0]
    sheet["B" + str(fila)] = match[1]
    sheet["C" + str(fila)] = return_pct_last_matches_home(df,30,match)
    sheet["D" + str(fila)] = return_pct_last_matches_both(df,30,match)
    sheet["E" + str(fila)] = return_pct_last_matches_away(df,30,match)
    sheet["L" + str(fila)] = len(filter_two_teams_home(df,match))
    sheet["M" + str(fila)] = len(filter_two_teams_both(df,match))
    sheet["N" + str(fila)] = len(filter_two_teams_away(df,match))
    fila=fila+1
    
df['corner9']=df.minc1<9

fila=2
for match in matches_list:
    sheet["F" + str(fila)] = return_pct_last_matches_home(df,30,match)
    sheet["G" + str(fila)] = return_pct_last_matches_both(df,30,match)
    sheet["H" + str(fila)] = return_pct_last_matches_away(df,30,match)
    fila=fila+1
    
df['corner9']=df.minc1<11

fila=2
for match in matches_list:
    sheet["I" + str(fila)] = return_pct_last_matches_home(df,30,match)
    sheet["J" + str(fila)] = return_pct_last_matches_both(df,30,match)
    sheet["K" + str(fila)] = return_pct_last_matches_away(df,30,match)
    fila=fila+1

#calculando el total de corners de los partidos
df['total_corners']=df.corners_home+df.corners_away

#linea 9,5 corners
df['corner9']=df.total_corners>9.5

fila=2
for match in matches_list:
    sheet["O" + str(fila)] = return_pct_last_matches_home(df,30,match)
    sheet["P" + str(fila)] = return_pct_last_matches_both(df,30,match)
    sheet["Q" + str(fila)] = return_pct_last_matches_away(df,30,match)
    fila=fila+1

#linea 10,5 corners
df['corner9']=df.total_corners>10.5

fila=2
for match in matches_list:
    sheet["R" + str(fila)] = return_pct_last_matches_home(df,30,match)
    sheet["S" + str(fila)] = return_pct_last_matches_both(df,30,match)
    sheet["T" + str(fila)] = return_pct_last_matches_away(df,30,match)
    fila=fila+1

wb.save('excelcalc.xlsx')
#print len(filter_two_teams(df,match1))
#ahora ya tengo los corners convertidos, actualizar el  df['corner9']=df.minc1<11 con la linea de corners y sacar pcts