import math
def suma ():
	print ('suma')
	num1= int(raw_input('ingrese primer numero'))
	num2= int(raw_input('ingrese segundo numero'))
	num3= num1 + num2
 	print ('resultado' + str(num3))

def resta():
	print ('resta')
	num1= int(raw_input('ingrese primer numero'))
	num2= int(raw_input('ingrese segundo numero'))
	num3= num1 -num2 
	print ('resultado' + str(num3))

def multiplicacion():
	print ('multiplicacion')
	num1= int(raw_input('ingrese primer numero'))
	num2= int(raw_input('ingrese segundo numero'))
	num3= num1 *num2 
	print ('resultado' + str(num3))

def division():
	print ('division')
	num1= int(raw_input('ingrese primer numero'))
	num2= int(raw_input('ingrese segundo numero'))
	num3= num1 / num2 
	print ('resultado' + str(num3))

def raiz_cuadrada():
	print ('raiz cuadrada')
	num1= int(raw_input('ingrese numero'))
	resultado=math.sqrt(num1)
	print (resultado)


def primo():
	print ('primo')
	num= int(raw_input('ingrese numero'))
  	i=2
  	es_primo=True
  	while (i<num):
  		x=num % i
  		if x == 0:
  			es_primo= False
  			break 
  		i+=1
  	if es_primo :
  		 print (str(num)+ ' es primo')
	else:
	 	 print (str(num)+ 'no es primo')
def salir ():
	print ('gracias por venir')



opciones= {

	1:suma,
	2:resta,
	3:multiplicacion,
	4:division,
	5:raiz_cuadrada,
	6:primo,
	7:salir
}

num = 0
while (num!= 7):
	num = input ('seleccione operacion:')
	opciones[num]()




	
