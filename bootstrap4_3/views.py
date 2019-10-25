# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render


def index(request):
    settings.CRISPY_TEMPLATE_PACK = 'bootstrap4'
    from bootstrap4_3.forms import HorizontalMessageForm, MessageForm, SampleForm

    form = SampleForm()
    form.fields['is_company'].label = False
    form.fields['email'].label = False
    form.fields['password1'].label = False
    form.fields['password2'].label = False
    form.fields['first_name'].label = False
    form.fields['last_name'].label = False
    form.fields['datetime_field'].label = False

    del form.fields['is_company']



    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'bootstrap4_3/index.html',
                  {
                      'default_form': SampleForm,
                      'horizontal_form': HorizontalMessageForm(),
                      'default_form_failing': MessageForm(data={}),
                      'horizontal_form_failing': HorizontalMessageForm(data={}),
                  })