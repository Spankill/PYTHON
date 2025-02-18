#variables y tipos de datos 
nombre = "Cristiano Ronaldo"
edad = 40
es_goat = True

#estructuras de control
if es_goat:
    print(f"{nombre} es el mejor del mundo. Tiene {edad} anios.")
else:
    print(f"{nombre} no es el mejor del mundo")

#listas y bucles 
equipos = ["Sporting", "Real madrid", "Al hilal"]
for equipo in equipos:
    print(f"{nombre}, jugo en {equipo}")
    
    
#funciones 
def calcular_promedio(goles,partidos):
    return goles / partidos

promedio = calcular_promedio(940, 1500)
print(f"Promedio de goles: {promedio: .2f}")