"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
  + Salário Bruto : R$
  - IR (11%) : R$
  - INSS (8%) : R$
  - Sindicato ( 5%) : R$
  = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
try:
  salario_por_hora = max(0, float(input("Quantos você ganha por hora (R$)?\n")))
  horas_trabalhadas = max(0, float(input("Quantas horas você trabalhou este mês?\n")))
  # A função max() garante que o valor seja zero caso o usuário digita algum número negativo

  salario_bruto = salario_por_hora * horas_trabalhadas
  imposto_de_renda = salario_bruto * (11 / 100)
  inss = salario_bruto * (8 / 100)
  sindicato = salario_bruto * (5 / 100)
  descontos = imposto_de_renda + inss + sindicato
  salario_liquido = salario_bruto - descontos

  print(f"\nResumo do salário:")
  print(f"Salário bruto: R$ {salario_bruto:.2f}")
  print(f"\n- Imposto de Renda (11%): R$ {imposto_de_renda:.2f}")
  print(f"- INSS (8%): R$ {inss:.2f}")
  print(f"- Sindicato (5%): R$ {sindicato:.2f}")
  print(f"\nDescontos totais: R${descontos:.2f}")
  print(f"Salário Líquido: R$ {salario_liquido:.2f}")

except ValueError:
  print("Erro: Você digitou um número inválido!")