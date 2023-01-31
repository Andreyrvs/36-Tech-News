import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)


# Requisito 12
def analyzer_menu():
    itens = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    choices = {
        "0": get_news,
        "1": get_title,
        "2": get_date,
        "3": get_tag,
        "4": get_category,
        "5": get_top_news,
        "6": get_top_categories,
        "7": get_exit,
    }

    try:
        print(itens)
        choice = input()
        choices[choice]()

    except KeyError:
        print("Opção inválida", file=sys.stderr)


def get_news():
    amount = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(int(amount))


def get_title():
    item = input("Digite o título:")
    return search_by_title(item)


def get_date():
    item = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(item)


def get_tag():
    item = input("Digite a tag:")
    return search_by_tag(item)


def get_category():
    item = input("Digite a categoria:")
    print('item: ', type(item))
    return search_by_category(item)


def get_top_news():
    return top_5_news()


def get_top_categories():
    return top_5_categories()


def get_exit():
    return print("Encerrando script\n")
