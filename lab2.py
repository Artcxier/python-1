




#1. Napisz funkcje, która oblicza pole prostokąta. Argumentami funkcji są boki a i b prostokąta, funkcja zwraca (nie printuje!) jedną wartość która jest polem zadanego prostokąta.

def pole(a, b):
    return a*b

#2.Napisz funkcje, która sprawdzi czy przekazana jako argument liczba n jest liczbą pierwszą. Funkcja zwraca True, jeżeli n jest liczbą pierwszą i False w przypadku przeciwnym.

def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    prime = int(n**0.5) + 1
    for i in range(3, prime, 2):
        if n % i == 0:
            return False
    return True


#3.. Napisać funkcje, która przyjmuje jako argumenty trzy liczby n, a, b i zwraca listę o długości n zawierającą całkowite liczby losowe z przedziału [a, b). Argumenty a i b muszą posiadać wartości defaultowe a = 0 oraz b = 10. Do wygenerowania listy należy użyć funkcji randrange z modułu random oraz konstrukcje [ ... for... in ...].

import random

def rand_list(n, a = 0, b = 10):
    random_list = []
    for i in range(n):
        random_list.append(random.randrange(a,b))
    return random_list

#4.Napisać program który wygeneruje listę składającą się z 10 całkowitych liczb losowych oraz zliczy częstotliwość wystąpienia poszczególnych elementów. Do wygenerowania listy można użyć funkcje z poprzedniego zadania. Do zliczenia elementów należy użyć obiekt Counter z modułu collections.


import random

from collections import Counter

def rand_list(n = 10, a = 0, b = 10):

random_list =[random.randrange(a, b) for i in range(n)]

print(random_list)

return(random_list)

print(Counter(rand_list()))


#5. Napisać program, który wygeneruje listę składającą się z 10 losowych liczb całkowitych z przedziału [−100, 100)
#oraz znajdzie i wypisze największą i najmniejszą liczbę bez uwzględnienia znaku liczby (wartość bezwzględna).
#Do wykonania zadania należy użyć wbudowanych funkcji min i max z przekazaniem argumentu key.

import random;
def rand_list(n, a = 0, b = 10):
    random_list = []
    for i in range(n):
        random_list.append(random.randrange(a,b))
    return random_list

def sort(list):
    return sorted(list, key=abs, reverse=True)

quest_list = rand_list(10, -100, 100)
quest_list = sort(quest_list)

print(quest_list)

#6Napisz funkcje, która przyjmuje listę jako argument i zwraca sumę dodatnich elementów tej listy. Funkcje
#należy zaimplementować z użyciem wbudowanej funkcji sum i konstrukcji (... for ... in ... if ...).

def sumujDodatnie(lista):

   return sum(i for i in lista if i > 0)

lista = [1, 5, -3, 6, 1, -7, 12, -5, 5, -11, 2, 4, -11, 5, 1, -4, -1000, 2]

print(sumujDodatnie(lista))

#7. Napisz program który wypisze wszystkie liczby pierwsze, które można złożyć z cyfr 1, 4, 7, 8. Przykładowo z
#liczb 2, 3, 5 można złożyć tylko jedną liczbę pierwszą: 523. Do wykonania tego zadania należy użyć funkcje
#permutations z modułu itertools

import itertools

def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    prime = int(n**0.5) + 1
    for i in range(3, prime, 2):
        if n % i == 0:
            return False
    return True

def liczby_do_permutacji(lista):
    gimme = list(itertools.permutations(lista))
    pierwsze_po_permutacji = []
    for i in gimme:
        number_from_list = ""
        for x in i:
            number_from_list = number_from_list + "" + str(x)
        number_from_list = int(number_from_list)
        if(czy_pierwsza(number_from_list)):
            pierwsze_po_permutacji.append(number_from_list)
    return pierwsze_po_permutacji

print(liczby_do_permutacji([1,4,7,8]))

#8 Napisz program który wypisze wygeneruje listę składającą się z 20 losowych liczb całkowitych z przedziału
#[0, 100), a zatem za pomocą konstrukcji [... for ... in ... if ...] przefiltruje wygenerowaną listę
#zostawiając tylko liczby należące do ciągu an = 3n + 1, gdzie n ∈ Z. Podpowiedź: można zaimplementować
#funkcje sprawdzającą czy liczba spełnia warunek i użyć tą funkcje w środku generatora.

import random

def CzyWyrazCiagu(liczba):
	if(liczba -1)%3 ==0:
		return True
	else:
		return False
		
	def GenerujListe(n, Lista_liczb, poczatek, koniec):
		random.seed(23122022)//losowa liczba
		for j in range(0,n):
			Lista_liczb.append(random.randint(poczatek, koniec))
			
	def PrzefiltrujListe(n, Lista_liczb):
		Lista_pomocnicza = list()
			for j in range(0,n):
				Lista_pomocnicza.append(lista_liczb.pop())
			Lista_pomocnicza.reverse()
				for element in Lista_pomocnicza:
					if CzyWyrazCiagu(element):
						Lista_liczb.append(element)
						
	def WygenerujListe(n, Lista_liczb, poczatek, koniec):
		random.seed((23122022)
			for j in range(0,n):
				While True:
					k = random.randint(poczatek, koniec)
						if CzyWyrazCiagu(k):
							Lista_liczb.append(k)
							break
							
	n = 20
	Lista_liczb = list()
	poczatek = 0
	koniec = 99
	GenerujListe(n, Lista_liczb, poczatek, koniec)
	print(Lista_liczb)
	PrzefiltrujListe(n, Lista_liczb)
	print(Lista_liczb)
	
	Lista_liczb = list()
	WygenerujListe(n, Lista_liczb, poczatek, koniec)
	print(Lista_liczb)
	
#9 Napisz funkcje która posortuje po numerach albumów listę rekordów o strukturze (”Imie”, ”Nazwisko”, numer_albumu). 
# Do wykonania zadania należy użyć wbudowanej funkcji sorted z użyciem argumentu key.

def sortuj(lista_studentow):
    return sorted(lista_studentow, key=lambda lista_studentow: lista_studentow[2])

studenci = [
    ("Jan", "Kowalski", 3512),
    ("Jan", "Kowalski", 1243),
    ("Jan", "Kowalski", 2536),
    ]

print(sortuj(studenci))	

#10 Napisz funkcje rekurencyjną, która przyjmuje jako argumenty posortowaną listę oraz liczbę. Funkcja zwraca
#True, jeżeli podana liczba zawiera się w liście i False w przeciwnym przypadku. Dla sprawdzenia czy liczba zawiera się w liście funkcja ma używać wyszukiwanie binarne

def bin_search(arr:list,low:int,high:int,k:int)->bool:

   if low <= high:  

       mid = (high + low) // 2

       if (mid == k):

           return True

       elif arr[mid] < k:

           return(bin_search(arr,mid+1,high,k))  

       else:

           return(bin_search(arr,low,mid-1,k))  

   else:

       return False


def find_number(arr:list,k:int)->bool:

   return(bin_search(arr,0,len(arr)-1,k))
   
#11 Używając obiektów z modułu datetime obliczyć liczbę dni do swoich najbliższych urodzin, oraz swój wiek w minutach.


 from datetime import datetime

urodzony = datetime(2001, 10, 19)

def wiek_w_minutach(urodzony : datetime):
    now = datetime.now()
    wiek = now.year - urodzony.year
    miesiac = now.month
    dzien = now.day
    godzina = now.hour
    minuta = now.minute
    return (((wiek * 12 + miesiac) * 30 + dzien) * 24 + godzina) * 60 + minuta
    
def dni_do_urodzin(urodzony : datetime):
    now = datetime.now()
    delta1 = datetime(now.year, urodzony.month, urodzony.day)
    delta2 = datetime(now.year+1, urodzony.month, urodzony.day)
    
    return ((delta1 if delta1 > now else delta2) - now).days

print("Å¼yjesz minut : " + str(wiek_w_minutach(urodzony)))
print("dni do urodzin : " + str(dni_do_urodzin(urodzony)))  
   
#12 Napisz dwie funkcje obliczające silnie (wersja iteracyjna i rekurencyjna). Za pomocą funkcji time z
#modułu time porównaj czas działania obu funkcji przy obliczeniu silni z liczb z zakresu [20, 50) (sprawdź kilka
#liczb, tak żeby była widoczna różnica w czasach wykonania).


def recursive_factorial(n):

   if n < 2:

       return n

   else:

       return n*recursive_factorial(n-1)


def iterative_factorial(n):

   data = []

   data.append(1)

   for i in range(2,n+1):

       data.append(i*data[-1])

   return data[-1]


from timeit import default_timer as timer

n=20

start = timer()

iterative_factorial(n)  

print("iterative" , timer()-start)

start = timer()

recursive_factorial(n)

print("recursive" , timer()-start)

n=34

start = timer()

iterative_factorial(n)  

print("iterative" , timer()-start)

start = timer()

recursive_factorial(n)

print("recursive" , timer()-start)

n=50

start = timer()

iterative_factorial(n)  

print("iterative" , timer()-start)

start = timer()

recursive_factorial(n)

print("recursive" , timer()-start)

n=40

start = timer()

iterative_factorial(n)  

print("iterative" , timer()-start)

start = timer()

recursive_factorial(n)

print("recursive" , timer()-start)



#13 Napisz program, który wypisze jakie liczby z ciągu Fibonacciego do 10000 są jednocześnie liczbami pierwszymi.
#Do sprawdzenia czy liczba jest pierwszą


def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    prime = int(n**0.5) + 1
    for i in range(3, prime, 2):
        if n % i == 0:
            return False
    return True

lista_fib = [1, 1]
def fib(n):
    new = lista_fib[-1] + lista_fib[-2]
    if(new < n):
        if(czy_pierwsza(new)):
            print(new)
        lista_fib.append(new)
        fib(n)

fib(1000)


