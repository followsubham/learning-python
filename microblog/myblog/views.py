from django.shortcuts import render
from django.http import HttpResponse
posts=[{
    'author': 'Subham Das',
    'title': 'Blog 1',
    'content': 'First Post Content',
    'published_on': '25-10-2020',
}, {
    'author': 'Baba',
    'title': 'Blog 2',
    'content': 'Second Post Content',
    'published_on': '25-10-2020',
}, {
    'author': 'Ma',
    'title': 'Blog 3',
    'content': 'Third Post Content',
    'published_on': '25-10-2020',
},
]


def home(request):
    context={'posts':posts}
    return render(request, 'myblog/home-index.html', context)

# Create your views here.
