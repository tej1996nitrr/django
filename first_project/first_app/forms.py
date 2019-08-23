from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("start with z")
class Formname(forms.Form):
    name = forms.CharField()
    email=forms.EmailField()
    verifyemail =
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    # widget = forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])
