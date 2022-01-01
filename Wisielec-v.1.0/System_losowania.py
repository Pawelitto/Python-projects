import random

def losowanie_kat_oraz_hasla():
    lista_z_wszystkimi_wyrazami = []

    wyrazy_do_losowania = []
    kategorie_do_losowania = []
    lista_tymczasowe_hasla = []
    numer_interacji = 0
    numer_interacji_wyrazow = 0


    with open('wyrazy.txt', 'r') as file:
        line = file.readline()
        while line:
            lista_z_wszystkimi_wyrazami.append(line.rstrip())
            line = file.readline()

    for element in lista_z_wszystkimi_wyrazami:

        if element.endswith(','):
            element_bez_znaku = element[:-1]
            wyrazy_do_losowania.append(element_bez_znaku)

        elif element.endswith(':'):
            wyrazy_do_losowania.append(numer_interacji)
            element_bez_znaku = element[:-1]
            kategorie_do_losowania.append(element_bez_znaku)

    nr_idx_kat = random.randint(0, len(kategorie_do_losowania) - 1)
    for element in wyrazy_do_losowania:

        if isinstance(element, (int)) == True:
            numer_interacji_wyrazow += 1

        if numer_interacji_wyrazow - 1 == nr_idx_kat:
            lista_tymczasowe_hasla.append(element)

    lista_tymczasowe_hasla.pop(0)
    nr_idx_has = random.randint(0, len(lista_tymczasowe_hasla) - 1)

    return kategorie_do_losowania[nr_idx_kat], lista_tymczasowe_hasla[nr_idx_has]
