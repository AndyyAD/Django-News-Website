from django.shortcuts import render
import requests

API_KEY = '724468afc665447b9a3079447a45dcd5'

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