l1 = l3 = l2 = l4 = 0
l1 = int(input('Digite uma idade(0 para calcular a média): '))
while l1 != 0: 
    l3 += 1
    l2 += l1 / l3
    l1 = int(input('Digite uma idade(0 para calcular a média): '))
print('A media foi {}'.format(l2 + 1))
