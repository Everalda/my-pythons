ordem = int(raw_input('Ordem da matriz:'))
matriz=[]
print 'Digite os termos da matriz:'
for i in range(ordem):
	matriz.append([])
	for j in range(ordem):
		termo= ' A'+str(i+1)+str(j+1)
		matriz[i].append(float(raw_input('termo '+termo+':')))
print '\n'

print 'Matriz '

for i in range(ordem):
	for j in range (ordem):
		print matriz[i][j]
print '\n'	