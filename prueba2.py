iden = open("Voc")
iden2 = open("Voc2")

a = ""
for i in iden: 
	a = a + i

c = ""
for i in iden2:
	c = c + i

iden.close()
iden2.close()

#print(a)

# a es una variable tipo string
b = a

# convertimos b de cadena a lista	
b = b.split()

d = c
d = d.split()
