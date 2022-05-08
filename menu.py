import os

def linha():
    print('-' * 60)

def sair(popcao='Voltar'):
    """Indicar o que irá aparecer ao lado do submenu opção 0.
    param opcao --> Indicará a frase ao lado da opção 0 (Padrão: Voltar)"""
    print(f'|0. {popcao:<55}|')
    linha()

def apagar_console():
    print('\n' * os.get_terminal_size().lines)

def cabecalho(ptitulo, psubtitulo=''):
    """Indicar a palavra que ficará como Menu superior ao printar a tela.\n
    param titulo --> Nome que aparecerá no título do cabeçalho
    param subtitulo --> Frase que aparecerá abaixo do título"""
    linha()
    print(f'|{ptitulo.center(58)}|')
    if psubtitulo != '':
        print(f'|{psubtitulo.center(58)}|')
    linha()

def sub_menu(popcoes, pbutton0='Voltar'):
    """Indicar os nomes que aparecerão em forma de lista no menu a ser utilizado pelo usuário.\n
    param opcoes --> Todos os sub-menus que aparecerão. (OBS: Para mais de um item, utilizar uma lista com os nomes)\n
    param button0 --> O que aparecerá no submenu ao lado da opção 0."""
    for i, opcao in enumerate(popcoes):
        tamanho = 60 - len(str(i + 1)) - 4
        print(f'|{i+1}. {opcao:<{tamanho}}|')
    sair(pbutton0)
    while True:
        opcao = int(input('Digite a opção escolhida: '))
        if opcao >= 0 and opcao <= i+1:
            break
        else:
            print('Insira um valor válido!')
    return opcao