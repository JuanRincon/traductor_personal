iden = open("/mnt/d/DiscoExtraible/Estudio/Ingles/Vocabulario.txt")

origEng = ""
for i in iden: 
	origEng += i

iden.close()

# a es una variable tipo string
eng = origEng

# convertimos b de cadena a lista	
eng = eng.split()

