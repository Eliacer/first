tupla = (1, 2, 3, 4)
array = [8, 5, 3, 9, 0]
print(tupla)

lista = list(tupla)
print("CONVIERTE UNA TUPLA EN LISTA")
print(lista)

tupla1 = tuple(lista)
print("CONVIERTE UNA LISTA EN TUPLA")
print(tupla1)

#PUEDE SER DE LA TUPLA O DEL ARRAY
#max: retorno el valor maximo del array
print(max(tupla))

#min: retorno el valor minimo del array
print(min(tupla))

#len: retorno la longitud del array
print("LONGITUD DE UN ARRAY O TUPLA")
print(len(array))

print("UNE DOS ARRAYS")
print(lista+array)
