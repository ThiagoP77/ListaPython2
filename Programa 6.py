"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 6 - Faça um Programa que leia três números
e mostre o maior deles.
Data: 22/09/21
"""

# Entrada de dados
print("=================================================")
print("PROGRAMA QUE ENCONTRA O MAIOR DENTRE TRÊS NÚMEROS")
print("=================================================")
print(" ")
print("-Insira os dados exigidos abaixo-")
print(" ")
numero1 = float(input("Informe o primeiro número: "))#Comando que pede para o usuário inserir o primeiro número
numero2 = float(input("Informe o segundo número: "))#Comando que pede para o usuário inserir o segundo número
numero3 = float(input("Informe o terceiro número: "))#Comando que pede para o usuário inserir o terceiro número
print(" ")

# Processamento e saída de dados
if (numero1>=numero2) and (numero1>=numero3):#Comando que define o resultado para caso o primeiro número seja maior ou igual aos outros números
    if(numero1==numero2) and (numero1!=numero3):#Comando que define o resultado para caso o primeiro número seja o maior e igual ao segundo
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O maior dentre esses três números é o %.2f."%(numero1))
    elif(numero1==numero3) and (numero1!=numero2):#Comando que define o resultado para caso o primeiro número seja o maior e igual ao terceiro
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O maior dentre esses três números é o %.2f."%(numero1))
    elif(numero1>numero3) and (numero1>numero2):#Comando que define o resultado para caso o primeiro número seja o maior
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O maior dentre esses três números é o %.2f."%(numero1))
    elif(numero1==numero2)and(numero2==numero3):#Comando que define o resultado para caso os três números sejam iguais
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("Os três números são iguais!")
        
elif (numero2>=numero1) and (numero2>=numero3):#Comando que define o resultado para caso o segundo número seja maior ou igual aos outros números
    if(numero2==numero3) and (numero2!=numero1):#Comando que define o resultado para caso o segundo número seja o maior e igual ao terceiro
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O maior dentre esses três números é o %.2f."%(numero2))
    elif(numero2>numero1)and(numero2>numero3):#Comando que define o resultado para caso o segundo número seja o maior
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O maior dentre esses três números é o %.2f."%(numero2))
        

elif (numero3>numero1) and (numero3>numero2):#Comando que define o resultado para caso o terceiro número seja o maior
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O maior dentre esses três números é o %.2f."%(numero3))



    
   
