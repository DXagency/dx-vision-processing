from util.search import search_google_using_queries


def test_google_search_by_keyword():
    q = 'Heinz, Ketchup, Heinz Tomato Ketchup'
    l = search_google_using_queries(q)
    for i in l:
        print(i)
