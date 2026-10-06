import csv

FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"


# Importerer med kolonnenavn fra csv fil: 
# "Navn" "Stasjon", "Tid(norsk normaltid)", "Maksimumstemperatur (døgn)",
# "Middeltemperatur (døgn)", "Nedbør (døgn)", "Høyeste middelvind (døgn)", "Snødybde"
def les_fil():
    """
    Leser FILNAVN og returnerer dataene kolonnevis

    Args:

    Returns:
        En dict der verdien peker til en individuell liste. 

    """


    with open(FILNAVN,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        rader = list(reader)
        temperatur = {
            kolonne: [rad[kolonne] for rad in rader]
            for kolonne in rader[0]
        }
        return temperatur

temperatur = les_fil()

# print(temperatur["Stasjon"]) for å velge Stasjon kolonnen

# Oppgave e) Skiføre 
"""
Skiføre: Hvis vi antar at det er skiføre så lenge snødybden er minst 20cm, la brukeren
skrive inn et årstall og regn ut for et oppgitt år hvor mange dager det var skiføre den
skisesongen. En skisesong strekker seg fra november forrige år til mai dette året.
"""
def antall_dager_skifore(arstall, snodybde=20):
    """
    Regner ut hvor mange dager det er skiføre den skisesongen 

    Args:
        arstall (int): Årstall for den respektive skisesongen
        snodybde (int or float): Minimun snødybde


    """