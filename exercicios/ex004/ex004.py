tipo = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(tipo))
print('Só tem espaços? ', tipo.isspace())
print('Só tem números? ', tipo.isnumeric())
print('É alfabético? ', tipo.isalpha())
print('É alfanumérico? ', tipo.isalnum())
print('Está em maiúsculas? ', tipo.isupper())
print('Está em minúsculas? ', tipo.islower())


