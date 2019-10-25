from django.test import Client
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
django.setup()
 
c = Client()
response = c.get('/bootstrap4')
print(response.content)
 
 
 
