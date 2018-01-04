r= float(input('Digite um valor: '))
def perimetro(r):
	try:
		return 2*3.14*r
	except:
		print 'Argumento da funcao deve ser umm numero!'
def area(r):
	try:
		return 3.14*(r**2)
	except :
		print 'Argumento da funcao deve ser umm numero!'

def potencia(x,y=2):
	try:
		return x**y
	except:
		print 'Argumento da funcao deve ser umm numero!'
def nada(r):
	pass

print perimetro(r)
print area(r)
print potencia(r)
print nada(r)