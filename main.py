from Escuderia import Escuderia
  
escuderias=[]
sumatoriaSalarios=0
numeroEscuderia=0
while(numeroEscuderia<1):
    escuderia=Escuderia()
    escuderia.nombre=input("Digita el nombre de la escuderia")
    escuderia.motor=input("Digita el motor de la escuderia")
    escuderia.costoAnual=int(input("Digita el costo anual: "))
    escuderia.piloto1.salarioAnual=int(input("Digite el salario del piloto1: "))
    escuderia.piloto2.salarioAnual=int(input("Digite el salario del piloto2: "))
    escuderias.append(escuderia)#agregar la escuderia a la lista
    numeroEscuderia+=1

#recorrer la lista de escuderia
for escuderia in escuderias:
    print(f"{escuderia.nombre}")
    sumatoriaSalarios=sumatoriaSalarios+escuderia.piloto1.salarioAnual+escuderia.piloto2.saralarioAnual
print(f"El salario acumulado fue: {sumatoriaSalarios} ")