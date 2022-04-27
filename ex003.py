n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O sucessor de {} é {} e o antecessor é {}.'.format(n, s, a))
#Poderia ser feito também sem as variaveis
print('O sucessor de {} é {} e o antecessor é {}.'.format(n, (n+1), (n-1)))