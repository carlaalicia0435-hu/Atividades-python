def somar_todos(*numeros):
    soma = 0
    for numero in numeros:
        soma+=numero 
    return soma 
print(somar_todos(8,8,8))
print(somar_todos(5,5,5,9))
print(somar_todos())