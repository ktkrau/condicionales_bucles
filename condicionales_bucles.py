"""""
python3 nombre_archivo para iniciar terminal
"""""
#CONDICIONALES

x = 2
if x > 10:
    print("Mayor a  10")
else:
    print("Menor a 10")

if x < 10:
    print("menor a 10")
elif x > 25:
    print("Mayor a 25")
else:
    print("Número entre 10 y 25")

y=2
if(y < 5 and x>10):
    print("Y menor a 5, X mayor a 10")
else:
    print("Alguna de las condicionales no se cumplió")

i= 10
if(i >5 and i%2 == 0 and i% 5 == 0):
    print("Se cumple con 3")

#BUCLES o CICLOS

for i in range(5): #del 0 hasta el 4. Ya NO entra en el 5
    print(i)
print('-------------------')

for j in range(1, 5): #del 1 al 4. Ya NO entra en el 5
    print(j)
print('-------------------')

for k in range(1, 10,2): #Comienzo, parada, cantidad a avanzar resultado:(1,3,5,7,9)
    print(k)
print('-------------------')

for l in range(0, 10,2): #0,2,4,6,8
    print(l)
print('-------------------')

#Podemos recorrer textos

string = "Buenos días"
for a in string:
    print(a)


""" for(var i=0; i<array.length;i++){
    console.log(array[i])
} """


gastos=[10,20,30,10]
total=0
#total = 0
#gasto = 10
#total = 0 + 10 = 10

#gasto = 20
#total = 10 + 20 = 30

#gasto = 30
#total = 30 + 30 = 60

#gasto = 10
#total = 60 + 10 = 70


for gasto in gastos:
    total+= gasto

print(total)
array = ['A','B','C','D']
for i in range(0, len(array)): # para saber el indice o posicion de mi arreglo
    print(i, array[i])


diccionario = {"nombre": "Elena", "apellido": "De Troya", "edad": 31}
for llave in diccionario:
    print(llave,diccionario[llave])

#WHILE

y= 0
while y <3:
    print(y)
    y+=1
else: 
    print("Sentencia else final") #este else es opcional

num = 1
while num <15:
    print(num)
    num +=2
else: #este else es opcional
    print("Ya no entra al ciclo porque el número es", num)

#BREAK: interrupcion completa de mi bucle // cuando nos encontramos con un break, el bucle deja de ejecutarse por completo

#CONTINUE: interrupcion solo de esa ronda del bucle. Cuando nos encontramos con un continue, el bucle ignora esa ronda y continúa con la siguiente

#RETO 1
#Dado un for y recorriendo del 1 al 15, imprime todos los numeros excepto aquellos multiplos de 5: -Break o continue
for x in range(1,16):
    if x % 5 == 0:
        continue
    else:
        print(x)
#RETO 2
#Dada una cadena imprime cada uno de los caracteres y detente cuando encuentres un punto(.)

cadena1 = "Había una vez una niña. Esa niña quería aprender Python"

for letra  in cadena1:
    if letra in cadena1:
        if letra == ".":
            break

        print(letra)

#10-100 cuando sea divisible entre 3 imprima pizza
#divisible entre 7, imprima sandwich

for x in range(1,101): #var x=1; x<101;x++
    if x % 3 == 0:
        print("pizza")
    elif x % 7 == 0:
        print("sandwich")
    else:
        print(x)