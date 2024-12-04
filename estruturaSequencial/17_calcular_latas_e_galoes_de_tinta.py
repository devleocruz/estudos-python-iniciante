"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math
try:
  area = max(0, float(input("Tamanho em metros quadrados da área a ser pintada:\n")))

  area_com_folga = area * 1.10
  cobertura_por_litro = 6
  capacidade_lata = 18
  preco_lata = 80.00
  capacidade_galao = 3.6
  preco_galao = 25.00

  quantidade_litro = area_com_folga / cobertura_por_litro

  # Apenas latas
  quantidade_lata = math.ceil(quantidade_litro / capacidade_lata)
  preco_comprar_latas = preco_lata * quantidade_lata

  # Apenas galões
  quantidade_galao = math.ceil(quantidade_litro / capacidade_galao)
  preco_comprar_galao = preco_galao * quantidade_galao

  # Minha lógica matematica precisa ser melhorada
  # Misto
  latas_mistas = math.floor(quantidade_litro / capacidade_lata) # A função math.floor() em Python arredonda um número para baixo
  litros_restantes = quantidade_litro - (latas_mistas * capacidade_lata)
  galoes_restantes = math.ceil(litros_restantes / capacidade_galao)
  preco_misto = latas_mistas * preco_lata + galoes_restantes * preco_galao

  print(f"\nPara pintar {area:.2f} m² você precisará de {quantidade_litro:.2f} litros de tinta.\n")
  print(f"Se for comprar apenas latas de 18 litros:")
  print(f"Você precisará de {quantidade_lata} lata(s) de tinta. O preço total será R$ {preco_comprar_latas:.2f}\n")
  print(f"Se for comprar apenas galões de 3,6 litros:")
  print(f"Você precisará de {quantidade_galao} galão(ões) de tinta. O preço total será R$ {preco_comprar_galao:.2f}\n")
  print(f"Se for misturar latas e galões (menos desperdício):")
  print(f"Você precisará de {latas_mistas} lata(s) e {galoes_restantes} galão(ões) de tinta. O preço total será R$ {preco_misto:.2f}")

except ValueError:
  print("Erro: Você digitou um número inválido!")