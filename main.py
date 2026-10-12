from plotting import plot_data
from lese_inn_data import les_data
from verfunksjoner import antall_dager_skifore, lengste_torkeperiode
from plantevekst import plantevekst
from sommerdager import antall_sommerdager


def main():
    data = les_data()
    forste = min(rad["dato"].year for rad in data)
    siste = max(rad["dato"].year for rad in data)

    # Menyvalg
    valgmeny = [
        ("Plott værdata for et år", plot_data), 
        ("Antall dager med skiføre", antall_dager_skifore), 
        ("Plantevekst", plantevekst), 
        ("Lengste periode uten nedbør", lengste_torkeperiode),
         ("Sommer-, høysommer- og tropedager", antall_sommerdager)
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

        # Sjekker om funksjonen trenger 2 eller fler argumenter
        if funksjon.__code__.co_argcount >= 2:
            arstall = les_ar(forste, siste)
            funksjon(data, arstall)
        else:
            funksjon(data)

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