from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User


class QuoteManager(models.Manager):
    def quote_validation(self,data):
        errors = {}
        if len(data['author']) < 4:
            errors["author"] = "Author's name needs to be at least 4 characters"

        if len(data['message']) < 10:
            errors["message"] = "Message needs to be at least 10 characters"
    
        return errors

    def addfavorites(self, user_id, quote_id):
        f1 = User.objects.get(id = user_id)
        f2 = Quote.objects.get(id = quote_id)
        f2.favorites.add(f1)
        f2.save()

    def removefavorites(self, user_id, quote_id):
        f1 = User.objects.get(id = user_id)
        f2 = Quote.objects.get(id = quote_id)
        f2.favorites.remove(f1)
        f2.save()

class Quote(models.Model):
    user = models.ForeignKey(User, related_name='people')
    author = models.CharField(max_length = 255)
    message = models.TextField(max_length = 1000)
    favorites = models.ManyToManyField(User, related_name='faves') 
    objects = QuoteManager()

# Create your models here.
