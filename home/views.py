from django.shortcuts import render
from .models import Article,Sport

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def article_id(request,id):
    article=Article.objects.get(id=id)
    data={"nom":article.nom,"auteur":article.auteur,"date":article.date,"avatar":"assets"+article.images.url,"description":article.description,"contenu":article.contenu}
    return render(request,'home/articles.html',data)