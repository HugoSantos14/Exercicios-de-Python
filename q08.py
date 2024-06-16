# Escreva um código que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input("Digite um valor em metros: "))
print(f"Em centímetros: {n * 100:.2f} cm")
print(f"Em milímetros: {n * 1000:.2f} mm")