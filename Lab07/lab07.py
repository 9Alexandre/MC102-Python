def main():
    notas_ac = [float(x) for x in input().split()]
    notas_lab = [tupla_float_int(x) for x in input().split()]
    prova1, teste, prova2 = map(float, input().split())
    frequencia = float(input())

    aprovado_nota = False
    aprovado_freq = False
    exame = -1

    media_ac = 0
    for i in range(0, 5):
        media_ac += notas_ac[i]
    media_ac /= 5

    media_lab = 0
    pesos = 0
    for i in range(0, len(notas_lab)):
        media_lab += notas_lab[i][0] * notas_lab[i][1]
        pesos += notas_lab[i][1]
    media_lab /= pesos

    media_avaliacoes = (teste + (2 * prova1) + (4 * prova2)) / 7

    print("Media das atividades conceituais:", format(media_ac, ".1f"))
    print("Media das tarefas de laboratorio:", format(media_lab, ".1f"))
    print("Media das avaliacoes escritas:", format(media_avaliacoes, ".1f"))
    print("Frequencia: %.1f%%" %frequencia)

    if frequencia >= 75:
        aprovado_freq = True

        if (media_avaliacoes >= 5) and (media_lab >= 5):
            media_final = (0.6 * media_avaliacoes) + (0.3 * media_lab) + (0.1 *media_ac)
            media_final = max(5, media_final)

            print("Aprovado(a) por nota e frequencia.")

        elif (media_avaliacoes >= 2.5) and (media_lab >= 2.5):
            media_preliminar = (0.6 * media_avaliacoes) + (0.3 * media_lab) + (0.1 *media_ac)
            media_preliminar = min(4.9, media_preliminar)

            exame = float(input())
            media_final = (media_preliminar + exame) / 2

            print("Media preliminar:", format(media_preliminar, ".1f"))
            print("Nota no exame:", format(exame, ".1f"))

            if media_final >= 5:
                print("Aprovado(a) por nota e frequencia.")
            else:
                print("Reprovado(a) por nota.")

        elif (media_avaliacoes < 2.5) or (media_lab < 2.5):
            media_final = min(media_avaliacoes, media_lab)
            print("Reprovado(a) por nota.")
    else:
        media_final = min(media_avaliacoes, media_lab)
        print("Reprovado(a) por frequencia.")

    print("Media final:", format(media_final, ".1f"))



def tupla_float_int(x):
    x = x[1:-1]      # remove parênteses
    x = x.split(",") # separa em duas strings
    f = float(x[0])  # converte primeiro elemento para float
    i = int(x[1])    # converte segundo elemento para int
    return (f,i)     #  retorna tupla

main()
