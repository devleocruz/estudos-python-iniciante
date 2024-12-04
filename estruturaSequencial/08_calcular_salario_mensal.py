"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
try:
    salario_por_hora = float(input("Quanto você ganha por hora (R$)?\n"))
    horas_trabalhadas = float(input("Quantas horas você trabalhou neste mês?\n"))

    salario_por_hora *= horas_trabalhadas

    print(f"Seu salário neste mês será R${salario_por_hora:.2f}")
    
except ValueError:
    print("Erro: Você digitou um número inválido!")