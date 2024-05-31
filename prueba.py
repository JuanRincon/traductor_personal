import random

a = []

for i in range(100):
	a.append(random.randint(1,100))

print(a)
iden = open("lista", "a")

iden.write("[")

for i in range(100):
	iden.write("%a," %a[i])

iden.write("]")

iden.close()
