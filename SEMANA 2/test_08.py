# Definición de variables (faltantes en el original)
nombre_1 = "Juan"
nombre_2 = "Kevin"
edad1 = 20
edad2 = 25
altura1 = 1.70
altura2 = 1.75
es_estudiante = True
es_estudiante2 = True

if es_estudiante:
    print('Nombre es {}, tengo {} años y mi altura actual es {}'.format(nombre_1, edad1, altura1))

    if es_estudiante2:
        print('Mi nombre es {}, tengo {} años y mi altura actual es {}'.format(nombre_2, edad2, altura2))

        if edad2 > edad1:
            print('{} es mayor que {}'.format(edad2, edad1))

        if edad2 < edad1:
            print('{} es menor que {}'.format(edad1, edad2))