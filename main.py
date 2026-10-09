from plotting import plot_data
from lese_inn_data import les_data
from skifore import antall_dager_skifore


def main():
    data = les_data()
    forste = min(rad["dato"].year for rad in data)
    siste = max(rad["dato"].year for rad in data)

    # Menyvalg
    valgmeny = {
        "1": ("Plott værdata for et år", plot_data), 
        "2": ("Antall dager med skiføre", antall_dager_skifore), 
        # "3": ("Plantevekst", plantevekst), 
        # "4": ("Lengste periode uten nedbør", lengste_tørkeperiode),
        # "5": ("Sommer-, høysommer- og tropedager", antall_sommerdager)
        }
    
    
    # Main loop
    while True:
        print("\n--- Værdata Sinnes ---")
        for tast, (tekst, _) in valgmeny.items():
            print(f"{tast}: {tekst}")
        print("b: Avslutt")

        valg = input("Valg: ").strip().lower()

        if valg == "b":
            break
        if valg not in valgmeny:
            print("Ugyldig valg. Prøv igjen.")
            continue

        _, funksjon = valgmeny[valg]
        
        # Hver funksjon skriver ut sitt eget resultat, så main trenger ikke print
        funksjon(data, les_ar(forste, siste))

        

def les_ar(forste, siste):
    while True:
        arstall = input(f"Skriv inn et årstall mellom {forste} og {siste}: ").strip()
        if arstall.isdigit() and forste <= int(arstall) <= siste:
            return int(arstall)
        print("Ugyldig årstall. Prøv igjen.")

if __name__ == "__main__":
    main()
    print("Programmet avsluttes")