"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 3 - Faça um Programa que verifique se uma
letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
Data: 22/09/21
"""

# Entrada de dados
print("============================================")
print("PROGRAMA QUE VERIFICA SEXO A PARTIR DE LETRA")
print("============================================")
print(" ")
letra_sexo = str(input("Informe seu sexo (M para masculino e F para feminino): "))#Comando que pede para o usuário inserir uma letra
print(" ")

# Processamento e saída de dados
if (letra_sexo=="M") or (letra_sexo=="m"):#Comando que define quando o resultado é masculino
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Sexo masculino!")

elif (letra_sexo=="F") or (letra_sexo=="f"):#Comando que define quando o resultado é feminino
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Sexo feminino!")

else:#Comando que define quando o resultado é inválido
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Sexo inválido.")
    print("Por favor, reinicie o programa e preencha os dados corretamente!")
