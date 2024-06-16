# Escreva um código que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Largura em metros = "))
h = float(input("Altura em metros = "))
área = l * h
print(f"Área = {área:.2f} metros quadrados")
print(f"Para pintar essa parede, serão necessários {área / 2:.2f}L de tinta.")