from tech_news.database import find_news


# Requisito 10
def top_5_news():
    sorted_ratings = []

    result = find_news()

    max_count = [x['comments_count'] for x in result]
    sorted_count = sorted(max_count, reverse=True)
    limeted = sorted_count[:5]
    print('comments_count: ', limeted)

    return limeted


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
