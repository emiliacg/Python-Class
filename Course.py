#Esto es un comentario
'''
Esto es un 
comentario de 
varias lineas
'''
print("Emilia")

nombre= "Miguel"
print(nombre)

n= 998.9
print(n)

m= True
print(m)

u= 10.989
j= int(u)
print(u)
print(j)

if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
elif n > 2 and n < 6:
    print("Not Weird")
elif n > 6 and n < 21:
    print("Weird")
elif n > 20:
    print("Not Weird")
else:
    ("Weird")

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
countdown(n-1)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
