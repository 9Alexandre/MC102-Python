# Entrada de dados
peso = float(input())

idade = int(input())
if idade == 16 or idade == 17:
    autorizacao = input()

saude = input()
drogas = input()

primeira_doacao = input()
if primeira_doacao == 'N':
    ultima_doacao = int(input())
    doacoes_12meses = int(input())

sexo = input()
if sexo == 'F':
    gravidez = input()
    amamentando = input()
    if amamentando == 'S':
        idade_bebe = int(input())

# Dados coletados
print("Peso:", peso)
print("Idade:", idade)
if idade == 16 or idade == 17:
    print("Documento de autorizacao:", autorizacao)
print("Boa saude:", saude)
print("Uso drogas injetaveis:", drogas)
print("Primeira doacao:", primeira_doacao)
if primeira_doacao == 'N':
    print("Meses desde ultima doacao:", ultima_doacao)
    print("Doacoes nos ultimos 12 meses:", doacoes_12meses)
print("Sexo biologico:", sexo)
if sexo == 'F':
    print("Gravidez:", gravidez)
    print("Amamentando:", amamentando)
    if amamentando == 'S':
        print("Meses bebe:", idade_bebe)

i = False # impedimento detectado se i = 1
if peso < 50:
    print("Impedimento: abaixo do peso minimo.")
    i=True
if idade < 16:
    print("Impedimento: menor de 16 anos.")
    i=True
if (idade == 16 or idade == 17) and autorizacao == 'N':
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
        i=True
if idade > 60 and primeira_doacao == 'S':
    print("Impedimento: maior de 60 anos, primeira doacao.")
    i=True
if idade > 69:
    print("Impedimento: maior de 69 anos.")
    i=True
if saude == 'N':
    print("Impedimento: nao esta em boa saude.")
    i=True
if drogas == 'S':
    print("Impedimento: uso de drogas injetaveis.")
    i=True
if primeira_doacao == 'N':
    if sexo == 'M':
        if ultima_doacao < 2:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
            i=True
        if doacoes_12meses >= 4:
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
            i=True
    else:
        if ultima_doacao < 3:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
            i=True
        if doacoes_12meses >= 3:
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
            i=1
if sexo == 'F':
    if gravidez == 'S':
        print("Impedimento: gravidez.")
        i=True
    if amamentando == 'S' and idade_bebe < 12:
        print("Impedimento: amamentacao.")
        i=True

if i == False:
    print("Procure um hemocentro para triagem completa.")
