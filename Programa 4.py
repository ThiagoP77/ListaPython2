"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 4 - Faça um Programa que verifique
se uma letra digitada é vogal ou consoante.
Data: 22/09/21
"""

# Entrada de dados
print("=========================================")
print("PROGRAMA QUE IDENTIFICA VOGAL E CONSOANTE")
print("=========================================")
print(" ")
letra = str(input("Informe a letra a ser identificada: "))#Comando que pede para o usuário inserir uma letrar
print(" ")

# Processamento e saída de dados
if(letra=="A")or(letra=="E")or(letra=="I")or(letra=="O")or(letra=="U")or\
(letra=="a")or(letra=="e")or(letra=="i")or(letra=="o")or(letra=="u"):#Comando que define quando a letra digitada é vogal
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("A letra digitada é uma vogal!")

elif(letra=="B")or(letra=="C")or(letra=="D")or(letra=="F")or(letra=="G")or\
(letra=="H")or(letra=="J")or(letra=="K")or(letra=="L")or(letra=="M")or\
(letra=="N")or(letra=="P")or(letra=="Q")or(letra=="R")or(letra=="S")or\
(letra=="T")or(letra=="V")or(letra=="W")or(letra=="X")or(letra=="Y")or\
(letra=="Z")or(letra=="b")or(letra=="c")or(letra=="d")or(letra=="f")or\
(letra=="g")or(letra=="h")or(letra=="j")or(letra=="k")or(letra=="l")or\
(letra=="m")or(letra=="n")or(letra=="p")or(letra=="q")or(letra=="r")or\
(letra=="s")or(letra=="t")or(letra=="v")or(letra=="w")or(letra=="x")or\
(letra=="y")or(letra=="z"):#Comando que define quando a letra digitada é consoante
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("A letra digitada é uma consoante!")
    
elif (len(letra)>1):#Comando que define o resultado quando é digitado mais do que uma letra
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Parece que você digitou mais do que um caractere!")
    print("Por favor, reinicie o programa e preencha os dados corretamente!")

else:#Comando que define o resultado quando não se digita uma letra
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O caractere digitado não é vogal e nem consoante!")
