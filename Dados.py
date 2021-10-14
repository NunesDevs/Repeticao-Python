l4 = 0
l5 = 0
l6 = 0
for l1 in range  (1, 8):
    l2 = int(input("Pessoa {} idade: ".format(l1)))
    l3 = float(input('Pessoa {} peso: '.format(l1)))
    l4 += l2
    if l3 > 90.00:
        l6 += 1
l5 = l4 / 7
print('a media da idade das sete pessoas é: {}'.format(l5))
print('{} pessoas com mais de 90.00kg'.format(l6))
    
