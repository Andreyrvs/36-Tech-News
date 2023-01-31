# Requisito 12
def analyzer_menu():
    choice = int(input('Selecione uma das opções a seguir: '))
    itens = """
    Selecione uma das opções a seguir: 
    0 - Popular o banco com notícias;
    1 - Buscar notícias por título;
    2 - Buscar notícias por data;
    3 - Buscar notícias por tag;
    4 - Buscar notícias por categoria;
    5 - Listar top 5 notícias;
    6 - Listar top 5 categorias;
    7 - Sair.
    """
    int(input(itens))
    print(itens)
    if choice == 0:
        int(input('Digite quantas notícias serão buscadas:'))


    # choice = int(input('Selecione uma das opções a seguir: '))
    # if choice == 0:
    #     int(input('Digite quantas notícias serão buscadas:'))
    # elif choice == 1:
    #     str(input('Digite o título:'))
    # elif choice == 2:
    #     input('Digite a data no formato aaaa-mm-dd:')
    # elif choice == 3:
    #     input('Digite a tag:')
    # elif choice == 4:
    #     input('Digite a categoria:')
    # elif choice == 5:
    #     input('')
    # elif choice == 6:
    #     input('')
    # elif choice == 7:
    #     input('')