from django import forms

class SearchArtist(forms.Form):
    name = forms.CharField()


class SearchBand(forms.Form):
    name = forms. CharField()