ids = input()
ids = ids.split()

rede = []
for i in range(0, len(ids)):
    id = []
    rede.append(id)

while True:
    link = input()
    if link.isdigit():
        n = int(link)
        break
    else:
        x = ord(link[0])
        x -= 65
        print(x)
        rede[x].append(link[5])


for i in range(0, len(rede)):
    if len(rede[i]) > 0:
        print(chr(65+i), "->", rede[i])
    else:
        print(chr(65+i), "-> []")

    print("[] ->", chr(65+i))


    print(rede[i], "->", chr(65+i))
