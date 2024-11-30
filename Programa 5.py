"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 5 - Faça um programa para a leitura de duas
notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
Data: 22/09/21
"""

# Entrada de dados
print("===================================")
print("PROGRAMA QUE VERIFICA SUA APROVAÇÃO")
print("===================================")
print(" ")
print("-Insira os dados exigidos abaixo-")
print(" ")
nota1 = float(input("Informe sua primeira nota: "))#Comando que pede ao usuário para inserir sua primeira nota
nota2 = float(input("Informe sua segunda nota: "))#Comando que pede ao usuário para inserir sua segunda nota
print(" ")

# Processamento de dados
media_provas = ((nota1+nota2)/2)#Comando que calcula a média das notas do usuário

# Saída de dados
if(media_provas<7):#Comando que gera o resultado caso a média seja menor que 7(reprovação)
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Sua média é de %.2f ponto(s)."%(media_provas))
    print("Você está reprovado!")

elif(media_provas>=7) and (media_provas<10):#Comando que gera o resultado caso a média seja maior que 7(aprovação)
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Sua média é de %.2f ponto(s)."%(media_provas))
    print("Você foi aprovado!")

elif(media_provas==10):#Comando que gera o resultado caso a média seja igual a 10(aprovação com distinção)
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Sua média é de %.2f ponto(s)."%(media_provas))
    print("Você foi aprovado com distinção! Parabéns!")

elif(media_provas>10):#Comando que gera o resultado caso a média seja maior que 10
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Sua média ultrapassou o limite de 10 pontos!")
    print("Por favor, reinicie o programa e insira os dados corretamente.")
    
    
