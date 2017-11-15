from django import forms


class ArtistForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    hometown = forms.CharField(max_length=150)
    twitter_id = forms.CharField(max_length=150)


class BandForm(forms.Form):
    members = forms.CharField(max_length=150)
    name = forms.CharField(max_length=150)
    genre = forms.CharField(max_length=150)
    start_date = forms.DateField()
    end_date = forms.DateField()
    hometown = forms.CharField(max_length=150)
    website = forms.URLField()
    twitter_id = forms.CharField(max_length=150)


class AlbumForm(forms.Form):
    band = forms.CharField(max_length=150)
    name = forms.CharField(max_length=150)
    create_date = forms.DateField()

