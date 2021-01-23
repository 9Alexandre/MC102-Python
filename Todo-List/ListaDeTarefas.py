'''
Modele e construa uma aplicação do tipo TODO List, para armazenar tarefas
diárias de um estudante do ensino médio.

Cada tarefa, necessita ter os seguintes campos :
    - nome;
    - descrição;
    - data de criação;
    - status;
        * Onde o status da tarefa pode ser :
            1. Criada;
            2. Em progresso;
            3. Completa;
            4. Atrasada;
            - data de vencimento;

Como Features da aplicação, teremos:
    -Criar tarefas
    - Remover tarefas
    - Editar tarefas
    - Alterar status individual das tarefas
    - A lterar status em lote
    - Filtrar por status
    - Remover todas as tarefas completas
    - Adiar tarefa
'''

from datetime import datetime
import csv
import os
lista_status = ['Criada', 'Em progresso', 'Completa', 'Atrasada']

# Verifica se a tarefa ja exite na lista
# Se sim, retorna o indice da tarefas
# Se não, retorna -1
def buscar(lista, nome):
    for i in range(0, len(lista)):
        if(nome in lista[i].values()):
            return i
    return -1

# Adiciona um atarefa a lista
def adicionar(lista, nome, descricao, data, status, vencimento):
    tarefa = {'nome': nome, 'descricao': descricao, 'data': data, 'status': status, 'vencimento': vencimento}
    lista.append(tarefa)

# Cria uma tafera
def criar(lista):
    # Solicita o nome e verifica se ja não esta em uso
    nome = input('Nome: ')
    while(buscar(lista, nome) != -1):
        print('Nome já em uso, por favor insira outro nome.')
        nome = input('Nome: ')

    # Solicita a descricao
    descricao = input('Descrição: ')

    # Solicita a data de criacao e verifica se o formato informada e valido
    i = False
    while i == False:
        data = input("Data de criação: ")
        try:
            datetime.strptime(data, '%m/%d/%Y')
            i = True
        except ValueError:
            print("Formato incorreto para data, tente DD/MM/AAAA.")

    # Solicita o status e verifica se e um status valido
    status = input('Status: ')
    while(status not in lista_status):
        print('Status inválido.')
        status = input('Status: ')

    # Solicita a data de vencimento e verifica se o formato informada e valido
    i = False
    while i == False:
        vencimento = input("Data de vencimento: ")
        try:
            datetime.strptime(vencimento, '%m/%d/%Y')
            i = True
        except ValueError:
            print("Formato incorreto para data, tente DD/MM/AAAA.")

    return nome, descricao, data, status, vencimento

# Remove um tarefa da lista
def remover(lista):
  nome = input('Nome da tarefa que será removida: ')
  i = buscar(lista, nome)
  if(i == -1):
    print('Tarefa não encontrada.\n')
  else:
    lista.pop(i)

# Edita todos os campos da tarefa
def editar(lista):
  nome = input('Nome da tarefa que será editada: ')
  i = buscar(lista, nome)
  if(i == -1):
    print('Tarefa não encontrada.\n')
  else:
    nome, descricao, data, status, vencimento = criar(lista)
    lista[i]['nome'] = nome
    lista[i]['descricao'] = descricao
    lista[i]['data'] = data
    lista[i]['status'] = status
    lista[i]['vencimento'] = vencimento

# Altera o status de um tarefa
def alterar_status(lista):
  nome = input('Nome da tarefa que o status será alterado: ')
  i = buscar(lista, nome)
  if(i == -1):
    print('Tarefa não encontrada.')
  else:
    status = input('Novo status: ')
    while(status not in lista_status):
        print('Status inválido.')
        status = input('Status: ')
    lista[i]['status'] = status

# Define o mesmo stayus para varias tarefas
def alterar_varios_status(lista):
    status = input('Novo status: ')
    while(status not in lista_status):
        print('Status inválido.')
        status = input('Status: ')

    nome = input('Insira o nome das tarefas ou 0 para finalizar:\n')
    while(nome != '0'):
        i = buscar(lista, nome)
        if(i == -1):
          print('Tarefa não encontrada.')
        else:
            lista[i]['status'] = status
        nome = input()

# Filtra as tarefas com base no status
def filtrar_status(lista):
    status = input('Insira o status a ser filtrado: ')
    while(status not in lista_status):
        print('Status inválido.')
        status = input('Insira o status a ser filtrado: ')

    for i in range(0, len(lista)):
        if(status in lista[i].values()):
            print(lista[i]['nome'])

# Remver as tarefas que tem status: Completa
def remover_completas(lista):
    for i in range(len(lista)-1, -1, -1):
        if('Completa' in lista[i].values()):
            lista.pop(i)

# Modifica a dava de vencimento de um tarefa
def adiar(lista):
    nome = input('Nome da tarefa que terá a data de vencimento adiada : ')
    i = buscar(lista, nome)
    if(i == -1):
      print('Tarefa não encontrada.')
    else:
        j = False
        while j == False:
            vencimento = input("Data de vencimento: ")
            try:
                datetime.strptime(vencimento, '%m/%d/%Y')
                lista[i]['vencimento'] = vencimento
                j = True
            except ValueError:
                print("Formato incorreto para data, tente DD/MM/AAAA.")

# Exibe as tarefas registradas na tela
def exibir(lista):
    for i in range(0, len(lista)):
        print('Nome: ' + lista[i]['nome'])
        print('Descrição: ' + lista[i]['descricao'])
        print('Data de criação: ' + lista[i]['data'])
        print('Status: ' + lista[i]['status'])
        print('Data de vencimento: ' + lista[i]['vencimento'])
        print()

# Abre e le o arquivo csv que armazena as tarefas
# Transforma os dados listo m um lista
def ler_csv():
    with open('lista-tarefa.csv', 'r') as arq_csv:
        r = csv.reader(arq_csv, delimiter=',')
        lista = list(r)
    arq_csv.close()
    return lista

# Adiciona as modificados no arquivo csv
def escrever_csv(lista_tarefas):
    open('lista-tarefa.csv', 'w').close()
    with open('lista-tarefa.csv', 'a') as arq_csv:
        w = csv.writer(arq_csv, delimiter=',', lineterminator='\n')
        for i in range(0, len(lista_tarefas)):
            w.writerow(lista_tarefas[i].values())
    arq_csv.close()

def main():
    lista_csv = ler_csv()
    lista_tarefas = []

    if len(lista_csv) > 0:
        for i in range(0, len(lista_csv)):
            adicionar(lista_tarefas, lista_csv[i][0], lista_csv[i][1], lista_csv[i][2],
                      lista_csv[i][3], lista_csv[i][4])
    while(1):
        print('-------------------------------------------------------')
        print('TODO List\n')

        print('0 - Sair')
        print('1 - Adicionar tarefa')
        print('2 - Remover tarefa')
        print('3 - Editar tarefa')
        print('4 - Alterar status individual de um tarefa')
        print('5 - Alterar status de várias tarefas')
        print('6 - Filtrar tarefas por status')
        print('7 - Remover todas as tarefas completas')
        print('8 - Adiar tarefa')
        print('9 - Exibir tarefas')

        print('-------------------------------------------------------\n')

        opcao = int(input())
        print()

        if opcao == 0:
            escrever_csv(lista_tarefas)
            break
        elif opcao == 1:
            nome, descricao, data, status, vencimento = criar(lista_tarefas)
            adicionar(lista_tarefas, nome,descricao, data, status, vencimento)
        elif opcao == 2:
            remover(lista_tarefas)
        elif opcao == 3:
            editar(lista_tarefas)
        elif opcao == 4:
            alterar_status(lista_tarefas)
        elif opcao == 5:
            alterar_varios_status(lista_tarefas)
        elif opcao == 6:
            filtrar_status(lista_tarefas)
        elif opcao == 7:
            remover_completas(lista_tarefas)
        elif opcao == 8:
            adiar(lista_tarefas)
        elif opcao == 9:
            exibir(lista_tarefas)
        else:
            print('Opção Inválida\n')

main()
