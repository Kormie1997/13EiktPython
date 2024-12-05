import random
lista = []
def veletlen():
    hossz = 20
    for i in range(hossz):
        lista.append(random.randint(1, 50))
    return lista

def kiieVeletlen():
    for i in range(20):
        print(veletlen()[i])

def kiir():
    for i in lista:
        print(i, end=" ")

def osszeadd():
    sum = 0
    for i in lista:
        sum = sum + i
    return sum

def legnagyobbElem():
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

veletlen()
kiir()
print(f"A lista elemeinek a osszege: {osszeadd()}")
kiieVeletlen()
print(f"A lista elemeinek a legnagyobb erteke: {legnagyobbElem()}")
