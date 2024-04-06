num = int(input('Digite um número: '))
c = 1
soma = 0 + num
while c < 5:
    num = int(input('Digite um número: '))
    soma += num
    c += 1
print(f'a soma dos número digitados é igual a {soma} e a media é {soma/5}')