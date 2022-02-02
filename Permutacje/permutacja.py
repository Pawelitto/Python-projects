from selenium import webdriver
from itertools import permutations
import time

cyfry = [0,1,2,3,4,5,6,7,8,9]
lista_z_wyrazami = []
cyfry1 = [0,1,2]


driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")


driver.get("https://www.platynov.com/")


klawa = driver.find_element_by_id("keyboardButton").click()


n1 = driver.find_element_by_xpath("//div[@data-num='1']")

rst = driver.find_element_by_id("keyboardClear")
potw = driver.find_element_by_id("keyboardSubmit")


p = permutations(cyfry, 4)

for i in list(p):
    lista_z_wyrazami.append(i)
    print(i)


ilosc_wyrazow = len(lista_z_wyrazami)
numer_wyrazu = 0
numer_indexu_wyrazu = 0

print("Ilosc hasel: ",ilosc_wyrazow)

for i in range(len(lista_z_wyrazami)):

    print("Wartość ",numer_wyrazu," wyrazu: ",lista_z_wyrazami[numer_wyrazu])
    numer_indexu_wyrazu = 0
    time.sleep(0.2)

    for i in range(4):

        print("Numer indexu wyrazu: ", numer_indexu_wyrazu)
        cyfra = lista_z_wyrazami[numer_wyrazu][numer_indexu_wyrazu]
        tekst = "//div[@data-num='%s']" %cyfra
        driver.find_element_by_xpath(tekst).click()
        print(cyfra)
        numer_indexu_wyrazu += 1
        time.sleep(0.2)

    potw.click()
    numer_wyrazu += 1
    time.sleep(0.2)
    rst.click()
