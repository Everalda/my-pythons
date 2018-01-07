import calendar
'''
Verifica se o ano eh bissexto ou nao.
'''

print calendar.isleap(2004)
print calendar.isleap(2055)
''' 
retorna uma tupla contendo em que dia da semanda comeca o mes y do ano x e quantos dias tem esse mes
'''
print calendar.monthrange(2004,5)
'''
imprime o mes y do ano x
'''
print calendar.prmonth(1922,2)