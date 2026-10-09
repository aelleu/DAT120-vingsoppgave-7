from datetime import datetime

def antall_dager_skifore(data, arstall, snodybde=20):
    """Regn ut antall dager med skiføre fra juli til og med juni.

    Args:
        data: Liste med dict-er fra les_data.
        arstall: Året skisesongen slutter.
        snodybde: Minste snødybde i centimeter for at det skal være skiføre.

    Returns:
        Antall dager med skiføre, eller None hvis sesongen ikke finnes i dataene.
    """
    forste = min(rad["dato"].year for rad in data)
    siste = max(rad["dato"].year for rad in data)


    start = datetime(arstall - 1, 7, 1)
    slutt = datetime(arstall, 7, 1)

    if start.year < forste or slutt.year > siste:
        print(f"Sesongen {start.year}/{slutt.year} finnes ikke i datafilen")
        return

    antall = 0
    for rad in data:
        if start <= rad["dato"] < slutt:
            dybde = rad["Snødybde"]
            if dybde is not None and dybde >= snodybde:
                antall += 1
    print(f"Det var {antall} dager skiføre i sesongen {start.year}/{slutt.year}")
    return antall