# Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def usuario():
    nome = input('Qual seu nome: ')
    senha = int(input('Digite uma senha: '))

def verificacao_usuario():
    nome_verificar = input('digite seu nome de usuario: ')
    senha_verificar = int(input('digite sua senha de usuario: '))

def verificacao():
    if usuario() == verificacao_usuario():
        print('valido')

    else:
        print('invalido')

def main():
    usuario()
    verificacao_usuario()
    verificacao()

if __name__ == '__main__':
    main()