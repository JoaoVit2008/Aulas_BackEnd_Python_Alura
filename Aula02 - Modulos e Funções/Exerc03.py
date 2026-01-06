# Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario_correto = 'joao'
senha_correta = 'joao123'

usuario = input('digite o nome de usuario: ')
senha = input('digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Login bem sucedido!')

else: 
    print('erro')