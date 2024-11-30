"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 10 - Faça um Programa que pergunte em que turno
você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.
Data: 23/09/21
"""

# Entrada de dados
print("==============================================")
print("PROGRAMA QUE VERIFICA EM QUE TURNO VOCÊ ESTUDA")
print("==============================================")
print(" ")
turno = str(input("Informe em que turno você estuda: "))#Comando que pede para o usuário informar em que turno estuda
print(" ")

# Processamento e saída de dados
if(turno=="M")or(turno=="m")or(turno=="matutino")or(turno=="Matutino"):#Comando que gera o resultado quando o usuário estuda no turno matutino
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Bom dia!")

elif(turno=="V")or(turno=="v")or(turno=="vespertino")or(turno=="Vespertino"):#Comando que gera o resultado quando o usuário estuda no turno vespertino
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Boa tarde!")

elif(turno=="N")or(turno=="n")or(turno=="noturno")or(turno=="Noturno"):#Comando que gera o resultado quando o usuário estuda no turno noturno
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Boa noite!")
    

else:#Comando que gera o resultado quando o usuário não informa os dados corretamente
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Valor inválido!")
    print("Por favor, reinicie o programa e insira os dados corretamente!")

