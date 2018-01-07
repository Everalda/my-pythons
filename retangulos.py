#retangulos.py
import math
raiz=math.sqrt
A=float(raw_input('Area inicial:'))
w=open('C:/Users/EVA/Documents/my-pythons/script.txt','w')
for i in range(1,51):
	a=raiz(A)
	w.write('Rectangle\n')
	pontoi=str(-a/2)+','+str(-a/2)+'\n'
	pontof=str(a/2)+ ','+str(a/2)+'\n'
	w.write(pontoi)
	w.write(pontof)
	A=2*A
w.write('Zoom\n')
w.write('Extents\n')
w.close()
