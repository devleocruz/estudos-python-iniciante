"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
try:
    lado = float(input("Qual o lado do quadrado?\n"))

    area = lado * lado # Área do quadrado é A = lado^2
    # Alternativa: "lado *= lado" também é válido

    print(f"A área do quadrado é {area:.2f}")
    print(f"O dobro da área do quadrado é {2 * area:.2f}")
    
except ValueError:
    print("Erro: Você digitou um número inválido!")