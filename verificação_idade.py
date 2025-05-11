# Verificador de maioridade em Python

try:
    idade = int(input('Digite sua idade: '))
    
    if idade >= 18:
        print('Você é maior de idade!')
    elif idade > 0:
        print('Você é menor de idade.')
    else:
        print('Idade inválida. Digite um número positivo.')
        
except ValueError:  # Se o usuário digitar texto em vez de número
    print('Erro: Digite apenas números!')
