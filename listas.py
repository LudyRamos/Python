
lista = [20, 'a', 3.1415, True]
#x = lista[0]
print(lista)

#percorrendo uma lista:
for l in range(4):
   print(lista[l])

#como saber o tamanho
tamanho = len(lista)
print(tamanho)

for l in range(len(lista)):
    print(lista[l])
#o for percorre intervalos. um alista já é um
for valor in lista:
    print(valor)

#print(lista)
#lista[3] = 150
#print(lista)

#aumentar o tamanho da lista(append coloca mais um valor no final)
print(lista)
lista.append('b')
print(lista)
lista.append(10)
print(lista)

#colocar em uma posição expecifica, sem mudar a lista
print(lista)
lista.insert(1, 'bom dia')
print(lista)

#não colocar valor na lista(abaixo na lista1)
lista1 = []
lista2 = [4,6,8]
lista3 = [3,5,7]
lista1.append(lista2)
lista1.append(lista3)
print(lista1)
print(lista1[0][2])
#concatenando listas
lista1 = lista2 + lista3
print(lista1)

#percorrendo lstas dentro de outra lista
numeros = [[2,4,6], [3,5,7]]
for x in numeros:
    print(x)
    for y in x:
        print(y)

#fatiandp listas 
lista = [10,20,30,40,50,60]
#lista_menor = lista[0:3]
#lista_menor = lista[1:7:2]
lista_menor = lista[:: -1]
print(lista_menor)