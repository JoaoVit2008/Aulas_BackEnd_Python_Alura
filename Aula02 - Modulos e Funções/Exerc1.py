# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('digite um Numero: '))
resultado = numero%2

if resultado == 0:
    print('O numero {} é par'.format(numero))

else:
    print('O numero {} é impar' .format(numero))
