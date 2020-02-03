def main():

    diagrama_entrada = []
    while True:
        linha = input()
        if linha.isdigit():
            n = int(linha)
            break
        else:
            linha = linha.split()
            diagrama_entrada.append(linha)

    palavras = []
    quantidade = []
    for i in range(0, n):
        linha = input()
        palavras.append(linha)
        quantidade.append(0)

    # Inicializa diagrama de saida
    diagrama_saida = []
    for i in range(0, len(diagrama_entrada)):
        linha = []
        for j in range(0, len(diagrama_entrada[i])):
            linha.append(".")
        diagrama_saida.append(linha)

    for i in range(0, len(palavras)):
        busca_horizontal(diagrama_entrada, palavras[i], diagrama_saida, quantidade, i)
        busca_vertical(diagrama_entrada, palavras[i], diagrama_saida, quantidade, i)
        busca_diagonal(diagrama_entrada, palavras[i], diagrama_saida, quantidade, i)

    for i in range(0, len(diagrama_saida)):
        for j in range(0, len(diagrama_saida[i])):
            print(diagrama_saida[i][j], " ", end='', sep='')
        print()

    palavras_alfabetica = sorted(palavras)
    for i in range(0, len(palavras)):
        for j in range(0, len(palavras)):
            if palavras_alfabetica[i] == palavras[j]:
                print(palavras_alfabetica[i], ": ", quantidade[j], sep='')


def busca_horizontal(diagrama, palavra, diagrama_saida, quantidade, n):
    palavra_inversa = palavra[::-1]
    for i in range(0, len(diagrama)):
        linha = ''.join(diagrama[i])
        idx1 = linha.find(palavra)
        idx2 = linha.find(palavra_inversa)
        if idx1 != -1:
            x = len(palavra)
            diagrama_saida[i][idx1:idx1+x] = palavra
            quantidade[n] += 1
        if idx2 != -1:
            x = len(palavra)
            diagrama_saida[i][idx2:idx2+x] = palavra_inversa
            quantidade[n] += 1

def busca_vertical(diagrama, palavra, diagrama_saida, quantidade, n):
    linha = ""
    palavra_inversa = palavra[::-1]
    for j in range(0, len(diagrama[0])):
        for i in range(0, len(diagrama)):
            linha = linha + diagrama[i][j]
        idx1 = linha.find(palavra)
        idx2 = linha.find(palavra_inversa)
        if idx1 != -1:
            for k in range(0, len(palavra)):
                diagrama_saida[idx1][j] = palavra[k]
                idx1 += 1
            quantidade[n] += 1
        if idx2 != -1:
            for k in range(0, len(palavra)):
                diagrama_saida[idx2][j] = palavra_inversa[k]
                idx2 += 1
            quantidade[n] += 1
        linha = ""


def busca_diagonal(diagrama, palavra, diagrama_saida, quantidade, n):
    linha = ""
    for i in range(0, len(diagrama)):
        linha = linha + diagrama[i][i+1]

    print(linha)

# Terminar isso





































main()
