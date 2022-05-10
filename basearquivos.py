from menu import cabecalho
from livros import alterar_livro

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') ## Read text, nessa def fazemos a verificação se é possivel abrir o arquivo, se for, quer dizer que ele existe
        a.close
    except FileNotFoundError:
        criarArquivo(nome)
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') ## Write Text, escrever o texto (O "+" presente significa que caso o arquivo nao exista, ele pode ser criado)
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
def lerArquivoLivros(pnome, pcabecalho, pretorno=False):
    """Mostra todos os itens pertencentes ao Banco de Dados dos Livros.\n
    param nome --> Nome do arquivo a ser aberto.\n
    param cabecalho --> Nome que aparecerá no cabeçalho ao verificar todos os itens.\n
    param retorno --> Sinalizar se precisa que retorne o número de linhas totais (Padrão é False)"""
    try:
        # ABrir o arquivo escolhido
        a = open(pnome, 'rt')
    except:
        # Caso nao consiga abrir, mostrar um erro
        print('Erro ao ler o arquivo!')
    else:
        # Mostrar cabeçalho
        cabecalho(pcabecalho)
        # No submenu, colocar as categorias de cada coluna
        print(f'|{"ID":^3}{"Nome do Livro":^95}{"Cód. Livro":^15}{"Qntd.":>5}|')
        i = None
        for i, linha in enumerate(a):
            # Para cada linha no arquivo, criar uma lista
            linha = linha.replace('\n','')
            dado = linha.split(';')
            # Printar a lista separada no terminal
            print(f'|{i + 1:<3}. {dado[0]:^95}{dado[1]:<13}{dado[2]:^5}|')
        if pretorno == True:
            # Retornar o numero total de linahs presentes no arquivo
            a.close()
            i = -1 if i is None else i
            return i
    finally:
        a.close()
        
def alterar_arquivo(pescolha, pindice, parquivo, plistaarquivo=''):
    """Alterar alguma informação na base de dados sobre os livros presentes na biblioteca\n
    param escolha --> O que deve ser alterado? (1. Nome, 2. Categoria, 3.Quantidade)\n
    param indice --> Qual o numero equivalente na lista que o usuário digitar ?\n
    param arquivo --> Qual o arquivo que deve ser aberto\n
    param listaarquivo --> Qual a lista de opções a ser chamada (OPCIONAL)"""
    lista_linha = []
    lista_geral = []
    
    # Gerar uma lista com todos os itens incluídos no arquivo
    with open(parquivo, 'r') as arquivo:
        for i, linha in enumerate(arquivo):
            for j in range(2):
                procurar = linha.find(';')
                lista_linha.append(linha[:procurar])
                linha = linha[procurar + 1:]
            linha = linha.replace('\n','')
            lista_linha.append(linha)
            lista_geral.append(lista_linha)
            lista_linha = []
    
    # Alterar o item da lista que o usuário solicitar
    if parquivo == 'Banco Livros.txt':
        resp = alterar_livro(pescolha, plistaarquivo)
    
    # De acordo com o índice e a opção escolhida de alteração, mudar o mesmo na lista
    lista_geral[pindice - 1][pescolha - 1] = resp
    
    # Escrever no arquivo os dados, com a alteração requisitada
    with open(parquivo, 'w') as arquivo:
        for i, registro in enumerate(lista_geral):
            linha = f'{registro[0]};{registro[1]};{registro[2]}'
            if i + 1 == len(lista_geral):
                arquivo.write(linha)
            else:
                arquivo.write(linha + '\n')
        arquivo.write('\n')
        
def categoria():
    # Gera uma lista com todas as categorias no arquivo
    """Gera uma lista com todas as categorias existentes no arquivo Categorias.txt"""
    categorias = []
    with open('Categorias.txt','r', encoding='utf-8') as arquivo:
        for i, linha in enumerate(arquivo):
            linha = linha.replace('\n', '')
            categorias.append(linha)
    return categorias

def adicionar_categoria(pnovacat):
    """Registra uma nova categoria no arquivo Categorias.txt\n
    param novacat --> Qual o nome da nova categoria a ser registrada."""
    categorias = categoria()
    categorias.append(pnovacat)
    with open('Categorias.txt','w', encoding='utf-8') as arquivo:
        for linha in categorias:
            arquivo.write(linha)
            arquivo.write('\n')