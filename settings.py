import os


def set_google_token():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + '/vision-processing-key.json'


""" Declarations """
CUSTOM_SEARCH_API_KEY = 'AIzaSyD-p0QypbFADtUYCmxDJpuyM8OhAHP8ETE'
