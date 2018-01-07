#instalar.py
import os
comando=os.system
comando('copy C:\Users\EVA\Documents\my-pythons\MeuModulo.py  C:\Users\EVA\Anaconda2')
NOME=raw_input('seu nome:')
NOME = 'python' + NOME
comando('md C:\Users\EVA\Documents\python-'+ NOME)
comando ('copy C:\Users\EVA\Documents\my-pythons\MeuPrograma.py C:\Users\EVA\Documents\python-'+NOME )
abrir=os.startfile
abrir('C:\Users\EVA\Documents\my-pythons\leiame.txt')