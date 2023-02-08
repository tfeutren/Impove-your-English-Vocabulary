# ------------------------ #
# ** i am bilingue soon ** #
# ------------------------ #

"Je note dans data.csv les mots que je ne connais pas en anglais"

#---------------------------------------------------------------
# importation des modules
import csv
import random as rd
from rich.console import Console

# --------------------------------------------------------------
# Lecteur du fichier data.csv

console = Console()

while True :
    fin=0
    nombreLigne=0
    with open("data.csv") as fichier_csv:
        reader = csv.reader(fichier_csv,delimiter=',')
        for ligne in reader:
            nombreLigne+=1
    with open("data.csv") as fichier_csv:
        reader = csv.reader(fichier_csv,delimiter=',')
        indiceL = rd.choice([k for k in range(1,nombreLigne)])
        indiceC = rd.choice([0,1])
        for ligne in reader:
            L=ligne
            if fin==indiceL:
                break
            fin+=1

    # --------------------------------------------------------------
    # Affichage TERMINAL

    print("")
    if indiceC==1:
        console.print(L[indiceC], style="bold blue")
        input("")
        console.print(L[0], style="bold red")
    else:
        console.print(L[indiceC], style="bold red")
        input("")
        console.print(L[1], style="bold blue")
    input("")
    print("--------------------")
