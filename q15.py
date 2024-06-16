# Escreva um código que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a ser pago, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
 
km = float(input("Km percorridos: "))
dias = int(input("Dias de aluguel: ")) 
print(f"Preço = R${dias * 60 + km * 0.15:.2f}")