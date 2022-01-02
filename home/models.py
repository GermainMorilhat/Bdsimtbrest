from django.db import models


# Create your models here.
class Sport(models.Model):
    nom=models.CharField(max_length=60)
    professeur=models.CharField(max_length=60)
    president= models.CharField(max_length=60)
    horaire = models.CharField(max_length=300,default='')
    description=models.CharField(max_length=500,default='')
    avatar= models.ImageField(upload_to='avatars',default='avatar.png')
    animation= models.ImageField(upload_to='avatars',default='avatar.png')
    lien=models.CharField(max_length=1000)

    def __str__(self):
        return str(self.nom)

class Article(models.Model):
    nom=models.CharField(max_length=60)
    auteur=models.CharField(max_length=60)
    description=models.CharField(max_length=500,default='')
    images= models.ImageField(upload_to='article_images',default='images.png')
    contenu=models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.nom)



