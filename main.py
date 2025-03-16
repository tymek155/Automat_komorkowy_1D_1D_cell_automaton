import csv
import random

iter = 0
def zapisz_do_csv(stany):
    global iter
    with open('Zapis' + str(iter)+ '.csv', 'w', newline='') as plik:
        write =csv.writer(plik)
        write.writerow(['Iteracja', 'Stan automatu'])
        for i,stan in enumerate(stany):
            write.writerow([i, stan])
    iter+=1


def decimal_to_binary_with_padding(n, bits=8):
    return format(n, f'0{bits}b')

def slownik_reguly(binarna):
    slownik = {}
    for i in range(8):
        klucz = format(i, '03b')
        slownik[klucz]= binarna[7-i]
    return slownik

def generate_p(slownik, automat):
    wynik = ""
    for i in range(len(automat)):
        if i == 0:
            klucz = automat[-1]+automat[i]+automat[i+1]
        elif i == len(automat)-1:
            klucz = automat[i-1]+automat[i]+automat[0]
        else:
            klucz = automat[i-1]+automat[i]+automat[i+1]
        wynik += slownik[klucz]
    return wynik

def generate_a(slownik, automat):
    wynik = "0"
    for i in range(1, len(automat)-1):
        klucz = automat[i-1]+automat[i]+automat[i+1]
        wynik += slownik[klucz]

    return (wynik + "0")


def automat_periodyczny(liczba_pocz, ilosc_iteracji, liczba_komorek):
    automat = ''.join(random.choice('01') for _ in range(liczba_komorek))
    liczba_bin = decimal_to_binary_with_padding(liczba_pocz)
    slownik = slownik_reguly(liczba_bin)
    print(automat)

    do_zapisu = [automat]
    for i in range(ilosc_iteracji):
        automat = generate_p(slownik, automat)
        do_zapisu.append(automat)
        print(automat)

    zapisz_do_csv(do_zapisu)
    return automat

def automat_absorpcyjny(liczba_pocz, ilosc_iteracji, liczba_komorek):
    automat = ''.join(random.choice('01') for _ in range(liczba_komorek))
    liczba_bin = decimal_to_binary_with_padding(liczba_pocz)
    slownik = slownik_reguly(liczba_bin)
    print(automat)

    do_zapisu = [automat]
    for i in range(ilosc_iteracji):
        automat = generate_a(slownik, automat)
        do_zapisu.append(automat)
        print(automat)

    zapisz_do_csv(do_zapisu)
    return automat

def main():
    opt = 0
    while opt != -1:
        print("1. Uruchom automat z warunkiem periodycznym.")
        print("2. Uruchom automat z warunkiem absorpcyjnym.")
        print("-1. Wyjście.")
        opt = int(input())

        if opt == 1 or opt == 2:
            liczba_komorek = 0
            liczba_iter = 0
            liczba_pocz = 0
            while(liczba_komorek<=0):
                try:
                    liczba_komorek = int(input("Podaj liczbę komórek automatu: "))
                    if liczba_komorek <= 0:
                        print("Nieprawdilowa liczba komorek!")
                except ValueError:
                    print("Podaj liczbe komorek jeszcze raz!")

            while liczba_iter <= 0:
                try:
                    liczba_iter = int(input("Podaj liczbę iteracji automatu: "))
                    if liczba_iter <= 0:
                        print("Nieprawdilowa liczba iteracji!")
                except ValueError:
                    print("Podaj liczbe iteracji jeszcze raz!")

            while liczba_pocz <= 0:
                try:
                    liczba_pocz = int(input("Podaj liczbę reguly: "))
                    if liczba_pocz <= 0:
                        print("Nieprawdilowa liczba reguly!")
                except ValueError:
                    print("Podaj liczbe reguly jeszcze raz!")

        if opt == 1:
            automat_periodyczny(liczba_pocz, liczba_iter, liczba_komorek)
        elif opt == 2:
            automat_absorpcyjny(liczba_pocz, liczba_iter, liczba_komorek)



main()