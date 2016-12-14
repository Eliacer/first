def calcular(importe, descuento):
    return importe - (importe * descuento / 100)


print("")
datos = [1500, 10]
print(calcular(*datos))

print("")
datos = {"descuento": 10, "importe": 1000}
print(calcular(**datos))


