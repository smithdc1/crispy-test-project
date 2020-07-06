# -*- coding: utf-8 -*-
import os

import errno
from django.conf import settings
from django.shortcuts import render

from bootstrap4.models import WithFileField


def index(request):
    settings.CRISPY_TEMPLATE_PACK = 'bootstrap4'
    from bootstrap4.forms import MessageForm

    filename = '.' + ("/somedire" * 10)
    try:
        os.makedirs(filename)
    except FileExistsError as e:
        assert e.errno is errno.EEXIST
    filename += "/" + ("myfile-" * 1) + ".txt"
    with open(filename, "w") as f:
        f.write('Hello world')
    instance = WithFileField(my_file=filename)

    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'bootstrap4/index.html',
                  {
                      'default_form': MessageForm(
                          data=request.POST if request.method == "POST" else None,
                          prefix='default_form',
                      ),

                  })
