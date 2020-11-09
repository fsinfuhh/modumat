from django.db import models


class Module(models.Model):
    shorthand = models.CharField(max_length=20)
    module_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.shorthand}: {self.module_name}"
