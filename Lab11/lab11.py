import csv
import math

f = open('dados.csv', 'r')
dados = csv.reader(f)

resultado = open("resultado.csv", "w")

A = float(input())
B = float(input())

for linha in dados:

    delta_pressao = round(float(linha[1]) - float(linha[2]), 2)
    ln_pressao_esperada = round(math.log(float(linha[2])), 2)
    AB_T = round(abs(A + (B / float(linha[0]))), 2)
    delta_ln_formula = round(AB_T - ln_pressao_esperada, 2)

    delta_pressao = str(delta_pressao)
    ln_pressao_esperada = str(ln_pressao_esperada)
    AB_T = str(AB_T)
    delta_ln_formula = str(delta_ln_formula)

    saida = '"' + linha[0] + '"' + ',' + '"' + linha[1] + '"' + ',' '"' + linha[2] + '"' + ','
    saida = saida + '"' + delta_pressao + '"' + ','
    saida = saida + '"' + linha[3] + '"' + ','
    saida = saida + '"' + AB_T + '"' + ','
    saida = saida + '"' + delta_ln_formula + '"'

    print(saida)
    print(saida, file=resultado)

f.close()
resultado.close()
