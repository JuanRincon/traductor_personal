iden = open("Voc")

a = ""
for i in iden: 
	a = a + i

iden.close()

#print(a)

# a es una variable tipo string
b = a

# convertimos b de cadena a lista	
b = b.split()
