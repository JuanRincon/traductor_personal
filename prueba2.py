iden = open("/mnt/d/DiscoExtraible/Estudio/Ingles/Vocabulario.txt")
iden2 = open("Voc2")

origEng = ""
for i in iden: 
	origEng += i

origSpa= ""
for i in iden2:
	origSpa += i

iden.close()
iden2.close()

#print(a)

# a es una variable tipo string
eng = origEng

# convertimos b de cadena a lista	
eng = eng.split()

spa= origSpa
spa= spa.split()
