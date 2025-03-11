def verificar_numero(numero):
    resultados = []
    
    # Verifica se o número é positivo, negativo ou zero
    if numero > 0:
        resultados.append(f"{numero} é positivo.")
    elif numero < 0:
        resultados.append(f"{numero} é negativo.")
    else:
        resultados.append(f"{numero} é zero.")
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        resultados.append(f"{numero} é par.")
    else:
        resultados.append(f"{numero} é ímpar.")
    
    # Verifica se o número é divisível por 3
    if numero % 3 == 0:
        resultados.append(f"{numero} é divisível por 3.")
    else:
        resultados.append(f"{numero} não é divisível por 3.")
    
    # Exibe os resultados
    for resultado in resultados:
        print(resultado)

# Entrada do usuário
try:
    numero = int(input("Digite um número: "))
    verificar_numero(numero)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
