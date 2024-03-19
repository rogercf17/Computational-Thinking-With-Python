senha = input('Digite a senha para entrar: ')
senha_correta = '1234'
while senha != senha_correta:
    senha = input('Senha incorreta! Digite novamente: ')
print('Acesso liberado')