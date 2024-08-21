suma=0
cuantos=int (input("cuantos estudiantes son?"))
for i in range (1,cuantos):
    edad=int(input("digite su edad"))
    suma= suma + edad

resultado = suma / cuantos

print("el promedio de edad es:", resultado)
