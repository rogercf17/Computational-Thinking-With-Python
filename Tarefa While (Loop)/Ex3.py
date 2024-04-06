popA = 80000
popB = 200000
anos = 0
taxa_a = 1 + (3/100)
taxa_b = 1 + (1.5/100)
while True:
    popA *= taxa_a
    popB *= taxa_b
    if popA == popB or popA > popB:
        break
    anos += 1
print(anos)