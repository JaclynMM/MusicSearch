from django.http import HttpResponse
from django.shortcuts import render

from . import forms


def home(request):
    return render(request, 'home.html')


# def search_form_view(request):
#     if request.method == 'POST':
#         form = forms.search_form(request.POST)
#         if form.is_valid():
#             return render(request, artist_name, {'form':form})
#     else:
#         return HttpResponse('We could not locate that search.')


def search_form_view(request):
    search_bar = SearchBar(request, ['name', 'age'])
    if search_bar.is_valid():
        my_name = search_bar['name']