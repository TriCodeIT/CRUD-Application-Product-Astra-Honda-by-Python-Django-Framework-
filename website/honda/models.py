from django.db import models

# Create your models here.

class Product(models.Model):
    genre_choices = (
        ('Matic', 'Matic'),
        ('Bebek', 'Bebek'),
        ('Sport', 'Sport'),
        ('BigBike', 'BigBike'),
    )
    product = models.CharField(max_length=50)
    genre = models.CharField(max_length=25, choices=genre_choices, default='Pop')
    color = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return self.product