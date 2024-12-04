"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""
try:
  peso = float(input("Digite o peso total de peixes (em quilos):\n"))
  
  excesso = peso - 50
  multa = max(0, excesso) * 4 # Se excesso for negativo, a multa será 0. A função max() sempre retorna o maior valor
  print(f"\nJoão, você pescou {peso:.2f} kg de peixe."
      f"\nO excesso foi de {max(0, excesso):.2f} kg."
      f"\nA multa será de R$ {multa:.2f}.")
  
except ValueError:
  print("Erro: Você digitou um número inválido!")