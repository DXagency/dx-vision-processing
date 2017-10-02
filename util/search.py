from lib.gsearch import search


def search_google_using_queries(list_of_queries, limit=5):
    """
    Search google using list of terms, return first n number
    :param list_of_queries:
    :param limit:
    :return:
    """
    search_urls = list(search(list_of_queries, stop=limit))
    # for url in search_urls:
    #     print(url)
    return search_urls
