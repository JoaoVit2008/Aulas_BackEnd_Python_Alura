import os

def exibir_nome_do_cod():
    print("Sabor Express\n")

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def escolher_opcao():
    opcao_escolhida = input('escolha uma opção: ')
    print('Você escolheu a opção', opcao_escolhida)
    
def finalizar_cod():
    os.system('cls')
    print('Finalizado programa!!!')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar Restaurante')

    elif opcao_escolhida == 2:
        print('Listar restaurantes: ')

    elif opcao_escolhida == 3:
        print('Ativar restaurante: ')

    else:
        finalizar_cod()

def main():
    exibir_nome_do_cod()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()