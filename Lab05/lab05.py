moeda = input()
data = input()
valor_compra, valor_venda = map(float, input().split())

valores_compra = list()
valores_venda = list()

min_compra = valor_compra
max_venda = valor_venda

while (valor_compra != 0) and (valor_venda != 0):
    valores_compra.append(valor_compra)
    valores_venda.append(valor_venda)

    if valor_compra < min_compra:
        min_compra = valor_compra
    if valor_venda > max_venda:
        max_venda = valor_venda

    valor_compra, valor_venda = map(float, input().split())

media_5_compra = 0
media_5_venda = 0

for i in range(0, 5):
    media_5_compra = media_5_compra + valores_compra[i]
media_5_compra /= 5

for i in range(0, 5):
    media_5_venda = media_5_venda + valores_venda[i]
media_5_venda /= 5

media_historico_compra = sum(valores_compra) / len(valores_compra)
media_historico_venda = sum(valores_venda) / len(valores_venda)

print("Moeda:", moeda)
print("Data:", data)
print("Valor minimo para compra:", format(min_compra, ".4f"))
print("Valor maximo para venda:", format(max_venda, ".4f"))
print("Medias das cinco cotacoes mais recentes:", format(media_5_compra, ".4f"), format(media_5_venda, ".4f"))
print("Medias do historico:", format(media_historico_compra, ".4f"), format(media_historico_venda, ".4f"))
