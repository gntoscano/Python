def calculadora():
    while True:
        # Solicitar entrada do usuário
        valor1 = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        valor2 = float(input("Digite o segundo número: "))
        

        # Realizar a operação
        if operacao == '+':
            resultado = valor1 + valor2
        elif operacao == '-':
            resultado = valor1 - valor2
        elif operacao == '*':
            resultado = valor1 * valor2
        elif operacao == '/':
            # Lidar com a divisão por zero
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                print("Erro: Divisão por zero!")
                continue  # Reinicia o loop

        # Exibir o resultado
        print(f"Resultado: {resultado}")

        # Perguntar se o usuário deseja continuar
        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            break  # Sai do loop se a resposta não for 's'

# Chamar a função da calculadora
calculadora()