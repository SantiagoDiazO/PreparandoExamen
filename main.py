from Escuderia import Escuderia

escuderias=[]

numeroEscuderia=0
sumatoriaSalarios=0

#Recojo datos de la escuderia y piloto
while(numeroEscuderia<2):
    escuderia=Escuderia()
    escuderia.nombre=input("Digita la escuderia: ")
    escuderia.motor=input("Digita el motor de la escuderia: ")
    escuderia.costoAnual=int(input("Digite el costo anual: "))

    escuderia.piloto1.salarioAnual=int(input("Digita Salario Piloto 1: "))
    escuderia.piloto2.salarioAnual=int(input("Digita Salario Piloto 2: "))
    

    escuderias.append(escuderia) #Agregar la escuderia a la lista
    numeroEscuderia+=1

#Recorrer la lista de escuderia
for escuderia in escuderias:
    sumatoriaSalarios=sumatoriaSalarios + escuderia.piloto1.salarioAnual + escuderia.piloto2.salarioAnual
print(f"El salario acumiulado fue: {sumatoriaSalarios}")