from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.


class Genres(models.Model):
    genre=models.CharField(max_length=120,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.genre

class Movies(models.Model):
    name=models.CharField(max_length=250,unique=True)
    genres=models.ManyToManyField(Genres,blank=True, null=True)
    year=models.CharField(max_length=200)
    options=(
        ("malayalam","malayalam"),
        ("telungu","telungu"),
        ("thamil","thamil"),
        ("english","english"),
        ("hindi","hindi")
    )
    language=models.CharField(max_length=200,choices=options,default="malayalam")
    runtime=models.FloatField()
    poster_image=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
    @property
    def gener_names(self):
        return self.genres.all()
    # it returs many geners objects

    @property
    def reviews(self):
        return Reviews.objects.filter(movie=self)
    
    @property
    def avg_rating(self):
        rating=Reviews.objects.filter(movie=self).values_list("rating",flat=True)
        if rating:
            return sum(rating)/len(rating)
        return 0
    
class Reviews(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])



    


    


