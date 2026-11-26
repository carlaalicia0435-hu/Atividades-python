
temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
soma = 0
for x in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[x]}: "))
    temperaturas.append(temperatura)
    soma = soma + temperatura

media = soma/12
print(f"\nMédia anual: {media}°C")
print("\nTemperaturas acima da média anual:")
for x in range(12):
    if temperaturas[x] > media:
        print(f"{meses[x]}: {temperaturas[x]}°C")
