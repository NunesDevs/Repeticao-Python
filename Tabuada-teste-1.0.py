def goto():
 tabuada = int(input('Digite o numero que deseja: '))
 tabuada2 = int(input('Digite até numero que deseja: '))
 for l1 in range(1, tabuada2 + 1):
  print('{} x {:2} = {}'.format(tabuada, l1, tabuada*l1))
outro = str(input('Deseja Calcular uma tabuada? [S/N]')).strip().upper()[0]
while outro not in'SsNn' :
     outro = str(input('Digite um valor correto! [S/N]')).strip().upper()[0]
while outro in 'Ss' :
    goto()
while outro in 'Nn' :
     print('Obrigado por utilizar o serviço!')
     break
