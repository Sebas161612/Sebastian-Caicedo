print('Escribé las 5 notas para saber tu promedio, Recuerda que se debe escribir en numeros y de 0 a 100')

nota_1 = int(input("Ingrese el valor de la nota #1:" ))
nota_2 = int(input("Ingrese el valor de la nota #2:" ))
nota_3 = int(input("Ingrese el valor de la nota #3:" ))
nota_4 = int(input("Ingrese el valor de la nota #4:" ))
nota_5 = int(input("Ingrese el valor de la nota #5:" ))

if (nota_1 < 0 or nota_2 < 0 or nota_3 < 0 or nota_4 < 0 or nota_5 < 0):
    print('No puedes ingresar números negativos')
elif (nota_1 > 100 or nota_2 > 100 or nota_3 > 100 or nota_4 > 100 or nota_5 > 100):
    print('No puedes ingresar notas mayores a 100')

else:
    suma_notas = nota_1 + nota_2 + nota_3 + nota_4 + nota_5
    promedio = suma_notas/5
    if promedio >= 60:
        print('Aprobado')
    elif promedio < 40:
        print('Reprobado')
    else:
        print('En recuperación')
    print(f"Su nota final es de: {promedio}")