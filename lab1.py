#1. Napisz program obliczający sumę dwóch liczb podanych z klawiatury.
#2. Napisz program rozwiązujący równanie liniowe:
#ax + b = 0 (1)
#Uwzględnić wszystkie możliwe warunki.
#3. Napisz program obliczający pole prostokąta:
#Pp = a ∗ b (2)
#4. Napisz program obliczający objętość kuli:
#Vk =
#4
#3
#πR3
#(3)
#5. Oblicz wartość funkcji f(x, y) = x
#2 − xy + 4 dla argumentów x = 8 oraz y = 9.
#6. Napisz program obliczający silnię:
#n! = ∏n
#k=1
#k, dla n ≥ 1 (4)
#7. Dla liczb z zakresu [2, 15] wypisz liczby podzielne bez reszty przez 4 oraz dla liczb z zakresu
#[5, 19] wypisz liczby podzielne bez reszty przez 5.
#8. Dla zadanej podstawy narysuj trójkąt prostokątny równoramienny poprzez wyświetlanie symbolu ∗. Przykład dla podstawy 4:
#∗
#∗ ∗
#∗ ∗ ∗
#∗ ∗ ∗ ∗
#12
#9. Napisz program obliczający sumę kolejnych elementów dwóch list.
#10. Napisz program, który wypisze iloczyn kartezjański dwóch list.
#11. Napisz program, który utworzy listę składającą się z unikalnych wartości podanej listy.
#12. Napisz program znajdujący indeks najmniejszej wartości w liście.
#13. Napisz program obliczający sumę szeregu n-elementowego:
#a0 + a1x + a2x
#2 + a3x
#3 + · · · + anx
#n
#Podpowiedź: Utwórz n-elementową listę wartości a, a następnie w pętli obliczaj sumę
#danych iloczynów.
#14. Napisz program wyszukujący największy element z listy.
#15. Napisz program, który zamieni wartości z listy według wzoru:
#{
#a < 0, −1
#a > 0, 1
#16. Napisz program, który utworzy listę złożoną z kolejnych wartości potęg od 0 do p zadanej
#liczby naturalnej n.
#17. Napisz program, który stworzy listę posiadającą wartości ciągu Fibonacciego dla zadanego
#rozmiaru n. Rozwiązanie rekurencyjn jest oceniane w 0 punktów.
#Fn
#
#
#
#0, if n = 0
#1, if n = 1
#Fn−1 + Fn−2, if n > 1
#18. Napisz program, który dla zadanej listy a i wartości p jej lewą połowę listy a wypełni wartością
#−p, ap prawą połowę wypełni wartością p.
#19. Stworzyć listę składającą się z elementów losowych i obliczyć częstotliwość wystąpienia
#poszczególnych elmentów. Przykładowo dla listy [1, 2, 1, 1, 3, 2, 3] w wyniku ma
#powstać słownik: {1: 3, 2: 2, 3: 2}
#20. Napisać prosty kalkulator. Za pomocą funkcji input() pobieramy od użytkownika dwie liczby
#oraz działanie które trzeba wykonać. Użyć instrukcje if - elif - else do wyboru operacji
#matematycznej. Wynik wyświetlić w formacie 2 + 4 = 6 (użyć formatowanie stringów). Do
#obsługi dzielenia przez zero zaleca się uzycie instrukcji try - except.


#Zadanie dodatkowe
#Zadnie dodatkowe bezwarunkowo dodaje +1 do oceny (o ile wykonany program działa poprawnie).
#Zadanie polega na opracowaniu małej gierki która będzie polegać na tym że gracz musi zgadnąć liczbę wylosowaną przez komputer. Zakres losowanych liczb to 0 do 1000. Przykładowe działania programu (>>> oznazca input uzytkownika):

#zad1


a=int(input("Podaj liczbe a : "))
b=int(input("Podaj liczbe b : "))
print("Suma:", a+b)

#zad2

a = int(input("Podaj a = "))
b = int(input("Podaj b = "))
if a == 0:
    if b == 0:
        print("Równanie tożsamościowe")
    else:
        print("Równanie sprzeczne")
else:
    x = -b/a
    print("x =", x)
	
#zad3

a = int(input("Podaj pierwszy bok prostokąta: "))
b = int(input("Podaj drugi bok prostokąta: "))
print("Pole prosokąta wynosi: ", a*b)

#zad4

import math

promien = int(input("Podaj promień: "))
print("Objętość koła wynosi: ",4/3*math.pi*promien**3)

#zad5

x = 8
y = 9
print("Wartość funkcji f(x,y) =",x**2-x*y+4)

#zad6

n = int(input("Podaj liczbe n silni: "))
silnia = 1
for i in range(1,n+1):
    if i==n:

        print("Silnia wynosi: ", int(silnia) * int(i))
    else:
        silnia = int(silnia) * int(i)

#zad7

print("liczby podzielne przez 4 to: ")
for i in range(2,16):
    if i%4==0:
        print(i)
print("liczby podzielne przez 5 to: ")
for i in range(5,20):
    if i%5==0:
        print(i)
		
#zad8

a = int(input("Podaj podstawe trójkąta prostokątnego równoramiennego: "))
for i in range(1,a+1):
    for x in range(1,i+1):
        if i==x:
            print("*")
        else:
            print("*", end=" ")
			
#zad9

a = []
b = []
suma = 0
x = int(input("Podaj długość dwóch list: "))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    a.insert(i,int(input(" liczbe pierwszej listy: ")))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    b.insert(i,int(input(" liczbe drugiej listy: ")))
for i in range(x):
    suma = suma + a[i] + b[i]
    if i == x-1:
        print(suma)
   
 #zad10
 
 iloczyn = []
a = []
b = []
x = int(input("Podaj długość dwóch list: "))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    a.insert(i,input(" liczbe pierwszej listy: "))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    b.insert(i,input(" liczbe pierwszej listy: "))
for i in range(0,x):
    for k in range(0,x):
        iloczyn.insert(i,[a[i],b[k]])
        print(iloczyn[i], end="")
    
#zad11

a = []
x = int(input("Podaj długość listy: "))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    a.insert(i,input(" liczbe listy: "))

print(a[:])

#zad12

a = []
najmniejsza_liczba = 0
index_najmniejszej_liczby = 0
x = int(input("Podaj długość listy: "))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    a.insert(i,input(" liczbe listy: "))
for i in range(x):
    if i==0:
        najmniejsza_liczba = a[i]
        index_najmniejszej_liczby = i
    else:
        if najmniejsza_liczba>a[i]:
            najmniejsza_liczba = a[i]
            index_najmniejszej_liczby = i
print("Index najmniejszej wartości w liście wynosi :", index_najmniejszej_liczby)

#zad13

lista = []
suma = 0
a = int(input("Podaj wartość a = "))
n = int(input("Podaj wartość n = "))
x = int(input("Podaj wartość x = "))
for i in range(n):
    if i==0:
        lista.insert(i,a)
    else:
        lista.insert(i,a*x**i)
for i in range(n):
    suma = suma + lista[i]
print("Suma szeregu n-elementowego wynosi ", suma)

#zad14

a = []
najmniejsza_liczba = 0
index_najmniejszej_liczby = 0
x = int(input("Podaj długość listy: "))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    a.insert(i,input(" liczbe listy: "))
for i in range(x):
    if i==0:
        najmniejsza_liczba = a[i]
        index_najmniejszej_liczby = i
    else:
        if najmniejsza_liczba>a[i]:
            najmniejsza_liczba = a[i]
            index_najmniejszej_liczby = i
print("Index najmniejszej wartości w liście wynosi :", index_najmniejszej_liczby)

#zad15

a = []
x = int(input("Podaj długość listy: "))
for i in range(x):
    l = i
    print("Podaj ", l+1, end='')
    a.insert(i,int(input(" liczbe listy: ")))
print(a[:])
for i in range(x):
    if a[i] < 0:
        a[i] = -1;
    elif a[i] > 0:
        a[i] = 1
print(a[:])

#zad16

n = int(input("Podaj n = "))
p = int(input("Podaj p = "))
lista = []
for i in range(p+1):
    lista.insert(i,n**i)
print("\tTwoja lista")
print(lista[:])
    
#zad17

n = int(input("Wprowadź n: "))
ciag = [1,1]

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n):
        ciag.insert(i,ciag[i-1]+ciag[i-2])
print(ciag[:])

#zad18

lista = []
a = int(input("Podaj długość listy : "))
if a%2!=0:
    while a%2!=0:
        a = int(input("Podaj długość listy (liczba parzysta): "))
polowa = (a/2)-1
for i in range(a):
    l = i
    print("Podaj ", l+1, end='')
    lista.insert(i,int(input(" liczbe listy: ")))
print("\tTWOJA LISTA")
print(lista[:])
for i in range(a):
    if i<=polowa and lista[i] > 0:
        lista[i] *= (-1)
    elif i>polowa and lista[i] < 0:
        lista[i] *= (-1)
print("\n\tTWOJA LISTA PO DZIAŁANIACH")
print(lista[:])

#zad19

import random

lista = []
lista = []
slownik = {}
x = int(input("Podaj długośc listy :"))
for i in range(x+1):    
    lista.insert(i,random.randrange(1,x))
for i in range(x+1):
    slownik[i] = 0
for i in range(x+1):
    slownik[lista[i]] += 1;
for klucz, wartosc in slownik.items():
    if klucz!=0:
        print(klucz, wartosc)
		
#zad20

print("Witam w kalkulatorze")
print("Wybierz operacje matematyczna")
print("1-Dodawanie")
print("2-Odejmowanie")
print("3-Mnożenie")
print("4-Dzielenie")
wybor = int(input("Twój wybór to:"))
while wybor<0 or wybor>4:
    print("Niepoprawna liczba")
    print("1-Dodawanie")
    print("2-Odejmowanie")
    print("3-Mnożenie")
    print("4-Dzielenie")
    wybor = int(input("Twój wybór to:"))
if wybor==1:
    a = int(input("Podaj pierwszą liczbę : "))
    b = int(input("Podaj drugą liczbę : "))
    print(a," + ", end="")
    print(b," = ", end="")
    print(a+b)
elif wybor==2:
    a = int(input("Podaj pierwszą liczbę : "))
    b = int(input("Podaj drugą liczbę : "))
    print(a," - ", end="")
    print(b," = ", end="")
    print(a-b)
elif wybor==3:
    a = int(input("Podaj pierwszą liczbę : "))
    b = int(input("Podaj drugą liczbę : "))
    print(a," * ", end="")
    print(b," = ", end="")
    print(a*b)
elif wybor==4:
    a = int(input("Podaj pierwszą liczbę : "))
    b = int(input("Podaj drugą liczbę : "))
    try:
        dzielenie = a/b
        print(a," : ", end="")
        print(b," = ", end="")
        print(dzielenie)
    except ZeroDivisionError as e:
        print('Wystąpił błąd:',e)

#zad dodatkowe

import random

szukana = random.randrange(1000)
print("Zgadnij liczbe od 0 do 1000")
twoj_wybor = int(input(">>>"))
while twoj_wybor!=szukana:
    if twoj_wybor>szukana:
        print("Liczba jest za duza, probuj jeszcze:")
    elif twoj_wybor<szukana:
        print("Liczba jest za mala, probuj jeszcze")
    twoj_wybor = int(input(">>>"))
print("Zgadłeś!")