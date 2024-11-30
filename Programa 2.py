"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 2 - Faça um Programa que peça um valor e
mostre na tela se o valor é positivo ou negativo.
Data: 22/09/21
"""

# Entrada de dados
print("======================================================")
print("PROGRAMA QUE INDICA SE UM VALOR É POSITIVO OU NEGATIVO")
print("======================================================")
print(" ")
numero_digitado = float(input("Informe o valor: "))#Comando que pede ao usuário para que digite um número
print(" ")
                        
# Processamento e saída de dados
if (numero_digitado>0):#Comando que define o resultado quando o número digitado é positivo
    print("=========")                  
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O valor digitado é positivo!")

elif (numero_digitado<0):#Comando que define o resultado quando o número digitado é negativo
    print("=========")                  
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O valor digitado é negativo!")

elif (numero_digitado==0):#Comando que define o resultado quando o número digitado é nulo
    print("=========")                  
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O valor digitado é nulo!")
