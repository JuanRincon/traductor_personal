iden = open("Vocabulario.txt")

eng = ""
for i in iden: 
	eng += i

iden.close()

# convertimos eng cadena a lista	
eng = eng.split()
