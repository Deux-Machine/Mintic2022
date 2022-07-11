print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre = input("Por favor ingrese su nombre: ")
materia = input("Ingresa el nombre de la materia: ")

i=0
SumPorcentaje = 0
Estado = 0

S = True
N = False

while SumPorcentaje < 100:
    n1 = float(input("Ingrese la nota obtenida: "))
    p1 = int(input("Ingrese el porcentaje de la nota: "))
    i += (n1*p1)
    SumPorcentaje += p1
    Nota_Acomulada = i/100
    Estado = Nota_Acomulada
    
    if Estado >= 3.0:
        Estado = "aprobado"
    else:
        Estado = "reprobado"
        
    if SumPorcentaje == 100:
        print(f'El estudiante {nombre.capitalize()} cursó la materia {materia.capitalize()} y obtuvo {round(Nota_Acomulada,2)} resultando en {Estado}')
        break
    elif SumPorcentaje > 100:
        print("El porcentaje evaluado de una materia no puede ser mayor a 100")  
        SumPorcentaje -= p1
        i -= (n1*p1)
        continue
    
    op = eval(input("¿Faltan añadir notas? S/N:"))
    if op == S:
        continue
    elif op == N:
        print(f'El estudiante {nombre.capitalize()} cursó la materia {materia.capitalize()} y obtuvo {round(Nota_Acomulada,2)} resultando en {Estado}')
    break