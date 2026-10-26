import csv
from datetime import datetime
import os


def til_float(verdi):
    verdi = verdi.strip()

    if verdi == "-":
        return None

    return float(verdi.replace(",", "."))


def les_data(filnavn="sinnes_2014_2025_med_makstemperatur.csv",
             mappe="data"):
    """Leser inn værdata fra CSV og returnerer liste med dicts"""

    plassering = os.path.dirname(os.path.abspath(__file__))
    filsti = os.path.join(plassering, mappe ,filnavn)

    data = []
    siste_dato = None

    KOLONNER = ("Maksimumstemperatur (døgn)",
        "Middeltemperatur (døgn)",
        "Nedbør (døgn)",
        "Høyeste middelvind (døgn)",
        "Snødybde"
    )


    if not os.path.isfile(filsti):
        raise FileNotFoundError(f"Fant ikke filen: {filsti}")

    with open(filsti, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for rad in reader:
            dato_tekst = rad["Tid(norsk normaltid)"].strip()

            if dato_tekst == "":
                continue

            dato = datetime.strptime(dato_tekst, "%d.%m.%Y")


            # la til for loop
            for kol in KOLONNER:
                rad[kol] = til_float(rad[kol])

            # Forkast datoer som ikke er nyere enn forrige dato
            if siste_dato is not None and dato <= siste_dato:
                continue

            siste_dato = dato
            rad["dato"] = dato

            data.append(rad)

    return data

