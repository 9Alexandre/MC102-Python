tipo_objeto = input()
caractere = input()

# Quadrado
if tipo_objeto == 'Q':
    lado = int(input())
    if lado < 3:
        print("Dimensao invalida.")
    else:
        print(lado * caractere)
        for i in range(0, lado-2):
            print(caractere, (lado-2) * " ", caractere, sep='')
        print(lado * caractere)

# Retangulo
elif tipo_objeto == 'R':
    largura = int(input())
    altura = int(input())
    if largura < 3 or altura < 3:
        print("Dimensao invalida.")
    else:
        print(largura * caractere)
        for i in range(0, altura-2):
            print(caractere, (largura-2) * " ", caractere, sep='')
        print(largura * caractere)

# Triangulo Retangulo
elif tipo_objeto == 'TR':
    altura = int(input())
    if altura < 3:
        print("Dimensao invalida.")
    else:
        print(caractere)
        print(2 * caractere)
        for i in range(1, altura-2):
            print(caractere, i * " ", caractere, sep='')
        print(altura * caractere)

# Triangulo Isosceles
elif tipo_objeto == 'TI':
    altura = int(input())
    if altura < 3:
        print("Dimensao invalida.")
    else:
        base = 2 * altura - 1
        d = base // 2
        print(d * " ", caractere, sep='')
        for i in range(1, altura-1):
           print((d-i) * " ", caractere, (2*i-1) * " ", caractere, sep='')
        print(base * caractere)

# Hexagono
elif tipo_objeto == 'H':
    lado = int(input())
    if altura < 3:
        print("Dimensao invalida.")
    else:
        print((lado-1) * " ", lado * caractere, sep='')
        j = 0
        for i in range(lado-2, -1, -1):
            print(i * " ", caractere, sep='', end='')
            print((j + lado) * " ", caractere, sep='')
            j += 2
        j -= 4
        for i in range(1, lado-1):
            print(i * " ", caractere, sep='', end='')
            print((j+lado) * " ", caractere, sep='')
            j -= 2
        print((lado-1) * " ", lado * caractere, sep='')

# Quadriculado
elif tipo_objeto == 'QQ':
    lado = int(input())
    largura = int(input())
    altura = int(input())
    if lado < 1 or largura < 1 or altura < 1:
        print("Dimensao invalida.")
    else:
        lado_QQ = 1 + largura * (lado-1)
        for i in range(0, altura):
            print(lado_QQ * caractere)
            for j in range(0, lado-2):
                for k in range(0, largura+1):
                    if k == largura:
                        print(caractere)
                    else:
                         print(caractere, (lado-2) * " ", sep='', end='')
        print(lado_QQ * caractere)

# Xadrez
elif tipo_objeto == 'X':
    lado = int(input())
    largura = int(input())
    altura = int(input())
    if lado < 1 or largura < 1 or altura < 1:
        print("Dimensao invalida.")
    else:
        lado_X = 1 + largura * (lado-1)

    for j in range(1, altura+1):
        if j % 2 == 1:
            print(lado_X * caractere)
            for i in range(0, lado - 2):
                print(caractere, end='')
                for k in range(0, largura - 3): # erro aqui, largura - 3 esta incorreto 
                    print((lado - 2) * " ", lado * caractere, sep='', end='')

                if largura % 2 == 0:
                    print((lado - 2) * " ", lado * caractere, sep='')
                else:
                    print((lado - 2) * " ", caractere, sep='')
        else:
            print(lado_X * caractere)
            for i in range(0, lado - 2):
                for k in range(0, largura - 3):
                    print(lado * caractere, (lado - 2) * " ", sep='', end='')

                if largura % 2 == 1:
                    print(lado * caractere, sep='')
                else:
                    print(lado * caractere, (lado - 2) * " ", caractere, sep='')

    print(lado_X * caractere)

else:
   print("Identificador invalido.")
