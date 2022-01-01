from main_2 import Wisielec

w = Wisielec()
numer_ekranu = 0


def przygotowanie_gry():
    w.ustawianie_prob_obrazu()
    w.losowanie()
    w.rstrip()
    w.siatkowanie()
    w.generowanie_paskow()
    w.czyszczenie_konsoli()


def loop_gry():
    w.wyswietlanie_menu(0)
    w.wypisywanie_prob()
    w.wypisywanie_paskow()
    w.wyswietlanie_obrazkow()
    w.wprowadzenie_litery()
    w.sprawdzanie_litery()
    w.czyszczenie_konsoli()


def gra_w_wisielca():
    przygotowanie_gry()
    while True:
        if w.sprawdzanie_hasla() == False:
            loop_gry()
        else:
            if w.pytanie_o_next() == True:
                przygotowanie_gry()
            else:
                return 0


if __name__ == "__main__":

    while True:

        w.czyszczenie_konsoli()
        w.wyswietlanie_menu(1)
        numer_opcji = w.pytanie_o_tryb()

        if numer_opcji == 'P':
            gra_w_wisielca()

        elif numer_opcji == 'K':
            w.czyszczenie_konsoli()
            w.wyswietlanie_menu(2)
            w.pytanie_2()

        elif numer_opcji == 'I':
            w.czyszczenie_konsoli()
            w.wyswietlanie_menu(3)
            w.pytanie_2()

        elif numer_opcji == 'Q':
            w.czyszczenie_konsoli()
            w.wyswietlanie_menu(4)
            break
