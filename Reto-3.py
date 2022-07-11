# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
# NO ELIMINAR LAS IMPORTACIONES A CONTINUACIÓN. SU SOLUCIÓN
# DEBE BASARSE EN EL USO DE ELLAS. CREE DOS FUNCIONES, UNA
# PARA EL ENCRIPTADO Y OTRA PARA EL DESENCRIPTADO

import numpy as np
import random
import math as nt

def encriptado(texto):
   
    diccio={}
    clave=[]
    mensaje_desordenado=[]
    Unicode=[]
    Unicode2=[]
    calcularsprt=nt.ceil(np.sqrt(len(texto)))
    for i in range(calcularsprt**2-len(texto)):
      texto+="_"
    texto= np.array(list(texto))
   
    for i in range(len(texto)):
      diccio[i]=texto[i]
      clave.append(i)

    random.shuffle(clave)

    for i in clave:
        mensaje_desordenado.append(diccio[i])
 
    for i in mensaje_desordenado:
      Unicode.append(ord(i))
    
    Unicode=np.array(Unicode)

    y=int(nt.sqrt(len(Unicode)))
    for i in range(y):
      Unicode2.append(Unicode[i*y:(i+1)*y])
    array_final = np.matrix(Unicode2)
   
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL ENCRIPTADO
    #USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DE LOS
    #RETORNOS PUESTOS AL FINAL DE ESTA FUNCIÓN

    return array_final, clave


def desencriptado(array_encriptado, clave):
    list1=[]
    list2=[]
    lista3=[0]*len(clave)
    
    b=array_encriptado.tolist()
    texto=str()
    for i in b:
      list1 += i
    
    for i in list1:
      list2.append(chr(i))
    
    for i in range(len(clave)):
      lista3[clave[i]]=list2[i]

    while "_" in lista3:
      lista3.remove("_")

    texto=str()

    for i in lista3:
      texto+=i
    
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL DESENCRIPTADO
    #USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DEL
    #RETORNO PUESTO AL FINAL DE ESTA FUNCIÓN
    
    return texto