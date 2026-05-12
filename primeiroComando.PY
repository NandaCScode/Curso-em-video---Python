
#   Basico de python - by Gustavo Guanabara


nome = "fernanda"   #Nome recebe Fernanda, string é aspas
idade = 20          #Idade recebe 20, numero não é string, sem aspas
peso = 72.5

print("nome:", nome)
print("idade:", idade)
print("peso:", peso) #print mostra na tela a mensagem

#Jeito mais organizado que achei de fazer


#------------------------------------------------------------

#Jeito ensinado no curso por enquanto

nome = "fernanda"
idade = 20
peso = 72.5

print(nome, idade, peso)

#-------------------------------------------------------------

#Como queremos perguntar ao usuario as coisas, vamos usar Input

nome = input("Qual o seu nome?")
idade = input("Qual a sua idade?")
peso = input("Qual é o seu peso?")
print(nome, idade, peso)
# ESSE É LEGAL
#---------------------------------------------------------

#vou tentar fazer um sozinha e e diferente
nome = input("qual o seu nome?")
idade = input(f"{nome},Qual sua idade? ")
peso = input(f"{nome}, Qual seu peso?")
print(nome, idade, peso)
#legal, curti
