
import matplotlib.pyplot as plt

from lese_inn_data import FILNAVN, les_data



def plot_data(data):

    årstall = input("Skriv inn et årstall mellom 2014 og 2025 : ")
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

data = les_data(FILNAVN)
plot_data(data)

    