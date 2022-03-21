print(' ')
print('=====|DESAFIO 44|=====')
'''
elabore um programa que calcule o 
valor a ser pago por um produto. 
considerando o seu preço normal e 
condição de pagamento:

- a vista dinheiro/cheque: 10% de 
desconto
- a vista no cartão:5% de desconto
- em ate 2x no cartão: preço normal 
- 3x ou mais no cartão: 20% de juros
'''
print(' ')
a = float(input('valor a pagar ? : R$ '))
print(' ')
b = input('''[1] a vista no dinheiro/cheque \n[2] a vista no cartão \n[3] em ate 2x no cartão \n[4] 3x ou mais no cartão 
\nqual meio de pagamento ? : ''' )
c = a * (10/100)
d = a * (5/100)
e = ((20/100) * a) / 3
ea = ((20/100) * a) / 4
eb = ((20/100) * a) / 5
ec = ((20/100) * a) / 6
f = a / 2
z = input('em quantas vezes ? : ' )
print(' ')
#print('{}'format(b))
if b == 1:
    print('o valor a pagar agora e R${} '.format(c))
elif b == 2:
    print('o valor a pagar agora e R${} '.format(d))   
elif b == 3:
    print('o valor a pagar e 2x de R${}  '.format(f))           	
elif b == 4:
    print(f'{z}')
else:
    print(' ')    
          
if z == 3:
    print('o valor a pagar agora e R${} '.format(e))
elif z == 4:
    print('o valor a pagar agora e R${} '.format(ea))    
elif z == 5:
    print('o valor a pagar agora e R${} '.format(eb))        
elif z == 6:
    print('o valor a pagar agora e R${} '.format(ec))   
else:
    print(' ')   