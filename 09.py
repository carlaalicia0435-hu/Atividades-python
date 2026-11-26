def exibir_perfil(nome, **dados_extras):
    print("Nome: ", nome)
    for chave, valor in dados_extras.items():
        print(chave, ":", valor)
exibir_perfil("Joabe", idade=25,cidade="São Paulo")