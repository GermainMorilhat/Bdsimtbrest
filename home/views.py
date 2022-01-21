from django.shortcuts import render
from .models import Article,Sport

# Create your views here.

def article_id(request,id):
    article=Article.objects.get(id=id)
    articles_data=Article.objects.all()
    other_articles=[]
    id_list=articles_data.values_list('id', flat=True)
    for i in id_list:
        if i==id:
            pass
        else:
            other_articles.append(Article.objects.get(id=i))
    return render(request,'home/articles.html',{'article':article,'other_articles':other_articles})

def sports(request):
    sport_data=Sport.objects.all()   
    return render(request,'home/sports.html',{'sports':sport_data})

def home(request):
    articles_data=Article.objects.all()
    id_list=articles_data.values_list('id', flat=True)
    nbr_articles=len(articles_data)
    last_id=articles_data.latest('id').id
    print(id_list,last_id)
    last_article=articles_data.get(id=last_id)
    data={}
    data['last_article']=last_article
    data['other_articles']={}
    print("test",id_list[nbr_articles-4:nbr_articles-1])
    j=1
    for i in id_list[nbr_articles-4:nbr_articles-1]:
        try:
            data['other_articles'][str(j)]=Article.objects.get(id=i)
            j+=1
        except:
            print("L'article n'existe pas")
        else:
            pass
    print(data)
    return render(request,'home/home.html',data)