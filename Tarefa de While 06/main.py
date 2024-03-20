sim = input('Digite a a palavra a segui "sim": ')
nao = input('Digite a a palavra a segui "não": ')
while sim != 'sim' and nao != 'não':
    print('Digite novamente!')
    sim = input('Digite a a palavra a segui "sim": ')
    nao = input('Digite a a palavra a segui "não": ')
    if sim == 'sim' and nao == 'não':
        print('Tudo certo!')