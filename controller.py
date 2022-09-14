from functions import functions
from time import time

lista = functions.readList("numbers.txt")
obj = functions.readTarget("numbers.txt")
result = []

print("-----------------Lista Inicial------------------------")
print(lista)
print("Target: "+obj)

print("--------funcion de comparacion izq -> der: ------")
resultado = functions.Compare(lista, obj, result)
print(resultado)

lista = functions.readList("numbers.txt")
obj = functions.readTarget("numbers.txt")

print("-------- funcion de comparacion dos sentidos: ------")
result2, iteraciones = functions.twoCompare(lista, obj)
print(result2)
print("Iteraciones: "+ str(iteraciones))

print("-------- funcion de comparacion busqueda binaria con Merge sort: ------")
result3=functions.searchAdd(obj, lista)
print(result3)



