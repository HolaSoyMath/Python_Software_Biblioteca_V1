from menu import *
from livros import *
from basearquivos import *

CATEGORIAS_LIVRO = categoria()
MENU_INICIAL = ['Registro Empréstimo','Registro Devolução', 'Novo Usuário', 'Editar Usuário', 'Lista Usuários', 'Novo livro', 'Editar Livro', 'Consultar Livro', 'Nova Categoria', 'Listar Categorias']
quantidade = 0

while True:
    # Abrir menu inicial com os sub-menus a serem acessados
    apagar_console()
    cabecalho('Menu Inicial')
    escolha = sub_menu(MENU_INICIAL, 'Sair')
    
    # Caso o usuário digite 0 o programa é encerrado
    if escolha == 0:
        break
    # Caso o usuário digite 6 o programa ira criar um novo livro na base de dados
    elif escolha == 6: # Novo Livro
        while True: 
            apagar_console()
            cabecalho('Registro novo livro', 'Qual a categoria do novo livro ?') # Construir o cabeçalho
            while True: 
                
                # Escolha de categoria do livro
                escolha_cat = sub_menu(CATEGORIAS_LIVRO)
                if escolha_cat == 0:
                    break
                elif escolha_cat < 0 or escolha_cat > len(CATEGORIAS_LIVRO):
                    print('Opção inválida, tente novamente!')
                    cabecalho('Registro novo livro', 'Qual a categoria do novo livro ?')
                else:
                    break
            if escolha_cat ==0:
                apagar_console()
                break
            
            # Escolher as informações referentes ao livro
            nome_livro = str(input('Qual o nome do livro ? ')).capitalize()
            codigo_livro = gerador_codigo(CATEGORIAS_LIVRO[escolha_cat - 1])
            quantidade = int(input('Quantidade de livros disponíveis: '))
            apagar_console()
            print(f'O código gerado para o livro é: \033[33m{codigo_livro}\033[m')
            
            # Verificação, criação e alteração do arquivo da Base de dados
            arquivoExiste('Banco Livros.txt')
            cadastrar_livro('Banco Livros.txt', nome_livro, codigo_livro, quantidade)
            
            # Registro de um novo livro
            while True:
                resp = str(input('Deseja cadastrar um novo livro ? [S/N] ')).strip().upper()[0]
                if resp in 'SN':
                    break
                else:
                    print('Opção inválida, tente novamente!')
            apagar_console()
            if resp == 'N':
                break
    
    # Caso o usuário digite 7 o programa ira modificar um livro na base de dados
    elif escolha == 7:
        while True:
            # Escrever o menu de opções de todos os livros na base de dados
            apagar_console()
            tamanho = lerArquivoLivros('Banco Livros.txt', 'Editar Livro', True) + 1
            sair()
            # Escolher o livro a ser editado
            resp = int(input('Qual o livro a ser editado? '))
            # Voltar ao menu anterior
            if resp == 0:
                break
            # Abrir um novo menu solicitando "O que será alterado ?"
            elif resp >= 1 and resp <= tamanho:
                apagar_console()
                cabecalho('Editar Livro', 'Escolha o que deve ser alterado')
                escolha = sub_menu(['Alterar Nome', 'Alterar Categoria', 'Alterar Quantidade'])
                alterar_arquivo(escolha, resp, 'Banco Livros.txt', CATEGORIAS_LIVRO)
                # Voltar ao menu anterior e listar novamente todos os livros
                if escolha == 0:
                    continue
                print('Alteração efetuada com sucesso!')
                # Perguntar se deseja alterar outro item
                while True:
                    resp = str(input('Deseja alterar outro item? [S/N] ')).upper().strip()[0]
                    if resp in 'SN':
                        break
                    else:
                        print('Opção inválida, tente novamente!')
                apagar_console()
                # Resposta positiva, listar novamente todos os livros, caso negativo, listar o menu principal novamente
                if resp == 'N':
                    break
            else:
                print('Opção inválida, tente novamente!')
        
    # Caso o usuário digite 8 o programa ira listar todos os livros presentes na base de dados
    elif escolha == 8:
        while True:
            apagar_console()
            # Ler todos os livros presentes na Base de Dados
            lerArquivoLivros('Banco Livros.txt', 'Livros Cadastrados')
            linha()
            # Opção para voltar ao menu principal
            resp = int(input('Para voltar ao menu principal digite 0: '))
            apagar_console()
            if resp == 0:
                break
            else:
                print('Opção inválida, tente novamente!')

    # Caso o usuário digite 9 o programa ira adicionar uma nova categoria de livros
    elif escolha == 9:
        while True:
            apagar_console()
            # Indicar a ação a ser feita no cabeçalho
            cabecalho('Adicionar categoria', 'Registrar nova categoria de livros')
            resp = str(input('Qual o nome da nova categoria? (Digite "0" para retornar ao menu anterior) ')).strip().capitalize()
            # Verificar se a resposta é um valor numerico
            if resp.isnumeric() == True:
                if float(resp) == 0.0:
                    break
                else:
                    continue
            # Verificar se o usuário quer voltar ao menu anterior
            elif resp == 'Voltar':
                break
            # Adicionar a categoria informada anteriormente no arquivo Categorias.txt
            else:
                adicionar_categoria(resp)
                print(f'A categoria \033[32m{resp}\033[m foi adicionada com sucesso!')
            # Verificar se o usuário deseja adicionar outra categoria
            while True:
                resp = str(input('Deseja registrar uma nova categoria? [S/N] ')).strip().capitalize()[0]
                if resp not in 'SN':
                    continue
                else:
                    break
            if resp == 'N':
                break
        # Atualizar a lista de Categorias presentes no sistema
        CATEGORIAS_LIVRO = categoria()
    
    # Caso o usuário digite 10 o programa listará todas as categorias que tem cadastro
    elif escolha == 10:
        apagar_console()
        while True:
            cabecalho('Categorias', 'Lista de todas as categorias cadastradas')
            sub_menu(CATEGORIAS_LIVRO,pindice=False)
            resp = int(input('Digite 0 para voltar ao menu principal: '))
            if resp == 0:
                break
            else:
                print('Opção inválida. Tente novamente!')
        
print('Programa encerrado!')
print('Obrigado e volte sempre!')
