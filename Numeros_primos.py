def Numero_primo(primo):
	teste=1
	for i in range(2,primo):
		if primo % i ==0:
			teste = teste+1
	if teste == 1:
		print 'Numero primo'
	else:
		print 'Numero Nao primo'

Numero_primo(5)
Numero_primo (22) 
