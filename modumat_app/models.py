from django.db import models


class Module(models.Model):
    shorthand = models.CharField(max_length=20)
    module_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.shorthand}: {self.module_name}"


class Question(models.Model):
    title = models.CharField(max_length=50)
    full_question = models.CharField(max_length=200)

    def __str__(self):
        return self.title
