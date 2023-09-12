from django.shortcuts import render
from django import forms


class NameForm(forms.Form):
    field_ = forms.CharField(label="field", max_length=100, required=False,
                             widget=forms.TextInput(attrs={'class': 'field'}))
    operator_ = forms.CharField(label="operator", max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': 'operator'}))
    value_ = forms.CharField(label="value", max_length=100, required=False,
                             widget=forms.TextInput(attrs={'class': 'value'}))


def first_view(request):
    if request.method == 'POST':
        print('si')
        print(request.POST)

    return render(request, "first_template.html", {'form': NameForm})
