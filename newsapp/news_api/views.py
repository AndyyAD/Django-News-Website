from django.shortcuts import render
import requests

API_KEY = 'my-secret-api-code' # paste your own free api code from news api

def home(request):
    country = 'in'
    category = request.GET.get('category')

    if category:
        url = f'https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)
