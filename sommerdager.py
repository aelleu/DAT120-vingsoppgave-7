
def antall_sommerdager(data, arstall):
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

    print(f"Antall sommerdager i {arstall}: {antall_sommerdager}")
    print(f"Antall høysommerdager i {arstall}: {antall_hoysommerdager}")
    print(f"Antall tropedager i {arstall}: {antall_tropedager}")
    return antall_sommerdager,antall_hoysommerdager, antall_tropedager

