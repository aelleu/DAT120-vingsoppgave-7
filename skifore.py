from datetime import datetime
# Import for debugging
from lese_inn_data import les_data

def antall_dager_skifore(arstall, data, snodybde=20):
    """Regn ut antall dager med skiføre fra juli til og med juni.

    Args:
        arstall: Året skisesongen slutter.
        data: Liste med dict-er fra les_data.
        snodybde: Minste snødybde i centimeter for at det skal være skiføre.

    Returns:
        Antall dager med skiføre i skisesongen.
    """
    start = datetime(arstall - 1, 7, 1)
    slutt = datetime(arstall, 7, 1)
    antall = 0
    for rad in data:
        if start <= rad["dato"] < slutt:
            dybde = rad["Snødybde"]
            if dybde is not None and dybde >= snodybde:
                antall += 1
    return antall


if __name__ == "__main__":
    FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"
    data = les_data(FILNAVN)
    print(antall_dager_skifore(2017, data))