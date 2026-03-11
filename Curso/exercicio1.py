nome = input('Digite seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite sua idade: '))
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
maior_de_idade= idade >= 18
altura_metros= float(input('Digite sua altura em metros, use o "." para separar metro de centimetro: '))


print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Idade: {idade}')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'Maior de idade: {maior_de_idade}')
print(f'Altura em metros: {altura_metros}')