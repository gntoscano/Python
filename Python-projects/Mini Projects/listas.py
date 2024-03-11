# valor_maximo = int(input('Digite o valor maximo: '))
# valor_inicial = 1
# for numero in range(valor_inicial,valor_maximo + 1):
#     print(numero)


# #coleções(listas)
# preco_1 = 20
# preco_2 = 50
# preco_3 = 200


# #listas
# precos = [20, 50, 200]
# print(precos[1])
# print(precos.index(200))
# #ou
# for preco in precos:
#     print(preco)

# #lista
# diversidades = [15, 'Jonathan', True]
# print(diversidades[0])
# print(diversidades[1])
# print(diversidades[2])

# for diversidade in diversidades:
#     print(diversidade)

#Exemplo - Some os valores
# Dados uma coleção de dados 'idades' [15, 46, 75, 34, 23]
# Imprima a soma desses valores
idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total = total + idade
print(total)