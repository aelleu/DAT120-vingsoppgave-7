import pandas as pd

FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"

temperatur = pd.read_csv(FILNAVN, sep=";", decimal=",", na_values="-")
temperatur["Tid(norsk normaltid)"] = pd.to_datetime(temperatur["Tid(norsk normaltid)"], format="%d.%m.%Y")



def antall_dager_skifore(arstall, data, snodybde=20):
    """Regn ut antall dager med skiføre fra november til og med mai.

    Args:
        arstall: Året skisesongen slutter.
        data: DataFrame med dato- og snødybdekolonnene.
        snodybde: Minste snødybde i centimeter for at det skal være skiføre.

    Returns:
        Antall dager med skiføre i skisesongen.
    """
    start = pd.Timestamp(arstall - 1, 5, 30)
    slutt = pd.Timestamp(arstall, 6, 1)
    datoer = data["Tid(norsk normaltid)"]
    sesong = (datoer >= start) & (datoer < slutt)
    skifore = data.loc[sesong, "Snødybde"] >= snodybde
    return int(skifore.sum())


print(antall_dager_skifore(2017, temperatur))