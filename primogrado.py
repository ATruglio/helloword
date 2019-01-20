a=input("inserire il coefficente di primo grado ")
a=int(a)
b=input("Inserire il termine noto ")
b=int(b)
if a==0 and b==0 :
	print("L equazione ammette infinite soluzioni ")
elif a==0 :
	print("L equazione non ammette soluzioni ")
else:
	x=int(-b/a)
	print("Il risultato dell incognita e ",x)