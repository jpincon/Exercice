# -*- coding: utf-8 -*-
"""
Created on Thu May 07 19:41:14 2015

@author: David PREVOST
"""

#Import des bibliothèques nécessaires
import matplotlib.pyplot as plt

#Ouverture du fichier
fichier="dep10aller_z.csv"
fi=open(fichier)
t=[]; acc=[] 
for li in fi: 
    if li[0] not in "abcdefghijklmnopqrstuvwxyz": 
        li_sep=[] 
        li_sep=li.split(",") 
        t.append(float(li_sep[0])) 
        acc.append(float(li_sep[1][:-1]))
#ajout joel
tempsDepart=t[0]
for i in range(len(t)):
    t[i]=t[i]-tempsDepart
    acc[i]=acc[i]-1
#Tracé de la première figure
plt.figure(1)   
plt.plot(t,acc) 
plt.title("Resultats experimentaux") 
plt.ylabel('acc (m/s²)') 
plt.xlabel("t (s)") 
plt.show() 
fi.close() 


