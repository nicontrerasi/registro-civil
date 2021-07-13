from numpy import array
import random
import pruebaj

valor=[]
nombre=[]
certificado=[]
cantidad=[]

op=1

while op!=5:
	print("\n\n\tRegistro Civil\n\n\t")
	print("\n1. Ingresar")
	print("\n2. Mostrar")
	print("\n3. Más solicitados")
	print("\n4. Total")
	print("\n5. Salir")
	op=int(input("\n\tElija opción: "))

	if op==1:
		while True:
			try:
				n=int(input("\n\tCantidad de personas: "))
				if n>0:
					break
				else:
					print("\n\n\tDebe ser mayor a 0")
			except ValueError:
				print("Debe ser un número entero")
		pruebaj.llenar(n,nombre,certificado,cantidad)

	if op==2:
		if (len(certificado)==0):
			print("\n\tDebe ingresar información en opción 1")
		else:
			pruebaj.total(n,certificado,cantidad,valor)
			pruebaj.mostrar(n,nombre,certificado,cantidad,valor)






