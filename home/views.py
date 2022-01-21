from django.shortcuts import render
from .models import Article,Sport

# Create your views here.

def article_id(request,id):
    article=Article.objects.get(id=id)
    return render(request,'home/articles.html',{'article':article})

def sports(request):
    sport_data=Sport.objects.all()   
    return render(request,'home/sports.html',{'sports':sport_data})

def home(request):
    articles_data=Article.objects.all()
    nbr_articles=len(articles_data)
    last_article=Article.objects.get(id=nbr_articles)
    data={}
    data['last_article']=last_article
    print(data,nbr_articles)
    for i in range(1,4):
        print(i)
        try:
            data[str(i)]=Article.objects.get(id=nbr_articles-i)
        except:
            print("L'article n'existe pas")
        else:
            pass
    return render(request,'home/home.html',data)