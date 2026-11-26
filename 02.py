def carlas_money(dinheiro,compras):
    if(dinheiro>=compras):
        print("Compra bem sucedida" )
    else:
        print(f"compra não sucedida Faltam: {compras - dinheiro} reais")     


dinheiro = float(input("Quanto de dinheiro a Carla tem? "))
compras = float(input("Qual o valor das compras? "))

carlas_money(dinheiro,compras)