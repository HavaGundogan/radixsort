import timeit
from functools import reduce

#diğerlisteleriçin 10lukliste.txt yerine 100lukliste.txt ve 100000likliste.txt yazınız
onlukliste = open("100lukliste.txt","r",encoding="utf-8") #txtden okuma
liste = []

for i in onlukliste:
    liste.append(int(float(i)*10000))
# en büyük öğedeki basamak sayısını al
def flatten(dizi):
    return reduce(lambda x, y: x + y, dizi)
    
def num_digits(dizi):
    maxDigit = 0
    for num in dizi:
        maxDigit = max(maxDigit, num)
    return len(str(maxDigit))

basla = timeit.default_timer()
def radixSort(dizi):
    digits = num_digits(dizi) # digits = n , o(1) 1 defa çalışacak
    for digit in range(0, digits): # o(n) / n defa çalışacak
        temp = [[] for i in range(10)] # / 10n defa çalışacak.counting sort
        for item in dizi:  # dizi = m de defa çalışacak
            num = (item // (10 ** digit)) % 10
            temp[num].append(item)
        dizi = flatten(temp)
    return dizi
bitir = timeit.default_timer()

#   nm + n.10 + n + 1 = o(nm)

array = liste
array = radixSort(array)

sonliste = []

for i in array:
    if i % 10000==0:
        tempnum = int(i / 10000)
        sonliste.append(tempnum)
    else:
        tempnum = i/10000
        sonliste.append(tempnum)


for i in sonliste:
    print(i)

print('Time: ', bitir - basla, "s")