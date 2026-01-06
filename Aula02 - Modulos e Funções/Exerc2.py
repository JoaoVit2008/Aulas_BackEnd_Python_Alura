#  Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Qual a sua idade? '))

if 0 < idade <= 12:
    print('você é criança')

elif 12 < idade < 18:
    print('Você é adolecente')

elif idade >= 18:
    print('Você é adulto')

else:
    print('erro!!!')