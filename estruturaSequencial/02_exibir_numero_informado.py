"""
Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]".
"""
numero = input("Digite um número:\n")
try: # Uso de try-except para previnir erros
    numero = float(numero)
    print(f"O número informado foi {numero:.2f}")
    
except ValueError:
    print("Erro: Você digitou um número inválido!")