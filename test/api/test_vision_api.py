import pytest

from api.vision import process_image_using_vision_api
from settings import set_google_token


@pytest.fixture()
def g_token():
    """ set google auth token for test suite """
    set_google_token()


def test_parse_image_using_vision_api(g_token):
    # url = 'https://github.com/identicons/adamperez.png'
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/gnc_blender_bottle.jpg'   # blender bottle
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/ketchup_in_hand.jpg'   # ketchup bottle no hand
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/dirty_converse.jpg'   # converse shoe
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/welchs_fruit_snacks.jpg'  # welchs fruit snacks
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/welchs_fruit_rolls.jpg'  # welchs fruit snacks (full match)
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/hershey_box.jpg'   # hershey's box
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/black_ice.jpg'   # black ice air freshener
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/scuplt_mouse.jpg'
    url = 'https://storage.googleapis.com/dx-vision-image-bucket/spidey.jpg'
    # url = 'https://storage.googleapis.com/dx-vision-image-bucket/heat_patches.jpg'

    resp = process_image_using_vision_api(url)
    notes = resp.web_detection

    # print entities as they appear
    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved'.format(len(notes.pages_with_matching_images)))

        for page in notes.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if notes.full_matching_images:
        print('\n{} Full Matches found: '.format(len(notes.full_matching_images)))

        for image in notes.full_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.partial_matching_images:
        print('\n{} Partial Matches found: '.format(len(notes.partial_matching_images)))

        for image in notes.partial_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.web_entities:
        print('\n{} Web entities found: '.format(len(notes.web_entities)))

        for entity in notes.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))
