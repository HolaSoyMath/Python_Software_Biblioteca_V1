

def lista_do_arquivo(parquivo):
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

def identificar_user_codigo():
    '''Identificar o usuário pelo seu código e retornar o seu numero no índice do arquivo.\n
    param resp --> '''
    # Looping de verificação
    while True:
        cod_user = str(input('Qual o código do usuário? (Digite 0 para retornar) ')).upper().strip()
        # String com 9 caracteres
        if len(cod_user) == 9:
            break
        # Ao digitar 0, volta ao anterior
        elif cod_user == '0':
            return 0
        else:
            print('Código inválido, tente novamente')
    # Criar uma lista com os dados do arquivo e verificar se o código existe
    lista_geral = lista_do_arquivo('Users.txt')
    for linha in lista_geral:
        if linha[2] == cod_user:
            return int(linha[0])
    # Caso não encontre o usuário na lista, retorna ao menu com a resposta 0
    print('Usuário não encontrado!')
    return 0