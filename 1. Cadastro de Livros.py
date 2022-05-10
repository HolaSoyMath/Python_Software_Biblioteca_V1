from menu import *
from livros import *
from basearquivos import *
from usuarios import *
from emprestimos import *

CATEGORIAS_LIVRO = categoria()
MENU_INICIAL = ['Registro Empréstimo','Registro Devolução','Livros com cada usuário', 'Novo Usuário', 'Editar Usuário', 'Lista Usuários', 'Novo livro', 'Editar Livro', 'Consultar Livro', 'Nova Categoria', 'Listar Categorias']
quantidade = 0

while True:
    # Abrir menu inicial com os sub-menus a serem acessados
    apagar_console()
    cabecalho('Menu Inicial')
    escolha = sub_menu(MENU_INICIAL, 'Sair')
    
    # Caso o usuário digite 0 o programa é encerrado
    if escolha == 0:
        break
    
    # Caso o usuário digite 1 o programa irá colocar um novo empréstimo para o usuário
    elif escolha == 1: # Criar um registro de empréstimo
        while True:
            ######### IDENTIFICAÇÃO DO USUÁRIO
            # Como o usuário sera identificado ?
            apagar_console()
            cabecalho('Como deseja identificar o usuário? ')
            resp = sub_menu(['Via ID do usuário', 'Via código do usuário'])
            if resp == 0:
                # Voltar ao menu principal
                break
            # Mostrar a lista dos users
            while True:
                apagar_console()
                cabecalho('Identificar usuário')
                print_usuarios(True)
                if resp == 0:
                    # Voltar ao menu principal
                    break
                elif resp == 1:
                    # Identificar pelo ID
                    id_user = int(input('Qual o ID do usuário? '))
                elif resp == 2:
                    # Identificar pelo Codigo
                    id_user = identificar_user_codigo()
                    if id_user == 0:
                        break
                else:
                    print('Opção Inválida, tente novamente!')
            # Caso digite 0 em algum moneto do processo, volta ao Menu Principal
            if resp == 0 or id_user == 0:
                break
            
            ########## IDENTIFICAÇÃO DO LIVRO
            # Como o livro será identificado ?
            cabecalho('Como deseja identificar o livro ?')
            resp = sub_menu(['Via ID do livro', 'Via código do livro'])
            apagar_console()
            lerArquivoLivros('teste.txt', 'Livros Cadastrados')
            linha()
            if resp == 0:
                break
            elif resp == 1: # Empréstimo via ID
                # Retirar da base dos livros 1 unidade disponível
                resp = int(input('Qual o ID do livro a ser emprestado? '))
                lista_atualizada = emp_dev_ID(resp)
                atualizar_arquivo_emprestimo('teste.txt', lista_atualizada)
                # Sinalizar que o registro foi feito
                print('\033[32mRegistro efetuado!\033[m')
            elif resp == 2: # Empréstimo via Código
                
                
                
                
                
                
                
                
                pass
            else:
                print('Opção inválida, tente novamente!')
                continue
            
            # Emprestar novo livro ?
            while True:
                resp = str(input('Deseja emprestar um novo livro? [S/N] ')).strip().upper()[0]
                if resp in 'S/N':
                    break
                else:
                    print('Digite uma opção válida!')
            # Se nao precisar, voltar ao menu principal
            if resp == 'N':
                break
    
    # Caso o usuário digite 4 o programa ira criar um novo usuario na base de dados
    elif escolha == 4: # Criar um novo usuário
        while True:
            # Apagar console e criar um menu
            apagar_console()
            cabecalho('Novo usuário', 'Cadastrar novo usuário')
            usuarios = cadastrar_usuario()
            # Caso digite 0 volta ao menu principal
            if usuarios == 0:
                break
            # Escrever a nova lista com o novo usuário no arquivo
            else:
                escrever_usuarios(usuarios)
                print('Novo usuário cadastrado com sucesso!')
            # Cadastrar novo usuário ?
            while True:
                resp = str(input('Deseja cadastrar um novo usuário? [S/N] ')).strip().upper()[0]
                if resp in 'S/N':
                    break
                else:
                    print('Digite uma opção válida!')
            # Se nao precisar cadastrar, voltar ao menu principal
            if resp == 'N':
                break
    
    # Caso o usuário digite 5 o programa irá alterar o nome do usuário na base de dados
    elif escolha == 5: # Alterar o nome do usuário
        while True:
            # Criar cabeçalho
            apagar_console()
            cabecalho('Editar nome', 'Indicar o usuário a ser realizada uma alteração')
            print_usuarios(True)
            resp = int(input('Escolha o usuário a ser modificado: '))
            if resp == 0:
                break
            editar_usuario(resp)
            print('\033[32mAlteração efetuada com sucesso!\033[m')
            # Alteração de outro usuário
            while True:
                resp = str(input('Deseja alterar outro usuário? [S/N] ')).strip().upper()[0]
                if resp in 'SN':
                    break
                else:
                    print('Opção inválida, tente novamente!')
            apagar_console()
            if resp == 'N':
                break
                
    # Caso o usuário digite 6 o programa ira listar todos os usuarios cadastrados
    elif escolha == 6: # Listar usuarios cadastrados
        while True:
            # Criar cabeçalho
            apagar_console()
            cabecalho('Usuários cadastrados')
            # printar todos os usuários cadastrados
            print_usuarios()
            while True:
                resp = int(input('Digite "0" para voltar ao menu principal: '))
                if resp == 0:
                    break
            if resp == 0:
                break
        
    # Caso o usuário digite 7 o programa ira criar um novo livro na base de dados
    elif escolha == 7: # Novo Livro
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
    
    # Caso o usuário digite 8 o programa ira modificar um livro na base de dados
    elif escolha == 8: # Editar Livro
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
        
    # Caso o usuário digite 9 o programa ira listar todos os livros presentes na base de dados
    elif escolha == 9: # Consultar Livro
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

    # Caso o usuário digite 10 o programa ira adicionar uma nova categoria de livros
    elif escolha == 10: # Nova categoria
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
    
    # Caso o usuário digite 11 o programa listará todas as categorias que tem cadastro
    elif escolha == 11: # Listar categorias
        apagar_console()
        while True:
            cabecalho('Categorias', 'Lista de todas as categorias cadastradas')
            sub_menu(CATEGORIAS_LIVRO,pindice=False)
            resp = int(input('Digite 0 para voltar ao menu principal: '))
            if resp == 0:
                break
            else:
                print('Opção inválida. Tente novamente!')
        
print('\033[1;31mPrograma encerrado!')
print('Obrigado e volte sempre!\033[m')
