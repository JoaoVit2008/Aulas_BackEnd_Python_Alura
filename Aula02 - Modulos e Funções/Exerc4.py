#Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero; x + / y +
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero; x- / y+
#Terceiro Quadrante: os valores de x e y devem ser menores que zero; x- / y-
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero; x+ / y+
#Caso contrário: o ponto está localizado no eixo ou origem.

x = float(input('digite um numero: '))
y = float(input('digite um numero: '))

if x > 0 and y > 0:
    print('Primeio Quadrante')

elif 0 > x and y > 0:
    print('Segundo Quadrante')

elif 0 > x and 0 > y:
    print('Terceiro Quadrante')

elif x > 0 and 0 > y:
    print('Quarto Quadrante')

else:
    print('ponto não encontrado!')