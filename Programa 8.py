"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 8 - Faça um programa que pergunte o preço de
três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
Data: 23/09/21
"""

# Entrada de dados
print("================================================")
print("PROGRAMA QUE ENCONTRA O MENOR DENTRE TRÊS PREÇOS")
print("================================================")
print(" ")
print("-Insira os dados exigidos abaixo-")
print(" ")
preco1 = float(input("Informe o preço do primeiro produto: "))#Comando que pede para o usuário inserir o primeiro preço
preco2 = float(input("Informe o preço do segundo produto: "))#Comando que pede para o usuário inserir o segundo preço
preco3 = float(input("Informe o preço do terceiro produto: "))#Comando que pede para o usuário inserir o terceiro preço
print(" ")

# Processamento e saída de dados
if (preco1<=preco2) and (preco1<=preco3):#Comando que define o resultado para caso o primeiro preço seja menor ou igual aos outros dois
    if (preco1<preco2) and (preco1<preco3):#Comando que gera o resultado quando o primeiro preço é o menor
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O menor dentre os três preços é o de R$%.2f."%(preco1))
        print("Recomendo que compre o primeiro produto, pois é o mais barato!")
    elif(preco1==preco2)and(preco1!=preco3):#Comando que gera o resultado quando o primeiro e segundo preço são os menores
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O menor dentre os três preços é o de R$%.2f."%(preco1))
        print("Recomendo que compre o primeiro ou o segundo produto, pois são os mais baratos!")
    elif(preco1==preco3)and(preco1!=preco2):#Comando que gera o resultado quando o primeiro e terceiro preço são os menores
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O menor dentre os três preços é o de R$%.2f."%(preco1))
        print("Recomendo que compre o primeiro ou o terceiro produto, pois são os mais baratos!")
    elif(preco1==preco2)and(preco1==preco3):#Comando que gera o resultado quando os três preços são iguais
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O menor dentre os três preços é o de R$%.2f."%(preco1))
        print("Pode comprar qualquer um deles, pois custam o mesmo preço!")
        
elif (preco2<=preco1) and (preco2<=preco3):#Comando que define o resultado para caso o segundo preço seja menor ou igual aos outros dois
    if (preco2<preco1) and (preco2<preco3):#Comando que gera o resultado quando o segundo preço é o menor
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O menor dentre os três preços é o de R$%.2f."%(preco2))
        print("Recomendo que compre o segundo produto, pois é o mais barato!")
    elif(preco2==preco3)and(preco2!=preco1):#Comando que gera o resultado quando o segundo e o terceiro preço são os menores
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O menor dentre os três preços é o de R$%.2f."%(preco2))
        print("Recomendo que compre o segundo ou o terceiro produto, pois são os mais baratos!")

elif (preco3<=preco1) and (preco3<=preco2):#Comando que define o resultado para caso o terceiro preço seja menor ou igual aos outros dois
    if (preco3<preco1) and (preco3<preco2):#Comando que gera o resultado quando o terceiro preço é o menor
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("O menor dentre os três preços é o de R$%.2f."%(preco3))
        print("Recomendo que compre o terceiro produto, pois é o mais barato!")



