from random import randint
from menu import apagar_console, sub_menu, cabecalho

def gerador_codigo (pcategoria):
    """Gerador de código para identificação do livro na Base de dados, utilizando como 3 primeiros digitos as iniciais da categoria do livro.\n
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
            print(f'Novo registro de \033[32m{pnome}\033[m adicionado')
            a.close
            
def alterar_livro(popcao, plistacategoria=''):
    """Alterar uma informação referente a um livro já cadastrado no sistema.\n
    param opcao --> Indicar a opção escolhida pelo usuário do que alterar.\n
    param listacategoria --> Caso seja alteração de livro, passar a informação de todas as categorias possíveis\n
    return --> Retorna o valor que o usuário escrever ou um novo código."""

    while True:
        if popcao == 0:
            return
        # Alterar o nome do livro
        elif popcao == 1:
            resp = str(input('Qual o novo nome do livro? ')).capitalize()
            break
        # Alterar categoria
        elif popcao == 2:
            while True:
                apagar_console()
                #Chaamar o menu de alteração
                cabecalho('Alterar categoria', 'Alterar a categoria do livro escolhido')
                escolha_cat = sub_menu(plistacategoria)
                # Caso digite 0, volta ao menu anterior
                if escolha_cat == 0:
                    break
                # Se a escolha não estiver entre os valores da lista, pede para que seja inserido um valor válido
                elif escolha_cat < 0 or escolha_cat > len(plistacategoria):
                    print('Opção inválida, tente novamente!')
                    cabecalho('Alterar categoria livro', 'Qual a nova categoria do livro ?')
                else:
                    break
            # Após informar os dados, gera um novo código para o livro retornando o valor para Resp
            resp = gerador_codigo(plistacategoria[escolha_cat - 1])
            break
        # Alterar quantidade
        elif popcao == 3:
            resp = int(input('Qual a quantidade de livros atual ?'))
            break
        else:
            print('Opção Inválida, tente novamente')
    # Retorna o valor escolhido para ser alterado
    return resp