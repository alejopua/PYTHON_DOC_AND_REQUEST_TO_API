#4
# ¿ES UN NÚMERO PRIMO?

#  Escribe un programa que se encargue de comprobar si un número es o no primo.
#  Hecho esto, imprime los números primos entre 1 y 100.

# nPrimo < 2 and nPrimo != 3 or nPrimo != 2 and nPrimo % nPrimo != 0 and nPrimo % 1 != 0 and nPrimo % 3 == 0 or nPrimo % 2 == int(0)

def isPrime():

  for i in range(14):
    if i == 2  or i == 3:
      print(f" {i}: Es primo")
    elif i < 2 or i % 3 == 0 or i % 2 == 0:
      print("No es primo")
    elif (i % i == 0 and i % 1 == 0) :
      print(f" {i}: Es primo")

isPrime()