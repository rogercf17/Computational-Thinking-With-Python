par = 0
impar = 0
i = 0
while i < 10:
    num = int(input(f'Digite o {i+1}° número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    i += 1
print(f'Total de pares: {par}\nTotal de ímpares: {impar}')