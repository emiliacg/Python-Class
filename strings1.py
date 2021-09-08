hola= "Hola World"
print(hola)
print(hola[2])
# rada

print(hola[7]+hola[3]+hola[9]+hola[3])
print(hola[-1])
print(hola[-2])
print(hola[-3]+hola[-7]+hola[-1]+hola[-7])

for Emilia in range(len(hola)):
    print(Emilia,hola[Emilia])

for Miguel in reversed(range(len(hola))):
    print(hola[Miguel],Miguel)

for letra in hola:
    print(letra)

for letra in reversed(hola):
    print(letra)


lista= []
print(lista)

lista.append(1)
print(lista)

lista.append(5)
lista.append(3)
print(lista)

print(lista[-1])
print(lista.sort())
print(lista)

lista.append(2)
print(lista)
print(sorted(lista))
print(lista)

# lista.clear() 
# print(lista)


print(lista.pop())
print(lista)
print(lista.pop())
print(lista.pop())
print(lista.pop())
lista.append(0)
if len(lista) >0:
    print(lista.pop())


e= "12345"
print(e[-1:-2:-1])