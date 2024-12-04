"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo;
a soma do triplo do primeiro com o terceiro;
o terceiro elevado ao cubo.
"""
try:
    numero_inteiro_1 = int(input("Digite o primeiro número inteiro:\n"))
    numero_inteiro_2 = int(input("Digite o segundo número inteiro:\n"))
    numero_real = float(input("Digite um número real:\n"))

    produto = (numero_inteiro_1 * 2) * (numero_inteiro_2 / 2)
    soma_do_triplo = (numero_inteiro_1 * 3) + numero_real
    cubo_do_terceiro = numero_real ** 3

    print(f"O produto do dobro do primeiro com metade do segundo é: {produto:.2f}")
    print(f"A soma do triplo do primeiro com o terceiro é: {soma_do_triplo:.2f}")
    print(f"O terceiro número elevado ao cubo é: {cubo_do_terceiro:.2f}")

except ValueError:
    print("Erro: Você digitou um número inválido!")