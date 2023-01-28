from tech_news.database import find_news


# Requisito 10
def top_5_news():
    sorted_ratings = []

    result = find_news()
    print('result: ', result)
    for doc in find_news():
        # doc['comments_count'].sort(revense=True)
        sorted_ratings.append({doc["title"], doc["url"], doc['comments_count']})
        # print(doc['comments_count'])

    # print(sorted(sorted_ratings, key=sorted_ratings['comments_count']))
    # list_tuple = []
    # for element in result:
    #     # sorted_ratings.append(element["comments_count"])
    #     # sorted_ratings.
    #     # if sorted_ratings == element["comments_count"]:
    #     # list_tuple.append((element["title"], element["url"]))
    #     sorted(result, key=element["comments_count"], reverse=True)
    #     print('list_tuple: ',
    #         sorted(result, key=element["comments_count"], reverse=True)
    #     )

    # for element in result:
    #     list_tuple.append((element["title"], element["url"]))
    return list_tuple


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
