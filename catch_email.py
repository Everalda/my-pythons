try:
	file=open('C:/Users/EVA/Documents/my-pythons/mailcollection.txt','a')
except:
	file=open('C:/Users/EVA/Documents/my-pythons/mailcollection.txt','w')

lista= raw_input('Mail:')
lista=lista.split()
for i in range(len(lista)):
	lista[i]=lista[i].replace('<','').replace('>','').replace(',','')
mail=[]
for i in range(len(lista)):
	if lista[i].__contains__('@'):
		mail.append(lista[i])
for i in range(len(mail)):
	mail[i]=mail[i]+','
print 'Enderecos capturados:\n'
for i in mail:
	print i,
	file.write(i)
file.close()