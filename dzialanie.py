import os
from grafiki import wys_obraz, wys_menu
from System_losowania import losowanie_kat_oraz_hasla


class Wisielec:

    def __init__(self):
        self.numer_obrazu = 0
        self.prawidlowe_proby = 6
        self.proby = 6
        self.pozycja_ciecia = 0
        self.lista_pomocnicza_do_liter = []
        self.lista_uzytkowa = []
        self.litery_gracza = []
        self.lista_posiatkowana = []
        self.stan_hasla = False
        self.stan_litery = False

    def czyszczenie_konsoli(self):
        czysc = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        czysc()

    def wyswietlanie_menu(self):
        wys_menu()

    def ustawianie_prob_obrazu(self):
        self.proby = self.prawidlowe_proby
        self.litery_gracza = []
        self.numer_obrazu = 0

    def losowanie(self):
        self.kategoria, self.wylosowany_wyraz = losowanie_kat_oraz_hasla()

    def rstrip(self):
        self.wylosowany_wyraz_bez = self.wylosowany_wyraz.rstrip().lower()

    def siatkowanie(self):
        self.lista_posiatkowana = []
        pozycja_ciecia = 0

        for i in range(len(self.wylosowany_wyraz_bez)):
            pociety = self.wylosowany_wyraz_bez[pozycja_ciecia]
            self.lista_posiatkowana.append(pociety)
            pozycja_ciecia += 1
            i += 1

    def generowanie_paskow(self):
        self.lista_uzytkowa = []
        for i in str(self.wylosowany_wyraz_bez):
            self.lista_uzytkowa.append('_')


    def wypisywanie_prob(self):
        print("Wylosowana kategoria:", self.kategoria)
        print(f'Próby: {self.proby}')


    def wypisywanie_paskow(self):
        for i in range(len(self.lista_uzytkowa)):
            print(self.lista_uzytkowa[i], end=' ')

        else:
            print("\t")


    def wyswietlanie_obrazkow(self):
        print(wys_obraz(self.numer_obrazu))



    def wprowadzenie_litery(self):
        self.stan_podananej_litery = True

        while self.stan_podananej_litery == True:
            self.litera_uzytkownika = str.lower(input("Podaj literę: "))
            if self.litera_uzytkownika.isalpha() == True and len(self.litera_uzytkownika) < 2:
                if self.litera_uzytkownika in self.litery_gracza:
                    print(f'Litera {self.litera_uzytkownika} się powtórzyła!')
                else:
                    self.litery_gracza.append(self.litera_uzytkownika)
                    self.stan_podananej_litery = False
            else:
                print("Prosimy podawać TYLKO po jednej literze oraz BRAK znaków specjalnych np. ';'")


    def sprawdzanie_litery(self):
        self.stan_litery = False

        for i in range(len(self.lista_posiatkowana)):
            if self.litera_uzytkownika == self.lista_posiatkowana[i]:
                self.lista_uzytkowa[i] = self.litera_uzytkownika
                self.stan_litery = True

        if self.stan_litery == False:
            self.proby -= 1
            self.numer_obrazu += 1


    def sprawdzanie_hasla(self):
        self.stan_hasla = False

        if self.lista_uzytkowa == self.lista_posiatkowana:
            self.stan_hasla = True
            print(f'Brawo odgadłeś hasło! {self.wylosowany_wyraz}')

        elif self.proby == 0:
            w.wyswietlanie_obrazkow()
            self.stan_hasla = True
            print('Koniec gry! Skończyły ci się próby.')
            print(f'Hasło gry "{self.wylosowany_wyraz_bez}"')
        return self.stan_hasla


    def pytanie_o_next(self):
        while True:
            pyt = input('Czy chcesz zagrać ponownie? (T/N): ').upper()
            if pyt.isalpha() == True and len(pyt) < 2 and pyt == 'T':
                return True
            elif pyt.isalpha() == True and len(pyt) < 2 and pyt == 'N':
                return False
            else:
                print('Prosimy podać JEDNĄ literę (T lub N) bez znaków specjalnych')


w = Wisielec()

def przygotowanie_gry():
    w.ustawianie_prob_obrazu()
    w.losowanie()
    w.rstrip()
    w.siatkowanie()
    w.generowanie_paskow()
    w.czyszczenie_konsoli()

def loop_gry():
    w.wyswietlanie_menu()
    w.wypisywanie_prob()
    w.wypisywanie_paskow()
    w.wyswietlanie_obrazkow()
    w.wprowadzenie_litery()
    w.sprawdzanie_litery()
    w.czyszczenie_konsoli()

if __name__ == "__main__":
    przygotowanie_gry()
    while True:
        if w.sprawdzanie_hasla() == False:
            loop_gry()
        else:
            if w.pytanie_o_next() == True:
                przygotowanie_gry()
            else:
                break

