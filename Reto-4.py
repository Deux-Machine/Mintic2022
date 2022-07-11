# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
#RECUERDE QUE SU SOLUCIÓN DEBE REQUERIR DE POR LO MENOS OTRA
#FUNCIÓN MÁS APARTE DE LA FUNCIÓN main


from collections import Counter
import collections

lista_texto = """a mitad del camino de la vida, en una selva oscura me encontraba porque mi ruta habia extraviado
¡Cuán dura cosa es decir cuál era esta salvaje selva, áspera y fuerte que me vuelve el temor al pensamiento!
Es tan amarga casi cual la muerte; mas por tratar del bien que alli encontré, de otras cosas dire que me
ocurrieron. Yo no se repetir como entre ella pues tan dormido me hallaba en el punto que abandone la senda verdadera.

Más cuanod hube llegado al pie de un monte, allí donde aquel valle terminaba que el corazon habíame aterrado,
hacia lo alto mire, y vi que su cima por cualquier camino. Entonces se calmó aquel miedo un poco, que pase con tanta angustia.
Y como quien con laiento anhelante, ya salio del piélago a la orilla, se vuelve y mira al agua peligrosa, tal mi animo,
huyendo todavia, se volvio por mirar de nuevo el sitio que a los que viven traspasar no deja."""

while " " in lista_texto:
       lista_texto.strip(" ")
       
for i in range(len(lista_texto)):
    lista_texto[i] = lista_texto[i].lower()

quitar = ['-','¿','?','.',',','¡','!',':','"','–','_']
for i in range (len(lista_texto)):
    for caracter in quitar:
        lista_texto[i] = lista_texto[i].replace(caracter,"")

lista_conteo = []

conteo_de_veces = Counter(lista_texto)
lista_conteo += conteo_de_veces.most_common(20)

for i in range(len(lista_conteo)):
            lista_conteo[i]=list(lista_conteo[i])


print(lista_conteo)