preco = float(input('Qual o preço do produto: R$\n'))
#precofinal = preco * 0.95
precofinal = preco - (preco*5/100)
print('O preço do produto com 5% de desconto ficará {:.2f}'.format(precofinal))