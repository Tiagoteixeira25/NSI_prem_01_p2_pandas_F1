import pandas as pd
import numpy as np

F1 = pd.read_csv("Classeur_projet.csv", encoding = "ISO-8859-1")
print (F1.head())
print (F1.dtypes)


n = F1["nom pilote"]
a = F1["abandon"]
gp = F1["grand prix"]
pa = F1["pourcentage d'abandon"]
a1 = F1["abandon T1"]
nv = F1["nombre de victoire"]
pv = F1["pourcentage de victoire"]
mps = F1["moyenne de points par saison"]
ncm = F1["nombre de championnat du monde"]
ns = F1["nombre de saison"]
npp = F1["nombre de pole position"]
npm = F1["nombre de podium"]
e = F1["ecurie"]


#df = pandas.DataFrame({'LH': [27,284,9.44,4,102,35.66,274.77,7,16,103,182,10],\
#                + 'VB':[17,176,9.66,1,10,5.68,190.56,0,9,20,67,10], \
#                + 'MV':[29,139,20.86,6,19,13.67,216.21,1,7,13,60,9],\
#                + 'SP':[26,211,12.32,4,2,0.81,81.45,0,10,0,15,9], \
#                + 'LN':[8,58,13.79,0,0,0.00,99.67,0,3,1,5,7], \
#                + 'DR':[34,208,16.35,1,8,3.68,114.91,0,10,3,30,7], \
#                + 'CL':[14,78,17.83,4,2,2.56,138.25,0,4,9,13,8], \
#                + 'CS':[27,138,19.57,5,0,0.00,73.93,0,6,0,6,8], \
#                + 'SV':[40,217,14.4,7,53,19.13,204.07,4,15,57,122,3], \
#                + 'LS':[19,98,19.49,4,0,0.00,35.2,0,4,1,3,3], \
#                + 'EO':[13,87,14.94,5,1,1.15,51.6,0,6,0,2,5], \
#                + 'FA':[69,332,20.78,7,32,9.64,109.78,2,18,22,98,5],\
#                + 'PG':[15,84,17.86,3,1,1.19,58.2,0,5,0,3,4],\
#                + 'YT':[3,19,15.79,1,0,0.00,20.0,0,1,0,0,4],\
#                + 'KR':[71,348,20.4,11,21,6.03,98.58,1,18,18,103,1],\
#                + 'AG':[6,60,10.0,0,0,0.00,4.64,0,5,0,0,1],\
#                + 'NM':[4,20,20.0,1,0,0.00,0.0,0,1,0,0,0],\
#                + 'MS':[2,20,10.0,1,0,0.00,0.0,0,1,0,0,0],\
#                + 'GR':[10,58,17.24,0,0,0.00,6.33,0,3,0,1,2],\
#                + 'NL':[7,37,18.37,1,0,0.00,3.5,0,2,0,0,2]})\
#                + index = ['Abandon','Grand Prix',\
#                +'Pourcentage d Abandon','Abandon T1','Nombre Victoire',\
#                +'Pourcentage Victoire','Moyenne Point Saison',\
#                +'Nombre Championnat Mondial','Nombre Saison',\
#                +'Nombre Pole Position','Nombre Podium', 'Ecurie']


#def ihm
def comparaison():
    texte = 0
    return texte