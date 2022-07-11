print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")

nombre = input("Por favor ingrese su nombre: ")
materia =input("Ingresa el nombre de la materia: ")

i=0
SumPorcentaje = 0
contador = 0
Estado = 0
N = False
S = True
while True:
     
   
    n1 = float(input("Ingrese la nota obtenida: "))
    p1 = int(input("Ingrese el porcentaje de la nota: "))
    i += n1
    SumPorcentaje += p1
    contador += 1
    Nota_Acomulada = i/contador*SumPorcentaje

    Estado = Nota_Acomulada
    if Estado <= 2.9:
        Estado = "reprobado"
    else:
        Estado = "aprobado"
        
    
    if SumPorcentaje == 100:
        print(f"El estudiante {nombre} curso la materia {materia} y obtuvo {i} resultando es {Estado}")
        break
    elif SumPorcentaje > 100:
        print("El porcentaje evaluado de una materia no puede ser mayor en 100")  
        SumPorcentaje -= p1
        continue
    
    op = eval(input("¿Faltan añadir notas? S/N:"))
    if op == True:
        continue
    else:
        print(f"El estudiante {nombre} curso la materia {materia} y obtuvo {i} resultando es {Estado}") 
        break