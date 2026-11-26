def avaliar_media(n1, n2, n3): 
    media = (n1+n2+n3)/3
    if media>=7.0: 
        situacao = "Aprovado"
    elif 5.0<=media<=6.9:    
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return "Média: " +str(media)+"-"+situacao
print(avaliar_media(10,10,4))         