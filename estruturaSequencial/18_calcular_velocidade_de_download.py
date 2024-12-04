"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."
"""
try:
      dowload = max(0.1, float(input("Qual o tamanho de um arquivo para download (em MB)?\n")))
      velocidade = max(0.1, float(input("Qual a velocidade da Internet (em Mbps)?\n")))

      # 1 MB = 8 megabits (Mb).
      # Converta MB para megabits:
      dowload_megabits = dowload * 8
      tempo = dowload_megabits / velocidade
 
      print(f"Um arquivo de {dowload} MB, com uma velocidade de {velocidade} Mbps, "
            f"levará cerca de {tempo:.2f} minutos para ser baixado.")

except ValueError:
  print("Erro: Você digitou um número inválido!")