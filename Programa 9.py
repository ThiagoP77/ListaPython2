"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 9 - Faça um Programa que leia três números
e mostre-os em ordem decrescente.
Data: 23/09/21
Atualização: 25/09/21
"""

# Entrada de dados
print("=====================================================")
print("PROGRAMA QUE MOSTRA TRÊS NÚMEROS EM ORDEM DECRESCENTE")
print("=====================================================")
print(" ")
print("-Insira os dados exigidos abaixo-")
print(" ")
numero1 = float(input("Informe o primeiro número: "))#Comando que pede para o usuário digitar o primeiro número
numero2 = float(input("Informe o segundo número: "))#Comando que pede para o usuário digitar o segundo número
numero3 = float(input("Informe o terceiro número: "))#Comando que pede para o usuário digitar o terceiro número
print(" ")

# Processamento e saída de dados
if(numero1>=numero2)and(numero1>=numero3):#Comando que gera o resultado caso o primeiro número seja maior ou igual aos outros dois números
    if(numero1>numero2)and(numero1>numero3)and(numero2<=numero3):#Comando que gera o resultado caso o primeiro número seja o maior e o segundo seja menor ou igual ao terceiro
        if(numero2==numero3):#Comando que gera o resultado caso o segundo e terceiro número sejam iguais
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f."%(numero1,numero2))
        elif(numero2<numero3):#Comando que gera o resultado caso o segundo número seja o menor
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f,%.2f."%(numero1,numero3,numero2))
    elif(numero1>numero2)and(numero1>numero3)and(numero3<=numero2):#Comando que gera o resultado caso o primeiro número seja o maior e o terceiro seja menor ou igual ao segundo
         if(numero3<numero2):#Comando que gera o resultado caso o terceiro número seja o menor
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f,%.2f."%(numero1,numero2,numero3))
    elif(numero1==numero2)and(numero1!=numero3):#Comando que gera o resultado caso o primeiro número seja igual ao segundo e diferente do terceiro
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("Ordem decrescente: %.2f,%.2f."%(numero1,numero3))
    elif(numero1==numero3)and(numero1!=numero2):#Comando que gera o resultado caso o primeiro número seja igual ao terceiro e diferente do segundo
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("Ordem decrescente: %.2f,%.2f."%(numero1,numero2))
    elif(numero1==numero2)and(numero1==numero3):#Comando que gera o resultado caso os três números sejam iguais
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("Ordem decrescente: %.2f."%(numero1))
        
elif(numero2>=numero1)and(numero2>=numero3):#Comando que gera o resultado caso o segundo número seja maior ou igual aos outros dois números
    if(numero2>numero1)and(numero2>numero3)and(numero1<=numero3):#Comando que gera o resultado caso o segundo número seja o maior e o primeiro seja menor ou igual ao terceiro
        if(numero1==numero3):#Comando que gera o resultado caso o primeiro e terceiro número sejam iguais
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f."%(numero2,numero1))
        elif(numero1<numero3):#Comando que gera o resultado caso o primeiro número seja o menor
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f,%.2f."%(numero2,numero3,numero1))
    elif(numero2>numero1)and(numero2>numero3)and(numero3<=numero1):#Comando que gera o resultado caso o segundo número seja o maior e o terceiro seja menor ou igual ao primeiro
         if(numero3<numero1):#Comando que gera o resultado caso o terceiro número seja o menor
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f,%.2f."%(numero2,numero1,numero3))
    elif(numero2==numero3)and(numero2!=numero1):#Comando que gera o resultado caso o segundo número seja igual ao terceiro e diferente do primeiro
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("Ordem decrescente: %.2f,%.2f."%(numero2,numero1))

elif(numero3>=numero1)and(numero3>=numero2):#Comando que gera o resultado caso o terceiro número seja maior ou igual aos outros dois números
    if(numero3>numero1)and(numero3>numero2)and(numero1<=numero2):#Comando que gera o resultado caso o terceiro número seja o maior e o primeiro seja menor ou igual ao segundo
        if(numero1==numero2):#Comando que gera o resultado caso o primeiro e segundo número sejam iguais
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f."%(numero3,numero1))
        elif(numero1<numero2):#Comando que gera o resultado caso o primeiro número seja o menor
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f,%.2f."%(numero3,numero2,numero1))
    elif(numero3>numero1)and(numero3>numero2)and(numero2<=numero1):#Comando que gera o resultado caso o terceiro número seja o maior e o segundo seja menor ou igual ao primeiro
         if(numero2<numero1):#Comando que gera o resultado caso o segundo número seja o menor
            print("=========")
            print("RESULTADO")
            print("=========")
            print(" ")
            print("Ordem decrescente: %.2f,%.2f,%.2f."%(numero3,numero1,numero2))
