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



#antall_sommerdager=0
#antall_høysommerdager=0
#antall_tropedager=0
#with open(FILNAVN, "r",encoding="UTF-8")as file:
#    reader=csv.reader(file,delimiter=";")
#    next(reader)
#    for row in reader:
#            dato=row[2]
#            dato_deler=dato.split(".")
#            if len(dato_deler)==3:
#                rad_år=dato.split(".")[2]
#            if rad_år==str(år):
#                if row[3] !="" and row[3] !="-":
#                      maksimaltemperatur=float(row[3].replace(",","."))
#                      if maksimaltemperatur>20:
#                          antall_sommerdager=antall_sommerdager+1
#                      if maksimaltemperatur>25:
#                          antall_høysommerdager=antall_høysommerdager+1
#                      if maksimaltemperatur>30:
#                          antall_tropedager=antall_tropedager+1
#print(f"Antall sommerdager året {år} er: {antall_sommerdager}")
#print(f"Antall høysommerdager året {år} er: {antall_høysommerdager}")
#print(f"Antall tropedager året {år} er: {antall_tropedager}")