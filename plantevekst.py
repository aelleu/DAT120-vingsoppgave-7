from lese_inn_data import les_data

def plantevekst(data,årstall):
    total_plantevekst = 0
    MIN_TEMP = 5.0 # Minimumstemperatur for plantevekst
    for row in data:
        if row["dato"].year == årstall:
            if row["Middeltemperatur (døgn)"] is not None and row["Middeltemperatur (døgn)"] > MIN_TEMP:
                dagens_vekst = row["Middeltemperatur (døgn)"] - MIN_TEMP
                total_plantevekst += dagens_vekst
            continue
            
    print(f"Total plantevekst for året {årstall} er: {round(total_plantevekst,2)}")
    return total_plantevekst

if __name__ == "__main__":
    data = les_data()
    plantevekst(data)

