import math
a=input("inserire il coefficente di secondo grado ")
a=int(a)
if a==0 :
	print("E una equazione di primo grado")
else:
	b=input("Inserire il coefficente di primo grado ")
	b=int(b)
	c=input("Inserire il termine noto ")
	c=int(c)
	if(b==0):
		if(c<0):
			x1=int(-(math.sqrt(-c/a)))
			x2=int(-x1)
			print("I risultati dell incognita sono ",x1,"  ",x2)
		else:
			print("L equazione non ammette soluzioni reali")
	elif(c==0):
		x1=0
		x2=int(-b/a)
		print("I risultati dell incognita sono ",x1,x2)
	else:
		d=b**2-4*a*c
		if(d==0):
			x=int(-b/2*a)
			print("L equazione ha due soluzioni reali e coincidenti e sono" ,x)
		elif(d<0):
			print("L equazione non ammette soluzioni reali")
		else:
			x1=int((-b-(math.sqrt(d))/2*a))
			x2=int((-b+(math.sqrt(d))/2*a))
			print("I risultati dell incognita sono ",x1," ",x2)