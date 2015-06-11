
tiene_arroba= False
tiene_punto = False
tiene_dos_puntos = False
tiene_dos_arrobas = False
tiene_arroba_punto= False
tiene_punto_arroba= False
correo= raw_input ('ingrese correo: ')
for x in range(0,len(correo)):
	if correo[x]== '@':
		print 'tiene arroba'
		tiene_arroba= True

	if correo[x]=='@'and correo[x+1]=='@':
		print 'incorrecto'
		tiene_dos_arrobas= False

	if correo[x]== '.':
		print 'tiene punto'
		tiene_punto = True

	if correo[x]== '.' and correo[x+1] == '.':
		print 'incorrecto'
		tiene_dos_puntos = False

	if correo[x]=='@'and correo[x+1]=='.':
		print 'incorrecto'
		tiene_arroba_punto=False

	if correo[x]=='.'and correo[x]=='@' :
		print 'incorrecto'
		tiene_punto_arroba=True

	if correo[x]=='@'and correo[x+1]=='.' and correo[x+2]=='.':
		print 'incorrecto'
		tiene_arroba_punto= False 

	if tiene_arroba and tiene_punto and not tiene_dos_puntos and not tiene_dos_arrobas \
		 and not tiene_dos_puntos and not tiene_punto_arroba \
			and not tiene_arroba_punto:
		print 'correcto electronico valido'

	







