from Escuderia import Escuderia

escuderias=[]

numeroEscuderia=0
sumatoriaSalarios=0

while(numeroEscuderia<2):
    escuderia=Escuderia()
    escuderia.nombre=input("Digite el nombre de la escuderia: ")
    escuderia.motor=input("Digite el motor de la escuderia: ")
    escuderia.costoAnual=input("Digite el costo anual: ")
    escuderia.piloto1.salarioAnual=int(input("Digita el salario del piloto1: "))
    escuderia.piloto2.salarioAnual=int(input("Digita el salario del piloto2: "))
    
    escuderias.append(escuderia) #agregar la escuderia a la lista
    numeroEscuderia+=1
    
#recorrer la lista de esciderias
for escuderia in escuderias:
    #print(f"{escuderia.nombre}")
    sumatoriaSalarios=sumatoriaSalarios+escuderia.piloto1.salarioAnual+escuderia.piloto2.salarioAnual
    print(f"El salario acumulado fue: {sumatoriaSalarios}")
