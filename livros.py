from random import randint

def gerador_codigo (pcategoria):
    """Gerador de código para identificação do livro na Base de dados, utilizando como 3 primeiros digitos as iniciais da categoria do livro
    
    param categoria --> Qual a categoria do livro que foi adicionada?"""
    parte1 = pcategoria[:3].upper()
    parte2 = parte3 = ''
    for i in range(3):
        parte2 = str(parte2 + str(randint(0,9)))
    for i in range(3):
        parte3 = parte3 + chr(randint(65, 90))
    return parte1 + parte2 + parte3
    
def cadastrar_livro(parq, pnome, pcodigo, pquantidade):
    """ Inserir dados no arquivo escolhido.
    
    param arq --> nome do arquivo que será editado\n
    param nome --> nome do livro que será cadastrado\n
    param codigo --> codigo do livro a ser cadastrado\n
    param quantidade --> quantidade de livros disponíveis para serem retirados"""
    try:
        a = open(parq, 'at') ## Append text, inserir itens na lista do arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{pnome};{pcodigo};{pquantidade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {pnome} adicionado')
            a.close