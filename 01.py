def saudar(nome, periodo="dia"):
    if periodo == "dia":
        print("Bom dia, ", nome)
    elif periodo == "tarde":
        print("Boa tarde, ", nome)
    elif periodo == "noite":
        print("Boa noite, ", nome)
saudar("Maria")
saudar("João","tarde")
saudar("Ana","noite")
