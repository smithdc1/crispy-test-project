from django.test import Client
from BeautifulSoup import BeautifulSoup as bs
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
django.setup()

c = Client()
response = c.get('/bootstrap4')
print(response.content)

soup = bs(response.content)                #make BeautifulSoup
prettyHTML = soup.prettify()
print(prettyHTML)

