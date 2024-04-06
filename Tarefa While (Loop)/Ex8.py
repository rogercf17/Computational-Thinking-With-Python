i = 0
c = 1
contador = 3
termo_final = int(input('Quantos termos da sequência de fibonacci deseja mostrar? '))
print(i)
print(c)
while contador <= termo_final:
    aux = i + c
    print(aux)
    i = c
    c = aux
    contador += 1
print(f'Fim esses são os {termo_final} primeiros termos da sequência de fibonacci.')