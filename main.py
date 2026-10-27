from lese_inn_data import les_data
from verfunksjoner import antall_dager_skifore, lengste_torkeperiode
from plantevekst import plantevekst
from plotting import plot_data, sammenlign_temperaturer
from sommerdager import finn_sommerdager, vis_sommerdager_per_ar

def main():
    print("Laster inn filen...")
    data = les_data()
    print("Filen lastet inn")
    forste = min(rad["dato"].year for rad in data)
    siste = max(rad["dato"].year for rad in data)

    # Menyvalg
    valgmeny = [
        ("Plott værdata for et år", plot_data),
        ("Antall dager med skiføre", antall_dager_skifore),
        ("Plantevekst", plantevekst),
        ("Lengste periode uten nedbør", lengste_torkeperiode),
        ("Sommer-, høysommer- og tropedager for et år", finn_sommerdager),
        # TODO: legg til slik at man bare får et plot?
        ("Sommerdager per år (plott)", vis_sommerdager_per_ar),
        ("Sammenlign gjennomsnittstemperatur for alle stasjoner",
         sammenlign_temperaturer)
    ]
    
    # Main loop
    while True:
        print("\n--- Værdata Sinnes ---")
        for tast, (tekst, _) in enumerate(valgmeny, start=1):
            print(f"{tast}: {tekst}")
        print("b: Avslutt")

        valg = input("Valg: ").strip().lower()

        if valg == "b":
            break
        if not valg.isdigit() or not 1 <= int(valg) <= len(valgmeny):
            print("Ugyldig valg. Prøv igjen.")
            continue

        _, funksjon = valgmeny[int(valg) - 1]

        # Kaller funksjonen med riktig antall argumenter
        antall_argumenter = funksjon.__code__.co_argcount
        if antall_argumenter >= 2:
            arstall = les_ar(forste, siste)
            funksjon(data, arstall)
        elif antall_argumenter == 1:
            funksjon(data)
        else:
            funksjon()

        input("Trykk 'enter' for å fortsette")

def les_ar(forste, siste):
    while True:
        arstall = input(f"Skriv inn et årstall mellom {forste} og {siste}: ").strip()
        if arstall.isdigit() and forste <= int(arstall) <= siste:
            return int(arstall)
        print("Ugyldig årstall. Prøv igjen.")

if __name__ == "__main__":
    main()
    print("Programmet avsluttes")