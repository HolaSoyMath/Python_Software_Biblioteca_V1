import os

def linha():
    print('-' * 120)

def sair(popcao='Voltar'):
    """Indicar o que irá aparecer ao lado do submenu opção 0.
    param opcao --> Indicará a frase ao lado da opção 0 (Padrão: Voltar)"""
    print(f'|\033[31m0 . {popcao:<114}\033[m|')
    linha()

def apagar_console():
    print('\n' * os.get_terminal_size().lines)

def cabecalho(ptitulo, psubtitulo=''):
    """Indicar a palavra que ficará como Menu superior ao printar a tela.\n
    param titulo --> Nome que aparecerá no título do cabeçalho
    param subtitulo --> Frase que aparecerá abaixo do título"""
    linha()
    print(f'|{ptitulo.center(118)}|')
    if psubtitulo != '':
        print(f'|{psubtitulo.center(118)}|')
    linha()

def sub_menu(popcoes, pbutton0='Voltar', pindice=True):
    """Indicar os nomes que aparecerão em forma de lista no menu a ser utilizado pelo usuário.\n
    param opcoes --> Todos os sub-menus que aparecerão. (OBS: Para mais de um item, utilizar uma lista com os nomes)\n
    param button0 --> O que aparecerá no submenu ao lado da opção 0. (Padrão: 0. Voltar)\n
    param indice --> Mostrar indice dos numeros. (Padrão: True)"""
    for i, opcao in enumerate(popcoes):
        if pindice == True:
            print(f'|{i+1:<2}. {opcao:<114}|')
        else:
            print(f'|{opcao:<118}|')
    sair(pbutton0)
    if pindice == True:
        while True:
            opcao = int(input('Digite a opção escolhida: '))
            if opcao >= 0 and opcao <= i+1:
                break
            else:
                print('Insira um valor válido!')
        return opcao