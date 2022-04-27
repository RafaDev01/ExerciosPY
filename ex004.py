n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('Número digitado: {} \n dobro: {} \n triplo: {} \n raiz quadrada {:.2f}.'.format(n, d, t, r))
#{:.2f} representa -> 2 casas decimais flutuantes
#poderia ser feito tambem:
print('Número digitado: {} \n dobro: {} \n triplo: {} \n raiz quadrada {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
print('-----------------------------\n------------------------')
print('Número digitado: {} \n dobro: {} \n triplo: {} \n raiz quadrada {:.2f}.'.format(n, (n*2), (n*3), pow(n, (1/2))))