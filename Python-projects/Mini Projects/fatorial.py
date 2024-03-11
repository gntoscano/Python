# Cire um programa que receba um numero e imprima o fatorial desse numero
# Método 5Q's para montar um algoritmo

numero = (int(input('Insira um número: ')))
if numero > 0:
    fatorial = 1
    for item in range(1,numero +1):
        fatorial = fatorial * item
    print(fatorial)



    