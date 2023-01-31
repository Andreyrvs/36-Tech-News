from tech_news.database import find_news


# Requisito 10
def top_5_news():
    result = find_news()

    # /**
    # Source:
    # https://stackoverflow.com/a/73050/17053855
    # */
    sort_title = sorted(result, key=lambda result: result['title'])
    sort_comments = sorted(
        sort_title,
        key=lambda sort_title: sort_title['comments_count'],
        reverse=True
    )
    limited_newlist = sort_comments[:5]

    # /**
    # * Consultei o repositório do
    # Lucas Dalbo (Lucas-Dalbo) para resolver essa parte.
    # * Link do repositório:
    # * https://github.com/tryber/sd-020-a-tech-news/pull/2
    # */
    list_tuple = [(item["title"], item["url"]) for item in limited_newlist]

    return list_tuple


# Requisito 11
def top_5_categories():
    result = find_news()
    compre = [item["category"] for item in result]

    counts = {}
    for item in compre:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    new_counts = []
    # /**
    # Source:
    # https://diegomariano.com/como-ordenar-um-dicionario-em-python/
    # */
    for i in sorted(counts, key=counts.get, reverse=True):
        new_counts.append(i)
        # print(i, counts[i])

    a = new_counts
    print('\na: ', a)
    return a
