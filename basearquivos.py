from menu import *

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
        
def lerArquivo(pnome, pcabecalho):
    """Mostra todos os itens pertencentes ao Banco de Dados escolhido.\n
    param nome --> Nome do arquivo a ser aberto.\n
    param cabecalho --> Nome que aparecerá no cabeçalho ao verificar todos os itens."""
    try:
        a = open(pnome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho(pcabecalho)
        print(f'|{"ID":<3}{"Nome do Livro":^35}{"Cód. Livro":^15}{"Qntd.":>5}|')
        for i, linha in enumerate(a):
            linha = linha.replace('\n','')
            dado = linha.split(';')
            print(f'|{i + 1:<3}. {dado[0]:^35}{dado[1]:<13}{dado[2]:^5}|')
    finally:
        a.close()
        