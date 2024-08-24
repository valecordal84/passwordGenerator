import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['?', '!', '#', '$', '%', '&', '(', ')', '+', '*']


print ("Esto es un generador de contraseña")
letraRandom = int(input("Cuantas letras quiere en su contraseña? \n"))
numeroRandom = int(input("Cuantos numeros quiere en su contraseña? \n"))
simboloRandom = int(input("Cuantos simbolos quiere en su contraseña? \n"))
lista = []
contraseña = ""

for lns in range(0, letraRandom):
    lista.append(random.choice(letras))
    
for lns in range(0, numeroRandom):
    lista.append(random.choice(numeros))
    
for lns in range(0, simboloRandom):
    lista.append(random.choice(simbolos))
    
random.shuffle(lista)

for lns in lista:
    contraseña += lns
    
print(contraseña)