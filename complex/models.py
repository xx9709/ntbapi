from django.db import models

class Complex(models.Model):
    name = models.CharField(max_length=255)

class Block(models.Model):
    complex = models.ForeignKey(Complex, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)

class Sizes(models.Model):
    name = models.CharField(max_length=255)

