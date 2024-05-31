from prueba2 import eng,spa


def select_lang():
	print("1. for vocabulary english to spanish")
	print("2. for vocabulary spanish to english")
	sele = int(input(""))
	if sele == 1:
		lang = eng
	else:
		lang = spa
	return(lang)

lang = select_lang()
print(lang)
