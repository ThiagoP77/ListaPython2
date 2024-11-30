"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 7 - Faça um Programa que leia três números
e mostre o maior e o menor deles.
Data: 22/09/21
"""

# Entrada de dados
print("=========================================================")
print("PROGRAMA QUE ENCONTRA O MAIOR E MENOR DENTRE TRÊS NÚMEROS")
print("=========================================================")
print(" ")
print("-Insira os dados exigidos abaixo-")
print(" ")
numero1 = float(input("Informe o primeiro número: "))#Comando que pede para o usuário inserir o primeiro número
numero2 = float(input("Informe o segundo número: "))#Comando que pede para o usuário inserir o segundo número
numero3 = float(input("Informe o terceiro número: "))#Comando que pede para o usuário inserir o terceiro número
print(" ")

# Processamento e saída de dados
if(numero1>=numero2)and(numero1>=numero3):#Comando que gera o resultado quando o primeiro número é o maior
    if(numero1>numero2)and(numero1>numero3)and(numero2<=numero3)or(numero1>numero2)and(numero1==numero3):#Comando que verifica se o primeiro é o maior e se o segundo é o menor e gera o resultado
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O número", numero1, "é o maior dentre os três números.")
        print("O número", numero2, "é o menor dentre os três números.")
    elif(numero1>numero2)and(numero1>numero3)and(numero3<=numero2)or(numero1>numero3)and(numero1==numero2):#Comando que verifica se o primeiro é o maior e se o terceiro é o menor e gera o resultado
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O número", numero1, "é o maior dentre os três números.")
        print("O número", numero3, "é o menor dentre os três números.")
    elif(numero1==numero2)and(numero1==numero3):#Comando que verifica se os três números são iguais e gera o resultado
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("Os três números são iguais!")
    
        
elif(numero2>=numero1)and(numero2>=numero3):#Comando que gera o resultado quando o segundo número é o maior
    if(numero2>numero1)and(numero2>numero3)and(numero1<=numero3)or(numero2>numero1)and(numero2==numero3):#Comando que verifica se o segundo é o maior e se o primeiro é o menor e gera o resultado
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O número", numero2, "é o maior dentre os três números.")
        print("O número", numero1, "é o menor dentre os três números.")
    elif(numero2>numero1)and(numero2>numero3)and(numero3<=numero1)or(numero2>numero3)and(numero2==numero1):#Comando que verifica se o segundo é o maior e se o terceiro é o menor e gera o resultado
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O número", numero2, "é o maior dentre os três números.")
        print("O número", numero3, "é o menor dentre os três números.")

elif(numero3>=numero2)and(numero3>=numero1):#Comando que gera o resultado quando o terceiro número é o maior
    if(numero3>numero1)and(numero3>numero2)and(numero1<=numero2)or(numero3>numero1)and(numero3==numero2):#Comando que verifica se o terceiro é o maior e se o primeiro é o menor e gera o resultado
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O número", numero3, "é o maior dentre os três números.")
        print("O número", numero1, "é o menor dentre os três números.")
    elif(numero3>numero1)and(numero3>numero2)and(numero2<=numero1)or(numero3>numero2)and(numero3==numero1):#Comando que verifica se o terceiro é o maior e se o segundo é o menor e gera o resultado
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O número", numero3, "é o maior dentre os três números.")
        print("O número", numero2, "é o menor dentre os três números.")   
