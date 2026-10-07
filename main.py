import csv


FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"

MIN_TEMP=5
total_vekst=0
år=2024
with open(FILNAVN, "r",encoding="UTF-8")as file:
    reader=csv.reader(file,delimiter=";")
    next(reader)
    for row in reader:
        dato=row[2]
        dato_deler=dato.split(".")
        if len(dato_deler)==3:
            rad_år=dato.split(".")[2]
        if rad_år==str(år):
           if row[4] !="" and row[4] !="-":
               middeltemp=float(row[4].replace(",","."))
           if middeltemp > MIN_TEMP:
               dagens_vekst=middeltemp-MIN_TEMP 
               total_vekst=total_vekst + dagens_vekst         

print(f"Total plantevekst for året {år} er: {round(total_vekst,2)}")

antall_sommerdager=0
antall_høysommerdager=0
antall_tropedager=0
with open(FILNAVN, "r",encoding="UTF-8")as file:
    reader=csv.reader(file,delimiter=";")
    next(reader)
    for row in reader:
            dato=row[2]
            dato_deler=dato.split(".")
            if len(dato_deler)==3:
                rad_år=dato.split(".")[2]
            if rad_år==str(år):
                if row[3] !="" and row[3] !="-":
                      maksimaltemperatur=float(row[3].replace(",","."))
                      if maksimaltemperatur>20:
                          antall_sommerdager=antall_sommerdager+1
                      if maksimaltemperatur>25:
                          antall_høysommerdager=antall_høysommerdager+1
                      if maksimaltemperatur>30:
                          antall_tropedager=antall_tropedager+1
print(f"Antall sommerdager året {år} er: {antall_sommerdager}")
print(f"Antall høysommerdager året {år} er: {antall_høysommerdager}")
print(f"Antall tropedager året {år} er: {antall_tropedager}")
                              
                 