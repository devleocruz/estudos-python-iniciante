"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math
try:
    area = max(0, float(input("Tamanho em metros quadrados da área a ser pintada:\n")))
    
    cobertura_por_litro = 3
    capacidade_lata = 18
    preco_lata = 80.00
    
    quantidade_litro = area / cobertura_por_litro
    quantidade_lata = math.ceil(quantidade_litro / capacidade_lata)
    # Primeiramente eu pensei em usar round(), mas ele só arredonda para o número mais próximo - 1,4 lata de tinta para 1 lata -, o que não seria correto.
    # A função math.ceil() arredonda para o número inteiro superior, o que é mais ideal
    preco = preco_lata * quantidade_lata

    print(f"Para pintar {area:.2f} m² você precisará de:\n"
      f" {quantidade_litro:.2f} litros.\n"
      f" {quantidade_lata} lata(s) de tinta.\n"
      f" O preço total será R$ {preco:.2f}")

except ValueError:
  print("Erro: Você digitou um número inválido!")