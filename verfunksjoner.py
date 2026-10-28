from datetime import datetime, timedelta

def antall_dager_skifore(data, arstall, snodybde=20, start_sesong=11,
                         slutt_sesong=4, min_andel=0.5,
                         skriv_ut_resultat=True):
    """Regn ut antall dager med skiføre i én skisesong.

    Skisesongen går fra første dag i start_sesong til siste dag i
    slutt_sesong. Standard er november til og med april. Sesongen
    forkastes hvis færre enn min_andel av dagene har målt snødybde.

    Args:
        data: Liste med dict-er fra les_data.
        arstall: Året skisesongen slutter.
        snodybde: Minste snødybde i centimeter for at det skal være skiføre.
        start_sesong: Måneden skisesongen starter, som heltall (1-12).
        slutt_sesong: Måneden skisesongen slutter, som heltall (1-12).
        min_andel: Minste andel av dagene i sesongen som må ha måling.
        skriv_ut_resultat: Om funksjonen skal skrive ut resultatet.

    Returns:
        Antall dager med skiføre, eller None hvis det er for lite data
        for sesongen.
    """
    # Går sesongen over årsskiftet, starter den året før arstall
    if start_sesong > slutt_sesong:
        start = datetime(arstall - 1, start_sesong, 1)
    else:
        start = datetime(arstall, start_sesong, 1)

    # Sesongen slutter ved starten av måneden etter slutt_sesong
    if slutt_sesong == 12:
        slutt = datetime(arstall + 1, 1, 1)
    else:
        slutt = datetime(arstall, slutt_sesong + 1, 1)

    antall_malinger = 0
    antall = 0
    for rad in data:
        if start <= rad["dato"] < slutt:
            dybde = rad["Snødybde"]
            if dybde is not None:
                antall_malinger += 1
                if dybde >= snodybde:
                    antall += 1

    # Datakrav: minst min_andel av dagene i sesongen må ha måling
    dager_i_sesongen = (slutt - start).days
    if antall_malinger < dager_i_sesongen * min_andel:
        if skriv_ut_resultat:
            print(f"For lite data for sesongen {start.year}/{arstall}")
        return None

    if skriv_ut_resultat:
        print(f"Det var {antall} dager skiføre i sesongen "
              f"{start.year}/{arstall}")
    return antall


def antall_dager_skifore_per_ar(data):
    """Teller antall dager skiføre for hvert år i datasettet.

    Args:
        data: Liste med dict-er fra les_data.

    Returnerer en dict der nøkkelen er årstall og verdien er int.
    """
    unike_ar = sorted(set(rad["dato"].year for rad in data))

    teller = {}
    for arstall in unike_ar:
        teller[arstall] = antall_dager_skifore(data, arstall, skriv_ut_resultat=False)

    return teller


def lengste_torkeperiode(data):
    """Regner ut lengste sammenhengende periode uten regn

    Args:
        data: Liste med dict-er fra les_data.

    Returns:
        (startdato, sluttdato, antall_dager) for den lengste tørkeperioden,
        eller None hvis ingen dager er uten nedbør.
    """

    sluttdato = None
    antall_dager = 0
    lengde = 0

    for rad in data:
        dato = rad["dato"]
        nedbor = rad["Nedbør (døgn)"]

        if nedbor == 0:
            # Hvis det ikke regner
            lengde += 1

            if lengde > antall_dager:
                antall_dager = lengde
                sluttdato = dato

        else: # Hvis det regner
            lengde = 0


    if sluttdato is None:
        print("Fant ingen dager uten regn")
        return

    startdato = sluttdato - timedelta(days=antall_dager - 1)

    print(f"Den lengste perioden uten regn var fra {startdato:%d.%m.%Y}"
          f" til {sluttdato:%d.%m.%Y}, den varte i {antall_dager} dager")
    return startdato, sluttdato, antall_dager

if __name__ == "__main__":
    from lese_inn_data import les_data
    data = les_data()
    print(antall_dager_skifore_per_ar(data))