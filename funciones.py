#Funcion simple
"""
def mi_funcion(xp1, xp2):
	print xp1
	print xp2

mi_funcion("hola",2)
"""
#Funcion con variable asignada, puede ser modificada
"""
def miFunc(xpr1,vcs=1):
	print vcs*xpr1

miFunc("hola")

print "="*10

miFunc("hola",3)
"""
#Funciones con n variables, aki la variable *p es una tupla
"""
def miFunc(p1,p2,*p):
	for val in p:
		print val

miFunc(1,2,3)
print "="*25
miFunc(1,2,3,4,5)
print "="*25
miFunc(1,2,3,4,5,6,7,8,9)
"""
#Funciones con n variables, la tupla es sustituida por diccionarios
"""
def varios(p1,p2,**otros):
	for i in otros.items():
		print i

varios(1,2,tercero=3)
"""

#Metodo append en Listas
"""
def f(x,y):
	x =x+3
	y.append(23)
	print x,y

x=22
y=[22]
f(x,y)
print x,y
"""

#Metodo con varios return
"""
def f(x,y):
	return x*2, y*2

a,b=f(1,2)
print a
print b

"""
