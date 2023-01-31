import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category
)


# Requisito 12
def analyzer_menu():

    itens = """
    Selecione uma das opções a seguir:\n
    0 - Popular o banco com notícias;\n
    1 - Buscar notícias por título;\n
    2 - Buscar notícias por data;\n
    3 - Buscar notícias por tag;\n
    4 - Buscar notícias por categoria;\n
    5 - Listar top 5 notícias;\n
    6 - Listar top 5 categorias;\n
    7 - Sair.\n
    """
    try:
        print(itens)
        choice = input()
        if choice == '0':
            amount = input('Digite quantas notícias serão buscadas:')
            get_tech_news(int(amount))
        elif choice == '1':
            str(input('Digite o título:'))
        elif choice == '2':
            input('Digite a data no formato aaaa-mm-dd:')
        elif choice == '3':
            input('Digite a tag:')
    except KeyError:
        print("Opção inválida", file=sys.stderr)



def category(param):
    if param == '4':
        input('Digite a categoria:')

    # elif choice == 5:
    #     input('')
    # elif choice == 6:
    #     input('')
    # elif choice == 7:
    #     input('')