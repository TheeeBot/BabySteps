lista = []
lista1 = []
while True:
    try:
        lista.append(input())
    except EOFError:
        break
for i in lista:
        i = i.lower()
        lista1.append(i)
        lista1.sort()
for i in lista:
    if lista1[-1] == i.lower():
        print (i)
        break
