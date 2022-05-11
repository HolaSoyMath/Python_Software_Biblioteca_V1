

def lista_do_arquivo(parquivo, psplit=True):
    '''Retorna o valor em formato de lista, todas as linhas do arquivo selecionado.\n
    param arquivo --> Nome do arquivo txt.\n
    return -- > lista de todos os itens.'''
    lista_geral = []
    with open(parquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.replace('\n', '')
            lista_linha = linha.split(';')
            lista_geral.append(lista_linha)
    return lista_geral

def emp_dev_ID(presp, pemp=True):
    '''Modificar quantidade de livros disponiveis no banco de dados atraves do empréstimo via ID do livro.\n
    param resp --> Resposta dada pelo usuário informando que a localização do livro será feita via ID livro.\n
    param emp --> Se for Empréstimo: True.\n
                              Se for Devolução: False.\n
    return --> retorna uma lista com o livro atualizado em -1 ou +1 unidade disponível.'''
    presp -= 1
    lista_geral = lista_do_arquivo('teste.txt')
    for i, registro in enumerate(lista_geral):
        if i == presp:
            if pemp == True:
                registro[2] = int(registro[2]) - 1
            if pemp == False:
                registro[2] = int(registro[2]) + 1
            break
    return lista_geral
    
def atualizar_arquivo_emprestimo(parquivo, plista):
    '''Atualizar o arquivo com a lista que a def receber como parâmetro.\n
    param arquivo --> Nome do arquivo a ser editado.\n
    param lista --> Lista a ser inserida no arquivo.'''
    with open(parquivo, 'w') as arquivo:
        for linha in plista:
            arquivo.write(f'{linha[0]};{linha[1]};{linha[2]}\n')

def identificar_ID_via_codigo(parquivo, ptexto):
    '''Identificar o usuário pelo seu código e retornar o seu numero no índice do arquivo.\n
    param arquivo --> Qual o nome do arquivo a ser criada a lista.\n
    param texto --> Qual o texto que aparecerá na pergunta.'''
    # Looping de verificação
    while True:
        codigo = str(input(f'Qual o código do {ptexto}? (Digite 0 para retornar) ')).upper().strip()
        # String com 9 caracteres
        if len(codigo) == 9:
            break
        # Ao digitar 0, volta ao anterior
        elif codigo == '0':
            return 0
        else:
            print('Código inválido, tente novamente')
    # Criar uma lista com os dados do arquivo e verificar se o código existe
    lista_geral = lista_do_arquivo(parquivo)
    for i, linha in enumerate(lista_geral):
        if ptexto == 'Usuário':
            if linha[2] == codigo:
                return int(linha[0])
        elif ptexto == 'Livro':
            if linha[1] == codigo:
                return i + 1
    # Caso não encontre o usuário na lista, retorna ao menu com a resposta 0
    print(f'\033[33m{ptexto} não encontrado!\033[m')
    return -1

def registrar_emprestimo(piduser, pidlivro):
    lista_separada = []
    with open('Livros emprestados.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.replace('\n', '')
            linha = linha.split(';')
            lista_separada.append(linha)
    if len(lista_separada) == 0:
        lista_separada.append([f'{piduser}',f'{pidlivro},'])
    else:
        for i, linha in enumerate(lista_separada):
            if int(linha[0]) == piduser:
                lista_livros = linha[1].split(',')
                for j in lista_livros:
                    if j == str(pidlivro):
                        return 1
                lista_separada[i][1] = f'{lista_separada[i][1]}{pidlivro},'
                break
            elif i+1 == len(lista_separada):
                lista_separada.append([f'{piduser}',f'{pidlivro},'])
                break
    with open('Livros emprestados.txt', 'w') as arquivo:
        for linha in lista_separada:
            arquivo.write(f'{linha[0]};{linha[1]}\n')
    return 2
    
def atualizar_livros_emprestados(plista):
    '''Escreve os itens da lista no arquivo de "Livros emprestados".\n
    param lista --> lista de itens a serem cadastrados.'''
    with open('Livros emprestados.txt', 'w') as arquivo:
           for linha in plista:
               arquivo.write(f'{linha}\n')

