import math
math.pi
print("Inserire 1 se si vuole calcolare il volume del cubo")
print("Inserire 2 se si vuole calcolare il volume della sfera")
s=input()
s=int(s)
if s==1 :
	l=input("Inserire il lato del cubo ")
	l=int(l)
	v=l**3
	print("Il volume del cubo e ",v)
elif s==2 :
	r=input("Inserire il raggio della sfera ")
	r=int(r)
	v=(4./3.)*math.pi*r**3
	print("Il volume della sfera e ",v)
else:
	print("ERRORE")