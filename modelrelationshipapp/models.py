from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    book_name = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)
    book_publish_date = models.DateField()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=20)
    post_category = models.CharField(max_length=20)
    post_publish_date = models.DateField()


class Dance(models.Model):
    user = models.ManyToManyField(User)
    dance_name = models.CharField(max_length=20)
    dance_duration = models.CharField(max_length=20)

    def dance_by(self):
        return ",".join([str(d) for d in self.user.all()])
