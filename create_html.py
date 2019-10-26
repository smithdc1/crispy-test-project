from django.test import Client
from bs4 import BeautifulSoup as bs
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
django.setup()

#get html
c = Client()
response = c.get('/bootstrap4')

#make html pretty
soup = bs(response.content)                #make BeautifulSoup
prettyHTML = soup.prettify()

#env variable
print(os.getenv('GITHUB_REF'))
print(os.getenv('GITHUB_SHA'))
print(os.getenv('GITHUB_WORKSPACE'))

#create file name
ref = os.getenv('GITHUB_REF')

if 'pull' in ref:
	start = ref.find(':')+1
	end = ref.find('/',start)
	ref= ref[start:end] + '-'
	print(ref)

else:
	ref = 'push-'

filename = ref + os.getenv('GITHUB_SHA') + '.html'

print(filename)

#make docs folder

os.makedirs(os.getcwd() + '/build/docs/')
path = os.getcwd() + '/build/docs/' + filename
print(path)

with open("path", "w") as file:
    file.write(prettyHTML)

