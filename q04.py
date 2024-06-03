# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print(f'Você digitou "{x}"')
print('Tipo primitivo:', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Possui apenas letras maiúsculas?', x.isupper())
print('Possui apenas letras minúsculas?', x.islower())
print('Está capitalizada?', x.istitle())