salario = int(input('Digite seu salário: '))
aumento = 1.5/100
salario += (salario * aumento)
contador = 1997
while contador <= 2024:
    aumento = 3/100
    salario += (salario * aumento)
    contador += 1
print(f'Seu salário com o aumento será de R$ {salario:.2f}')