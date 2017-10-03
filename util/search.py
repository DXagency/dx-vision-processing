from lib.gsearch import search, search_images


def search_google_using_queries(list_of_queries, limit=5):
    """
    Search google using list of terms, return first n number
    :param list_of_queries:
    :param limit:
    :return:
    """
    return list(search(list_of_queries, stop=limit, only_standard=True))
