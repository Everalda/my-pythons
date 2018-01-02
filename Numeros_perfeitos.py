
n = int(input('Digite o numero para ser testado:'))
print n
teste = 0
for i in range (1,n):
	if n % i == 0:
		teste=teste+i
if teste == n:
	print n,'e um numero perfeito'
else:
	print n,'nao e um numero perfeito'