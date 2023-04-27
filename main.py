from Escuderia import Escuderia

escuderias =[]
numeroEscuderia =0
sumatoriaSalarios =0
while(numeroEscuderia<2):
    escuderia = Escuderia()
    escuderia.nombre=input("Digita el nombre de la Escuderia: ")
    escuderia.motor=input("Digita el motor de la escuderia: ")
    escuderia.costoAnual=int(input("Digita el costo anual: "))
    escuderia.piloto1.salarioAnual=int(input("Digita el salario anual: "))
    escuderia.piloto2.salarioAnual=int(input("Digita el salario anual: "))

    # escuderia.piloto1.nombre=input("Digita el nombre del piloto: ")
    # escuderia.piloto2.nombre=input("Digita el nombre del piloto: ")
    escuderias.append(escuderia)
    numeroEscuderia+=1
# for escuderias in escuderias:
  # print (f"{escuderia.nombre}")

    
for escuderia in escuderias:
    sumatoriaSalarios=sumatoriaSalarios+escuderia.piloto1.salarioAnual+escuderia.piloto2.salarioAnual
print (f"{sumatoriaSalarios}")


from Piloto import Piloto