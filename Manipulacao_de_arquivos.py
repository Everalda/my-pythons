abertura=open('C:/Users/EVA/Documents/my-pythons/arquivos/tabela.txt','w')
abertura.close()
abrindo=open('C:/Users/EVA/Documents/my-pythons/arquivos/tabela.txt','a')
abrindo.write('%s\n' % 'Tabela de Dolares')
abrindo.close()
vamosdigitar=open('C:/Users/EVA/Documents/my-pythons/arquivos/tabela.txt','a')
for i in range(100):
	vamosdigitar.write('%i dolares valem %f reais\n' %(i,i*2.98))
vamosdigitar.close()
abertura=open('C:/Users/EVA/Documents/my-pythons/arquivos/tabela.txt','r')
print abertura.readline()
print abertura.readline()
abertura.close()
w=open('C:/Users/EVA/Documents/my-pythons/arquivos/tabela.txt','r')
lst=w.readlines()
print lst[0]
print lst[-1]
w.close()