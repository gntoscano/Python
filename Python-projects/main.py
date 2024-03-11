            # LISTAS
# lista_numeros = [3, 2, 1]
# lista_numeros.append ("Ola")
# print (lista_numeros [0])
# print (lista_numeros [1])
# print (lista_numeros [2])
# print (lista_numeros)


# print("total: ", len(lista_numeros))
# print("Maximo : ", max(lista_numeros))
# print("Minimo : ", min(lista_numeros))
# ==========================================================

            # CONDICIONAIS
# salario = float(input("Digite seu salario: "))

# if salario <= 300:
#     print("Poooobre")
# elif salario > 300 and salario <= 700:
#     print("Pobrinho")
# elif salario > 700 and salario <= 1500:
#     print("Tá na media vai") 
# elif salario > 1500 and salario <= 7000:
#     print("Ta ok")
# else:
#     print("Ta ganhando muito!")
# ============================================================


            #REPETICOES
    
# notas = []

# for x in range(3):
#     codigo_aluno = input("Codigo RM: ")
#     nota = input("Nota do aluno: ")
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

# print("Quantidade de notas: ", len(notas))

# for n in notas:
#     codigo_aluno = n[0]
#     nota = n[1]
#     print("O RM: ", codigo_aluno, "tirou a nota: ", nota )



# notas = []

# contador = 1

# while contador <= 3:
#     codigo_aluno = int(input("Digite o RM: ")) 
#     nota = float(input("Digite nota: ")) 
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

#     contador = contador + 1

# print("Quantidade de notas: ", len(notas))

# for n in notas:
#      codigo_aluno = n[0]
#      nota = n[1]
#      print("O RM: ", codigo_aluno, "tirou a nota: ", nota )

# ===============================================================



            # DICIONARIOS

# player = {
#     "Nome": input("Nome: "),
#     "hp": 3,
#     "exp": 0,
# }

# print(player)

            #LISTA DE DICIONARIOS

# npcs = [
#     {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
#     {"nome": "Monstro", "dano": 5, "hp": 100, "exp": 15},
#     {"nome": "Monstrao", "dano": 10, "hp": 300, "exp": 30},
#     {"nome": "Chefao", "dano": 20, "hp": 1000, "exp": 100},
# ]

# print(npcs)

# ====================================================================



            # CHAT DE MENSAGENS


   
    
   
    

# import os
# mensagens = []
# nome = input("Nome ")

# while True:

#      #limpar terminal
#     os.system('cls')
#     if len(mensagens) > 0:
#         for m in mensagens:
#             print(m['nome'], "-", m['texto'])

#     print("_____________________________")

#     #obtendo texto
#     texto = input("mensagem: ")
#     if texto == "fim":
#         break

#     #adicionar msgs
#     mensagens.append({
#         "nome": nome,
#         "texto": texto
#     })





            # FUNCOES

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Digite o valor 1: "))
    valor2 = int(input("Digite o valor 2: "))


    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+ ", valor2, "= ", resposta)
    sim_nao = input("Deseja continuar? ")

    if sim_nao == "Nao":
        break