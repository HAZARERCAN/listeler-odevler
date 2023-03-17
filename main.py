"""
# SORU: Kullanicidan 10 adet sayı alıp listeye atın
# ve sonrasında listenin aritmetik ortalamasını bulun.
sayi_listesi: list = list()
for i in range(1, 11):
    sayi = int(input(f"{i}. sayı: "))
    sayi_listesi.append(sayi)

print(sum(sayi_listesi) / len(sayi_listesi))
sayi_listesi_2: list = list()

for i in range(1, 11):
    sayi = int(input(f"{i}. sayı: "))
    sayi_listesi_2.append(sayi)

liste_toplami = 0

for sayi in sayi_listesi_2:
    liste_toplami += sayi

print(liste_toplami / len(sayi_listesi_2))
"""







"""
# 1. 1-100 arasında 20 adet rastgele sayı üretin ve
# aynı numara içerde olmadan listeye atın.
from random import randint
sayilar: list = list()
while len(sayilar) <= 20:
    sayi: int = randint(1, 101)
    if sayi not in sayilar:
        sayilar.append(sayi)
print(sayilar)
"""

"""
sayilar: list = list()
for i in range(1, 30):
    if len(sayilar) <= 20:
        sayi: int = randint(1, 101)
        if sayi not in sayilar:
            sayilar.append(sayi)
        else:
            continue
    else:
        break
print(sayilar)
tek_liste: list = list()
cift_liste: list = list()
for sayi in sayilar:
    if sayi % 2 == 0:
        cift_liste.append(sayi)
    else:
        tek_liste.append(sayi)
print(f"Tek Liste: {tek_liste}")
print(f"Çift Liste: {cift_liste}")
"""





"""
# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# : Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.
kelimeler: list = list()
sayac: int = 1
while sayac < 7:
    kelime = input("Bir kelime girin")
    if sayac < 6:
        if kelime not in kelimeler:
            kelimeler.append(kelime)
            sayac += 1
        else:
            print(f"Girmiş olduğunuz {kelime} kelimeler listesinde mevcut")
    else:
        if kelime in kelimeler:
            print(f"{kelime}  kelimesi kelimeler listesinde mevcut")
            break
        else:
            print(f"{kelime}  kelimesi kelimeler listesinde mevcut değil")
            break
"""




