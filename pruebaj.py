def llenar(n,aNom,aCert,aCant):
	for i in range(n):
		while True:
			nom=input("Ingrese nombre: ")
			if (len(nom)>=3):
				break
			else:
				print("El nombre debe tener al menos 3 caracteres")
		aNom.append(nom)
		aCert.append(random.choice(["Nacimiento", "Matrimonio", "Defunción", "Antecedentes"]))
		aCant.append(random.randint(1,10))

def total(n,aCert,aCant,aVal):
	for i in range (n):
		if aCert[i]=="Nacimiento":
			aVal.append(aCant[i]*750)
		if aCert[i]=="Matrimonio":
			aVal.append(aCant[i]*900)
		if aCert[i]=="Defunción":
			aVal.append(aCant[i]*1200)
		if aCert[i]=="Antecedentes":
			aVal.append(aCant[i]*1500)


def mostrar(n,aNom,aCert,aCant,aVal):
	print("\n\tInformación solicitada")
	for i in range(n):
		print("Nombre: "+(aNom[i])+" Tipo de certificado: "+(aCert[i])+" Cantidad solicitada: "+str(aCant[i])+" Total Cancelado: $"+str(aVal[i]))