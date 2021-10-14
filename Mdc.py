l1 = int(input('Digite o valor de a: '))
l2 = int(input('Digite o valor de b: '))
l3 = l1
while l1 % l3 != 0 or l2 % l3 != 0:
         l3 = l3 - 1
         print('mdc - ({},{})={}'.format(l1,l2,l3))
