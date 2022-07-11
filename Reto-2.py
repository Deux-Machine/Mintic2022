# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR EL NOMBRE, PARÁMETROS O RETORNO DE LA FUNCIÓN
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    pensum = [ 
    {'0123': {'nombre': 'intro a la ing', "creditos": 2}, 
    '4567': {'nombre': 'inglés', 'creditos': 1}}, 
    {}, 
    {} ]
    
    materia='9101'
    
    if len(pensum) < semestre:
        mensaje = "Ingrese un semestre válido"
    elif len(pensum[semestre-1]) < 1:
        mensaje = "El semestre no tiene materias"
    elif materia not in pensum[semestre-1]:
        mensaje = "La materia no existe"
    else:
        pensum.update({'nombre': 'lectoescritura', '´creditos': 3})
        mensaje = "Cambiada con exito"
     # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje
    

    
    