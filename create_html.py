from django.test import Client
from bs4 import BeautifulSoup as bs
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
django.setup()


# env variable
# print(os.getenv('GITHUB_REF'))
# print(os.getenv('GITHUB_SHA'))
# print(os.getenv('GITHUB_WORKSPACE'))

def create_filename(pagename):
    # get github ref (reason for workflow)
    ref = os.getenv('GITHUB_REF')

    # if PR then get PR number from string
    if 'pull' in ref:
        start = ref.find(':') + 1
        end = ref.find('/', start)
        ref = ref[start:end] + '-'
        print(ref)

    # if not PR then push
    else:
        ref = 'push-'

    return ref + pagename + '-' + os.getenv('GITHUB_SHA') + '.html'


# make docs folder
try:
    os.makedirs(os.getcwd() + '/build/docs/')
    os.makedirs(os.getcwd() + '/docs/')
except FileExistsError:
    print('folder already exists')


pages = ['boostrap4', 'boostrap3', 'semantic']

for page in pages:
    # get html
    c = Client()
    response = c.get("/" + page)

    # make html pretty
    soup = bs(response.content, "html.parser")  # make BeautifulSoup
    prettyHTML = soup.prettify()

    # set save location
    path = os.getcwd() + '/docs/' + create_filename(page)
    print(path)

    # save html
    with open(path, "w") as file:
        file.write(prettyHTML)
