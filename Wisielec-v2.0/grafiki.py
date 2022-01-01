
def wys_obraz(numer):

    wisielec_obrazki = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    return wisielec_obrazki[numer]

def rodzaje_menu_w_grze(numer_obraku):

    obrazy = ["""
========================================
        Wisielec v2.0 BY Pietras
========================================
""","""
========================================
        Wisielec v2.0 BY Pietras
========================================
            Wybierz opcję:
        
        P - Graj
        K - Konfiguracja gry
        I - Inforamcje o grze
        Q - Wyjście 

========================================
""","""
========================================
        Wisielec v2.0 BY Pietras
========================================

         ---Konfiguracja gry---

    1. Wszystkie zmiany mależy wykonać
       w plikach '.txt', po zmianie
       należy zapisać plik oraz
       uruchomić program ponownie.
    
    2. Ilość prób można zmienić w pliku
       'konfig.txt'.
    
    3. Hasła oraz kategorie są zachowane
       w 'wyrazy.txt'.

    4. Aby wprowadzić dane hasło należy
       uprzednio dodać kategorie w tym
       celu należy otworzyć plik
       z punktu powyrzeć...
       następnie dopisać kategorię
       ze znakiem ':' zaś hasło
       należy zakończyć ','
       wszystkie hasła i kategorie muszą
       znajdować się w osobnej linii.
    
    5. Zaleca się aby do poprawnego
       działania gry, wszystkie pliki  
       muszą być w tym samym folderze.
       
    6. W pierwszej kolejności trzeba
       uruchomić plik o nazwie:
       'main.py'.
    
    7. Życzę przyjemej rozgrywki!
       
    Wprowadź 'Q' aby wrócić do menu       
    
========================================
""","""
========================================
        Wisielec v2.0 BY Pietras
========================================

         ---Informacje o grze---

    1. Jeżeli w rozgrywce występują
       Jakiekolwiek błędy należy o tym
       napisać na wskazany adres e-mail
       'pawel.pietras144@gmail.com' .

    2. Jeśli są jakiekolwiek problemy
       z konfiguracją haseł, kategorii
       itp. można napisać do supportu
       e-mail 'pawel.pietras144@gmail.com'.

    3. Hasła oraz kategorie są w języku
       Angielskim.
    
    4. Została utworzona 06.11.2021
       Wydana -----
       
    Wprowadź 'Q' aby wrócić do menu       

========================================
""","""
========================================
        ---Dziękujemy za grę---
========================================
"""]

    return print(obrazy[numer_obraku])
