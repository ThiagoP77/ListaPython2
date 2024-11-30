"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 1 - Faça um Programa que peça
dois números e imprima o maior deles.
Data: 22/09/21
"""

# Entrada de dados
print("====================================")
print("PROGRAMA QUE ENCONTRA O MAIOR NÚMERO")
print("====================================")
print(" ")
print("-Insira os dados exigidos abaixo-")
print(" ")
numero1 = float(input("Informe o primeiro número: ")) #Comando que pede ao usuário para digitar o primeiro número
numero2 = float(input("Informe o segundo número: ")) #Comando que pede ao usuário para digitar o segundo número
print(" ")

# Processamento e saída de dados
if (numero1>numero2): #Comando que define o resultado caso o primeiro número seja o maior
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O maior dentre os dois números digitados é o %.2f."%(numero1))

elif (numero2>numero1): #Comando que define o resultado caso o segundo número seja o maior
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O maior dentre os dois números digitados é o %.2f."%(numero2))

elif (numero1==numero2): #Comando que define o resultado caso os dois números sejam iguais
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Os dois números digitados são iguais!")
    
    


