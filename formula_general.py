"""
Fecha de creación: 24/sep/21
Autor: Cristopher Olivares 
"""
import math

print ( 'Calculadora de ecuaciones de segundo grado, de la forma: \n ax^2 + bx + c = 0 \n Cuando "a" es diferente de 0.')
a = int(input('Ingrese valor de a: '))    
b = int(input('Ingrese valor de b: '))
c = int(input('Ingrese valor de c: '))

# Operaciones de la fromula general
formula1 = (- b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
formula2 = (- b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)

# Impresión de resultados
print( 'Resultado de la raíz positiva: ', formula1)
print( 'Resultado de la raíz negativa: ', formula2)

    
