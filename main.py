from api.vision import process_image_using_vision_api
from util.search import search_google_using_queries
from settings import set_google_token


def main():
    # set token to run application
    set_google_token()

    # get initial api poll using img
    img_url = ''
    print('searching for the best match for the image in url: {}'.format(img_url))

    resp = process_image_using_vision_api(img_url)
    notes = resp.web_detection

    # list of data to search google for if nothing is a good match
    search_flags = []

    # print entities as they appear
    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved'.format(len(notes.pages_with_matching_images)))
        for page in notes.pages_with_matching_images:
            print('= {}'.format(page.url))
        return

    if notes.full_matching_images:
        print('\n{} Full Matches found: '.format(len(notes.full_matching_images)))
        for image in notes.full_matching_images:
            print('+ {}'.format(image.url))
        return

    if notes.partial_matching_images:
        print('\n{} Partial Matches found: '.format(len(notes.partial_matching_images)))
        for image in notes.partial_matching_images:
            print('- {}'.format(image.url))
        return

    if notes.web_entities:
        for entity in notes.web_entities:
            search_flags.append(entity.description)

    print('no exact matches found, searching google for potential matches ...')

    # no exact matches, search google using first three keywords
    urls_from_search = search_google_using_queries(' '.join(search_flags[:4]))

    print('perhaps one of these URLs is what you were looking for?')
    for url in urls_from_search:
        print('* {}'.format(url))


if __name__ == '__main__':
    main()
