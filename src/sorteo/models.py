from django.db import models

from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True

class Raffle(models.Model):
    email = models.EmailField(max_length=250, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    
    def __str__(self):
        return f'{self.number}: {self.email}'

    class Meta:
        db_table = "raffle"

class TokenEmail(models.Model):
    token = models.CharField(max_length=100, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipped = models.BooleanField(db_index=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "token_email"
