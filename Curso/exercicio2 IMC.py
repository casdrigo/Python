"""
Quero que apareça

Fulano tem tanto de altura, pesa tantos kgs e tem o imc de tanto
"""

nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura em metro, use o "." para separar os centimetros: '))
peso = float(input('Qual seu peso? utilize o "." para separar as gramas: '))

imc = round((peso / altura**2), 2)

print(f'Seu imc é de: {imc}')