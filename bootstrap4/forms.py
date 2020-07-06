# -*- coding: utf-8 -*-
import datetime

from django import forms
from django.forms import widgets, modelform_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Column
from crispy_forms.bootstrap import AppendedText, PrependedText, PrependedAppendedText, FormActions, InlineCheckboxes, \
    InlineRadios
from django.utils import timezone

from bootstrap4 import models


class MessageForm(forms.Form):
    text_input = forms.CharField(
        help_text="help on a text_input",
    )
    text_input_a = forms.CharField()
    text_input_b = forms.CharField()
    text_input_c = forms.CharField()

    textarea = forms.CharField(
        widget=forms.Textarea(),
        help_text="help on a textarea",
    )

    radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             "Option two can is something else and selecting it will deselect option one")
        ),
        widget=forms.RadioSelect,
        initial='option_two',
        help_text="help on a radio_buttons",
    )

    inline_radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one', 'option_one'),
            ('option_two', 'option_two')
        ),
        widget=forms.RadioSelect,
        initial='option_two',
        help_text="help on a inline_radio_buttons",
    )

    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             'Option two can also be checked and included in form results'),
            ('option_three',
             'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    inline_checkboxes = forms.MultipleChoiceField(
        choices=(
            ('bird',
             "it's a bird"),
            ('plane',
             "it's a plane"),
            ('dunno',
             "it's something else !")
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="help on a inline_checkboxes",
    )

    grouped_checkboxes = forms.MultipleChoiceField(
        choices=(
            ('Group 1',
                ((1, "Option one"),
                 (2, "Option two"),
                 (3, "Option three"))),
            ('Group 2',
                ((4, "Option four"),
                 (5, "Option five"),
                 (6, "Option six"))),
        ),
        initial=(1,),
        widget=forms.CheckboxSelectMultiple,
        help_text="help on a grouped_checkboxes",
    )

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    appended_text2 = forms.CharField(
        help_text="And a bigger appended text field"
    )

    appended_select = forms.ChoiceField(
        label="Select field with appended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text"
    )

    prepended_appended_select = forms.ChoiceField(
        label="Select field with both preprended and appended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text"
    )

    prepended_select = forms.ChoiceField(
        label="Select field with prepended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
        help_text=(
            'This strange option climbing out of the box is in the examples too '
            'Only without Flexbox '
            'https://v4-alpha.getbootstrap.com/components/forms/#form-controls'),
    )
    datetime_field = forms.SplitDateTimeField(
        initial=timezone.now()
    )
    boolean_field = forms.BooleanField()

    file_field = forms.FileField(
        label="file_field",
        widget=widgets.FileInput(),
        help_text='with widgets.FileInput()'
    )

    file_field_raw = forms.FileField(
        label="file_field_raw",
        help_text='with default widget'
    )

    # Bootstrap4
    helper = FormHelper()
    helper.layout = Layout(
        'text_input_a',
        'text_input_b',
        'text_input_c',
    )
    helper.use_custom_control = True
    helper.form_class = 'form-inline'
    helper.field_template = 'bootstrap4/layout/inline_field.html'

