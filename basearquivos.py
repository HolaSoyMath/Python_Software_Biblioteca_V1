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