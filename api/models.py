from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    city = models.CharField(max_length = 200)
    address = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Vacancy(models.Model):
    company = models.ForeignKey(Company, related_name = "products", on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    salary = models.FloatField()

    def __str__(self):
        return f"{self.name}"
