

FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"
def plantevekst(data, ar):
    MIN_TEMP = 5
    total_vekst = 0

    for rad in data:
        if rad["dato"].year == ar:
            middeltemp = rad.get("middeltemperatur")

            if middeltemp is None or middeltemp == "" or middeltemp == "-":
                continue

            if isinstance(middeltemp, str):
                middeltemp = float(middeltemp.replace(",", "."))

            if middeltemp > MIN_TEMP:
                dagens_vekst = middeltemp - MIN_TEMP
                total_vekst = total_vekst + dagens_vekst

    print(f"Total plantevekst for året {ar} er: {round(total_vekst, 2)}")
