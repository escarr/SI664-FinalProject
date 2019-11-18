from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Sport(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE, null=False)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, null=False)
    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=False)
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    seller = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, null=False)
    meetup_spot = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Comment', related_name='comments_owned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sport

class Comment(models.Model) :
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'