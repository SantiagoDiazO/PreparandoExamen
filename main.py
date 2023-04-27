from Escuderia import Escuderia

escuderias = []

opcionEscuderia = 0

sumatoriaSalarios = 0

while (opcionEscuderia < 2):
    escuderia = Escuderia()
    escuderia.nombre = input("Ingrese el nombre de la escudería: ")
    escuderia.motor = input("Ingrese el motor de la escudería: ")
    escuderia.costoAnual = int(input("Ingrese el costo anual: "))
    # escuderia.piloto1.nombre = input("Ingrese el nombre del piloto 1: ")    
    
    escuderia.piloto1.salarioAnual = int(input("Ingrese el salario del piloto 1: "))
    escuderia.piloto2.salarioAnual = int(input("Ingrese el salario del piloto 2: "))
    
    
    
    # Metodo Append
    
    escuderias.append(escuderia)  
    
    opcionEscuderia +=1
    
# for escuderia in escuderias:
#     print(f"{escuderia.nombre}")
    
for escuderia in escuderias:
    sumatoriaSalarios = sumatoriaSalarios + escuderia.piloto1.salarioAnual + escuderia.piloto2.salarioAnual 
print(f'la sumatoria de salarios es: {sumatoriaSalarios}')
