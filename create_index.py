from yattag import Doc
#from bs4 import BeautifulSoup
import os


doc, tag, text = Doc().tagtext()

file_list = os.listdir('/home/runner/build/docs/')
file_list.sort(reverse=True)

with tag('html'):
    with tag('body'):
        with tag('H1'):
            text('Django-crispy-forms')

        for item in file_list:
            with tag('a', href='docs/'+item):
                text(item)
                with tag('br'):
                    text('')


soup = doc.getvalue()

with open('/home/runner/build/index.html', 'w') as file:
    file.write(soup)
