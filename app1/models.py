from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField(unique=True)
    role = models.CharField(max_length=10, default="user")
    tokens = models.JSONField(null=True)  # This will work with SQLite as well

    def __str__(self):
        return self.username

class API(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    endpoint = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    
    # Replacing ArrayField with a Many-to-Many relationship or a simple Integer field
    mapped_users = models.ManyToManyField(User, related_name='mapped_apis', blank=True)

    def __str__(self):
        return self.name