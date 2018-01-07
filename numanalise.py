'''
Este programa recebe um numero inteiro do usuario e faz a
analise sobre ele: se eh par ou impar, se eh primo ou nao,
se eh perfeito ou nao, imprime seu divisores e calcula a soma dos 
seus algarismos
'''

def test_par(n):
	if n%2==0:
		print n,'e um numero par'
	else:
		print n,'e um numero impar'

def test_primo(n):
	teste=0
	for i in range(2,n-1):
		if n % i ==0:
			teste=teste+1
	if teste <> 0:
		print n,'nao e primo'
	else:
		print n, 'e primo'

def test_perfeito(n):
	verifica=1
	for i in range(1,n):
		if n % i==0:
			verifica=verifica+i
	if verifica == n:
		print n,'e perfeito'
	else:
		print n, 'nao e perfeito'

def procura_divisores(n):
	lista_de_divisores=[]
	for i in range(1,n+1):
		if n%i ==0:
			lista_de_divisores.append(i)
	if len(lista_de_divisores)==0:
		print n, 'Nao tem divisores'
	else:
		print 'Divisores de',n,':'
		for i in lista_de_divisores :
			print i

def soma_algarismos(n):
	print('\n')
	m=0
	for i in range(1,n+1):
		m=m+i
	print 'Soma dos algarismos:\n'
	print m

n=int(raw_input('Digite o numero a ser analisado: \n'))	
test_par(n)
test_primo(n)
test_perfeito(n)
procura_divisores(n)
soma_algarismos(n)