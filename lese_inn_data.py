import csv
from datetime import datetime

FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"


def til_float(verdi):
    verdi = verdi.strip()

    if verdi == "-":
        return None

    return float(verdi.replace(",", "."))


def les_data(filnavn):
    """Leser inn værdata fra CSV og returnerer liste med dicts"""
    data = []
    siste_dato = None



    KOLONNER = ["Maksimumstemperatur (døgn)",
        "Middeltemperatur (døgn)",
        "Nedbør (døgn)",
        "Høyeste middelvind (døgn)",
        "Snødybde"]


    with open(filnavn, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            dato_tekst = row["Tid(norsk normaltid)"].strip()

            if dato_tekst == "":
                continue

            dato = datetime.strptime(dato_tekst, "%d.%m.%Y")


            # la til for loop
            for kol in KOLONNER:
                row[kol] = til_float(row[kol])

            # Forkast datoer som ikke er nyere enn forrige dato
            if siste_dato is not None and dato <= siste_dato:
                continue

            siste_dato = dato
            row["dato"] = dato

            data.append(row)

    return data


