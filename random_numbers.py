import random 
a=[]
for i in range(5):
	a.append(raw_input('Insira os numeros:'))

print ('o numero sorteado foi: '+ random.choice(a))