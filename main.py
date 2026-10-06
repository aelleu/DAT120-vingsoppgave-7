import csv

FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"

with open(FILNAVN,"r",encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)


print("hallo")


# Oppgave e) Skiføre 
"""
Skiføre: Hvis vi antar at det er skiføre så lenge snødybden er minst 20cm, la brukeren
skrive inn et årstall og regn ut for et oppgitt år hvor mange dager det var skiføre den
skisesongen. En skisesong strekker seg fra november forrige år til mai dette året.
"""

""" hvordan bruke git??
 git pull                         # Hent andres endringer
 git status                       # Se hva som er endret
 git add filnavn.py               # Velg endringer som skal lagres
 git commit -m "Beskriv endringen" # Lagre dem lokalt
 git push                         # Last opp til GitHub
"""