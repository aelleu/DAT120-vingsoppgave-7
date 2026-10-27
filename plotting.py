import matplotlib.pyplot as plt
from lese_inn_data import les_data, finn_stasjoner
import numpy as np


def plot_data(data, årstall):
    """Plotter daglige værdata for ett gitt år.

    Plotter snødybde, nedbør, middeltemperatur og høyeste middelvind
    i samme figur, med dato på x-aksen.

    Parametere:
        data - liste med dicts, én per dag, med nøklene "dato",
                "Snødybde", "Nedbør (døgn)", "Middeltemperatur (døgn)"
                og "Høyeste middelvind (døgn)"
        årstall - året som skal plottes
    """
    snødybde = []
    nedbør = []
    middeltemperatur = []
    høyeste_middelvind = []
    dato = []
    for rad in data:
        if rad["dato"].year == int(årstall):
            dato.append(rad["dato"])
            snødybde.append(rad["Snødybde"])
            nedbør.append(rad["Nedbør (døgn)"])
            middeltemperatur.append(rad["Middeltemperatur (døgn)"])
            høyeste_middelvind.append(rad["Høyeste middelvind (døgn)"])

    plt.plot(dato, snødybde, label = "Snødybde i cm")
    plt.plot(dato, nedbør, label = "Nedbør i mm")
    plt.plot(dato, middeltemperatur, label = "Middeltemperatur i °C")
    plt.plot(dato, høyeste_middelvind, label = "Høyeste middelvind i m/s")

    plt.xlabel("Dato")
    plt.ylabel("Verdi")
    plt.title(f"Værdata for {årstall}")
    plt.legend()
    plt.show()


def arlig_gjennomsnittstemperatur(data, min_dager=300):
    """Regner ut gjennomsnittstemperaturen for hvert år med nok data.

    Dager uten målt middeltemperatur telles ikke med.

    Parametere:
        data      - liste med dicts, én per dag, med nøklene "dato"
                    og "Middeltemperatur (døgn)"
        min_dager - minste antall dager med måling for at året tas med

    Returnerer en dict der nøkkelen er årstall og verdien er
    gjennomsnittstemperaturen for det året. År med færre enn min_dager
    målinger får verdien None.
    """

    temperatur_dict = {}
    for rad in data:
        arstall = rad["dato"].year

        if arstall not in temperatur_dict:
            temperatur_dict[arstall] = []

        temperatur = rad["Middeltemperatur (døgn)"]
        if temperatur is None:
            continue
        temperatur_dict[arstall].append(temperatur)

    # Sjekker om det er mindre enn min_dager temperaturer
    for arstall, liste in temperatur_dict.items():
        if len(liste) < min_dager:
            temperatur_dict[arstall] = None
        else:
            temperatur_dict[arstall] = np.mean(liste)

    return temperatur_dict


def plot_gjennomsnitt(stasjoner):
    """Plotter årlig gjennomsnittstemperatur for flere værstasjoner.

    Parametere:
        stasjoner - dict der nøkkelen er stasjonsnavn og verdien er en
                    dict fra arlig_gjennomsnittstemperatur
    """
    for stasjonsnavn, temperaturer in stasjoner.items():
        arstall = list(temperaturer.keys())
        temperatur = list(temperaturer.values())
        plt.plot(arstall, temperatur, label=stasjonsnavn,
                marker="o", markersize=3)

    plt.title("Gjennomsnittstemperatur per år")
    plt.xlabel("Årstall")
    plt.ylabel("Temperatur (°C)")
    plt.legend()
    plt.show()


def sammenlign_temperaturer():
    """Plotter årlig gjennomsnittstemperatur for alle værstasjonene.

    Leser inn alle CSV-filene funnet av finn_stasjoner, regner ut
    gjennomsnittstemperaturen for hvert år med nok data, og plotter
    alle stasjonene i samme figur.
    """

    stasjoner = {}
    for sti in finn_stasjoner().values():
        data = les_data(filnavn=sti)
        stasjoner[data[0]["Navn"]] = arlig_gjennomsnittstemperatur(data)
    plot_gjennomsnitt(stasjoner)


if __name__ == "__main__":
    sammenlign_temperaturer()