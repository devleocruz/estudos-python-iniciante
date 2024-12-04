"""
 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
 """
try:
    numero_1 = float(input("Digite a nota do primeiro bimestre:\n"))
    numero_2 = float(input("Digite a nota do segundo bimestre:\n"))
    numero_3 = float(input("Digite a nota do terceiro bimestre:\n"))
    numero_4 = float(input("Digite a nota do quarto bimestre:\n"))

    media = (numero_1 + numero_2 + numero_3 + numero_4) / 4
    print(f"A média é: {media:.2f}")

except ValueError:
    print("Erro: Você digitou um número inválido!")