def mi_funcion():
    print("Hola Mundo")

datos = mi_funcion()


#FUNCIONES CON PARAMETROS DE OMISION
def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)

saludar('Eliacer Fernandez')
saludar(mensaje="Buen día", nombre="Juancho")

#PARAMETROS ARBITRARIOS
print("")
def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print(parametro_fijo)

    # Los parámetros arbitrarios se corren como tuplas
    for argumento in arbitrarios:
        print(argumento)

recorrer_parametros_arbitrarios('Fixed', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3')

print("")
def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print(parametro_fijo)
    for argumento in arbitrarios:
        print(argumento)

        # Los argumentos arbitrarios tipo clave, se recorren como los diccionarios
    for clave in kwords:
        print("El valor de", clave, "es", kwords[clave])


recorrer_parametros_arbitrarios("Fixed", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno",clave2="valor dos")