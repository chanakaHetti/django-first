from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Lead(models.Model):
    # SOURCE_CHICES = (
    #     ('Newsletter', 'Newsletter'),
    #     ('Google', 'Goole'),
    #     ('Newsletter', 'Newsletter'),
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # CASCADE - if the agent delete then related leads delete
    # SET_NULL - foreign key may be a null value inside the lead table. The we have to define null=True
    # SET_DEFAULT - we can define default value for this agent foreign key inside the lead table


    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.email
