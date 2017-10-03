import os


def set_google_token():
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + '/vision-processing-key.json'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.path.abspath(__file__)) + \
                                                   '/vision-processing-key.json'


""" Declarations """
CUSTOM_SEARCH_API_KEY = 'AIzaSyD-p0QypbFADtUYCmxDJpuyM8OhAHP8ETE'
MAX_KEYWORD_SEARCH = 5
