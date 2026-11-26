Temperaturas = []
for x in range(7):
    temp = float(input("digite a temperatura: "))
    Temperaturas.append(temp)
maior = Temperaturas[0]
menor = Temperaturas[0]
soma = 0
for temp in Temperaturas:
    if temp>maior:
        maior = temp
    if temp<menor:
        menor = temp 
    soma = soma + temp 
media = soma/7        
print(f"Maior temperatura: {maior}, menor temperatura: {menor}, Média das temperaturas: {media}")