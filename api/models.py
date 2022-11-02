from email.policy import default
from django.db import models

# Create your models here.

class Balance(models.Model):
      name = models.CharField(max_length = 300)
      code  = models.CharField(max_length = 300, null=True, blank=True)
      status = models.CharField(max_length = 300)

      def __str__(self):
            return self.name

class Item(models.Model):
      balance = models.ForeignKey(Balance, on_delete = models.CASCADE)
      prize = models.PositiveIntegerField()

      def __str__(self):
            return str(self.prize) + " "+ str(self.balance.name)


class CheckBalance(models.Model):
      actives = models.ManyToManyField(Item, related_name = 'actives', null=True, blank=True)
      passives = models.ManyToManyField(Item, related_name = 'passives', null=True, blank=True)
      total_passives = models.PositiveIntegerField(default=0)            
      total_actives = models.PositiveIntegerField(default=0)
      remainder = models.IntegerField(default=0)   
      is_balanced = models.BooleanField(default=False)   

      def __str__(self):
            return str(self.is_balanced)      