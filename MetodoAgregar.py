a = [66.25, 333, 334, 1, 1234.5]
b = [3.6, 4.8]
print(a)
print(b)

#insert: Inserta un valor en la ubicacion del array...insert(location,data)
a.insert(2, -1)
print("AGREGA UN VALOR EN UNA UBICACION DETERMINADA")
print(a)

#append: Agrega un nuevo valor al array
a.append(333)
print("NUEVO VALOR EN EL ARRAY")
print(a)

a.extend(b)
print("AGREGA UN ARRAY DENTRO DE OTRO, al final de este")
print(a)