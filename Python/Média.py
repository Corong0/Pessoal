
def media():

    lista_notas = []
    q_notas = int(input("Quantas notas para a conta? "))
    
    for i in range(q_notas):
        notas = float(input(f"Digite sua {i + 1} nota: "))
        lista_notas.append(notas)

    media_final = sum(lista_notas) / q_notas
    print(f"Sua média é: {media_final:.2f}")
    
media()