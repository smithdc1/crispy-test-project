# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render


def index(request):
    settings.CRISPY_TEMPLATE_PACK = 'bootstrap4'
    from bootstrap4.forms import HorizontalMessageForm, MessageForm

    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'bootstrap4/index.html',
                  {
<<<<<<< HEAD
                      'default_form': MessageForm(
                          data=request.POST if request.method == "POST" else None,
                          prefix='default_form',
                      ),
                      'horizontal_form': HorizontalMessageForm(
                          data=request.POST if request.method == "POST" else None,
                          prefix='horizontal_form',
                      ),
                      'default_form_failing': MessageForm(
                          data={},
                          prefix='default_form_failing',
                      ),
                      'horizontal_form_failing': HorizontalMessageForm(
                          data={},
                          prefix='horizontal_form_failing',
                      ),
                  })
=======
                      'default_form': MessageForm(),
                      'horizontal_form': HorizontalMessageForm(),
                      'default_form_failing': MessageForm(data={}),
                      'horizontal_form_failing': HorizontalMessageForm(data={}),
                  })
>>>>>>> add bootstrap 4_3
