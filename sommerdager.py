import matplotlib.pyplot as plt


def finn_sommerdager(data, arstall, skriv_ut_resultat=True):
    """Teller antall sommerdager, høysommerdager og tropedager i ett gitt år.

    Definisjoner:
        Sommerdag     - en dag med maksimaltemperatur over 20 grader
        Høysommerdag  - en dag med maksimaltemperatur over 25 grader
        Tropedag      - en dag med maksimaltemperatur over 30 grader

    Parametere:
        data              - liste med dicts, én per dag, med nøklene "dato"
                            og "Maksimumstemperatur (døgn)"
        arstall           - året det skal telles for
        skriv_ut_resultat - skriver ut resultatet hvis True

    Returnerer en tuple (sommerdager, høysommerdager, tropedager).
    Dager uten målt maksimaltemperatur hoppes over.
    """
    
    antall_sommerdager = 0
    antall_hoysommerdager = 0
    antall_tropedager = 0

    for rad in data:
        if rad["dato"].year == arstall:
            makstemp = rad["Maksimumstemperatur (døgn)"]

            if makstemp is None:
                continue

            if makstemp > 20:
                antall_sommerdager += 1

            if makstemp > 25:
                antall_hoysommerdager += 1

            if makstemp > 30:
                antall_tropedager += 1

    if skriv_ut_resultat:
        print(f"Antall sommerdager i {arstall}: {antall_sommerdager}")
        print(f"Antall høysommerdager i {arstall}: {antall_hoysommerdager}")
        print(f"Antall tropedager i {arstall}: {antall_tropedager}")

    return antall_sommerdager, antall_hoysommerdager, antall_tropedager


def antall_per_ar(data):
    """Teller sommerdager, høysommerdager og tropedager for hvert år i datasettet.

    Returnerer en dict der nøkkelen er årstall og verdien er en tuple
    (sommerdager, høysommerdager, tropedager).
    """
    unike_ar = sorted(set(rad["dato"].year for rad in data))

    teller = {}
    for arstall in unike_ar:
        teller[arstall] = finn_sommerdager(data, arstall, skriv_ut_resultat=False)

    return teller


def plot_sommerdager(teller, stasjonsnavn):
    """Plotter antall sommerdager, høysommerdager og tropedager per år.

    Parametere:
        teller - dict fra antall_per_ar, med årstall som nøkkel og en tuple
        (sommerdager, høysommerdager, tropedager) som verdi
        stasjonsnavn - str, navn på værstasjonen
    """
    sommerdager = [verdi[0] for verdi in teller.values()]
    hoysommerdager = [verdi[1] for verdi in teller.values()]
    tropedager = [verdi[2] for verdi in teller.values()]
        
    arstall = list(teller.keys())
    plt.plot(arstall, sommerdager, label="Antall sommerdager")
    plt.plot(arstall, hoysommerdager, label="Antall høysommerdager")
    plt.plot(arstall, tropedager, label="Antall tropedager")
    plt.xlabel("År")
    plt.ylabel("Antall dager")
    plt.title(f"Sommerdager per år - {stasjonsnavn}")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    from lese_inn_data import les_data

    data = les_data(filnavn="oslo_blindern_1954_2025_med_makstemperatur.csv")
    teller = antall_per_ar(data)
    plot_sommerdager(teller, "Oslo-Blindern")