import math
math.pi
print("Inserire 1 se si vuole calcolare il volume del cubo")
print("Inserire 2 se si vuole calcolare il volume della sfera")
s=input()
s=int(s)
if(s==1):
	print("Inserire il lato del cubo")
	l=input()
	l=int(l)
	v=l**3
	print("Il volume del cubo e ",v)
elif(s==2):
	print("Inserire il raggio della sfera")
	r=input()
	r=int(r)
	v=(4./3.)*math.pi*r**3
	print("Il volume della sfera e ",v)
else:
	print("ERRORE")