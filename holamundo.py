print ('hola mundo!')
cadena= 'true'
numero1= input ('ingrese numero 1:')
numero2 = input ('ingrese numero2:')
numero3 = input('ingrese numero3:')
numero4 = numero1+numero2+numero3
verdad= True 

if (verdad):
	print'verdad'
else:
	print 'falso'

if numero4>20:
	print(str(numero4))
else:
	print('menor a 20, y el numero es:'+str(numero4))

if cadena =='true':
	print('true')

for x in range (0,10):
	print  (str(x))

sup = raw_input ('ingrese valor')
for x in range(0,int(sup)+1):
	print (str(x))
	