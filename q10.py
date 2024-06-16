# Escreva um código que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,38.

n = float(input("Seu dinheiro: R$"))
print(f"Você pode trocar por {n / 5.38:.2f} dólares americanos.")