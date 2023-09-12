from django.shortcuts import render
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    you_age = forms.CharField(label="Your age", max_length=100)
    you_cash = forms.CharField(label="Your cash", max_length=100)


def first_view(request):
    return render(request, "first_template.html", {'form': NameForm})
