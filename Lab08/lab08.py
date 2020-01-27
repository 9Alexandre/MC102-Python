# Entrada do texto
texto = input()
while True:
    linha = input()
    if linha:
        if linha[0] == '-':
            break
        else:
            texto = texto + " " + linha

# Entrada dos prefixos
prefixos = []
while True:
    linha = input()
    if linha[0] == '-':
        break
    else:
        prefixos.append(linha.lower())

# Converte todo o texto para letras minusculas
texto = texto.lower()

# Converte o texto para uma lista de palavras
texto = texto.split()

# Remove potuacao do final e do inicio das palavras que tiverem
for i in range(0, len(texto)):
    if len(texto[i]) > 1:
        if (ord(texto[i][-2]) < 97) or (ord(texto[i][-2]) > 122):
            texto[i] = texto[i].replace(texto[i][-2], "")

    if (ord(texto[i][-1]) < 97) or (ord(texto[i][-1]) > 122):
        texto[i] = texto[i].replace(texto[i][-1], "")
    if (ord(texto[i][0]) < 97) or (ord(texto[i][0]) > 122):
        texto[i] = texto[i].replace(texto[i][0], "")

# Remove hifens e transforma a palavras em duas
for i in range(0, len(texto)):
    j = texto[i].find("-")
    if j != -1:
        k = len(texto[i])
        texto.append(texto[i][j+1:k])
        texto[i] = texto[i].replace(texto[i][j:k], "")

vocabulario = {}
frequencia = {}

for i in range(0, len(texto)):
    primeira_letra = texto[i][0]

    if vocabulario.get(primeira_letra) == None:
        lista = [texto[i]]
        f = [1] # Inicializa a frequencia de cada palavra que tem sua inicial encontrada pela primeira vez
        vocabulario[primeira_letra] = lista
        frequencia[primeira_letra] = f
    else:
        lista = vocabulario.get(primeira_letra)
        f = frequencia.get(primeira_letra)
        repetido = False
        for j in range(0, len(lista)):
            if lista[j] == texto[i]:
                repetido = True
                f[j] = f[j] + 1
                break
        if repetido == False:
            lista.append(texto[i])
            f.append(1)

print("Vocabulario:")
for i in range(ord('a'), ord('z')+1):
    lista = vocabulario.get(chr(i))
    freq = frequencia.get(chr(i))
    if lista != None:
        lista_alfabetica = sorted(lista)
        for j in range(0, len(lista)):
            print(lista_alfabetica[j], " ", end='', sep='')
            for k in range(0, len(lista)):
                if lista_alfabetica[j] == lista[k]:
                    print("(", freq[k], ")", sep='')
                    break

print("Sugestoes:")
for i in range(0, len(prefixos)):
    lista = vocabulario.get(prefixos[i][0])
    print(prefixos[i], ":", sep='', end='')
    if lista != None:
        lista_alfabetica = sorted(lista)
        for j in range(0, len(lista)):
            tam = len(prefixos[i])
            if lista_alfabetica[j][0:tam] == prefixos[i] and lista_alfabetica[j] != prefixos[i]:
                print(" ", lista_alfabetica[j], sep='', end='')
    print()
