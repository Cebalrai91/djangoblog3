from django.db import models
from django.utils import timezone

class Post(models.Model):
    KATEGORIE=(('1','planety'),('2','obiekty mgławicowe'),('3','zdarzenia astronomiczne'))
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/car.png')
    rok = models.CharField(null=True, blank=True, max_length=4)
    kategoria = models.CharField(null=True, blank=True, max_length=1, choices=KATEGORIE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def pusta(self):
        pass






