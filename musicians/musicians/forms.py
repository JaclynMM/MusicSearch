from django import forms


class search_form(forms.Form):
    artist_name = forms.CharField(label='Artist', max_length=100)
    band_name = forms.CharField(label='Band', max_length=100)
