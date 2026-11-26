cidades = ["Fortaleza", "Recife", "São Paulo","Salvador", "Rio de Janeiro"]
nome = input("Digite o nome de uma cidade: ")
if nome in cidades: 
    posicao=cidades.index(nome)
    print("Cidade encontrada! ")
    print("Posição ", posicao)
else:
    print("Cidade não encontrada! ")    