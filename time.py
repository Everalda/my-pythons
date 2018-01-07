import time

print time.asctime()
print time.localtime()
salve=time.localtime()
print 'Hoje :', salve[2],'do',salve[1],'de', salve[0]
