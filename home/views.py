from django.shortcuts import render
from .models import Article,Sport

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def article_id(request,id):
    article=Article.objects.get(id=id)
    return render(request,'home/articles.html',{'article':article})

def sports(request):
    sport_data=Sport.objects.all()   
    return render(request,'home/sports.html',{'sports':sport_data})
