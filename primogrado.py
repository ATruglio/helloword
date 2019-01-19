print("inserire il coefficente di primo grado")
a=input()
a=int(a)
if(a==0):
	print("E una equazione senza incognita")
else:
	print("Inserire il termine noto")
	b=input()
	b=int(b)
	if(b==0):
		x=0
		print("Il risultato dell incognita e ",x)
	else:
		x=int(-b/a)
		print("Il risultato dell incognita e ",x)

	