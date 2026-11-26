list = [] 
for x in range(3):
    convidados = str(input("Digite o nome do convidado: "))
    list+=[convidados]
desista = str(input("Digite o nome do convidado para remover: "))
list.remove(desista)
print(list)

