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
preço = float(input('preço das compras: R$ '))
print('''
	[1] a vista no dinheiro
	[2] a vista no cartão
	[3] em ate 2x no cartão
	[4] 3x ou mais no cartão
	''')
opiçao = int(input('qual e a opiçao: '))
print(' ')
if opiçao == 1:
    total = preço - (preço * 10 / 100)
elif opiçao == 2:
    total = preço - (preço * 5 / 100)
elif opiçao == 3:
    total = preço
    parcela = total / 2
    print('sua compra sera parcelada em 2x de R${} '.format(parcela))
elif opiçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('quantas parcelas ? : '))
    parcelas = total / totparc
    print('sua compra sera parcelada em {}x de R${:.2f} '.format(totparc, parcelas))
print('sua compra de {:.2f} vai custar {:.2f} \nno final'.format(preço, total))     
    
    
    
    
    
