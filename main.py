from Escuderia import Escuderia

escuderias=[]

numeroEscuderia=0
sumatoriaSalarios=0
while(numeroEscuderia<2):
    escuderia=Escuderia()
    escuderia.nombre=input("Digita el nombre de escuderia: ")
    escuderia.motor=input("Digita el motor de la escuderia: ")
    escuderia.costoAnual=int(input("Digita el costo anual: "))
    
    escuderia.piloto1.salarioAnual=int(input("Digita el salario del piloto1: "))
    escuderia.piloto2.salarioAnual=int(input("Digita el salario del piloto2: "))

    escuderias.append(escuderia) #agregar la escuderia a la lista
    numeroEscuderia+=1

#recorrer la lista de escuderias
for escuderia in escuderias:
    sumatoriaSalarios=sumatoriaSalarios+escuderia.piloto1.salarioAnual+escuderia.piloto2.salarioAnual
print(f"El salario acumulado fue: {sumatoriaSalarios}")
   