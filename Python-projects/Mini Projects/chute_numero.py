# Ao iniciar gera ym valor aleatorio de 1 a 10 e permite que o usuário
# chute um numero ate que o valor aleatorio gerado no inicio seja chutado corretamente
# Programa deve informar se o chute foi acima ou abaixo do valor inicial

import random

valor_aleatorio = random.randint(1,100)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 100: '))
    if chute > valor_aleatorio:
        print('O valor foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('O valor foi menor que o gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print ('Você acertou!!')
