nome = input('Digite seu nome:')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso; '))
imc = peso / (altura ** 2)


print('O imc de', nome, 'é de', imc)
