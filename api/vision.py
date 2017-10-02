from google.cloud import vision
from google.cloud.vision import types


def process_image_using_vision_api(uri):
    """
    Send image from public URL through Google Vision API; to get image info capture `web_detection` from
    response

    Types of data from `web_detection`:
    - `pages_with_matching_images`: webpage where image appears
    - `full_matching_images`: exact match of actual image
    - `partial_matching_images`: partial image match
    - `web_entities`: tags that Google has provided about the image
    :param uri:
    :return:
    """
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    return client.web_detection(image=image)
