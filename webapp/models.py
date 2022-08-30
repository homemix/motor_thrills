from django.db import models


class Brand(models.Model):
    name = models.CharField('Name', max_length=100)
    model = models.CharField('Model', max_length=100)
    YOM = models.DateField('Year Of Make', blank=True, null=True)
    overview = models.TextField('Overview', blank=True, null=True)
    technical = models.TextField('Technical', blank=True, null=True)
    options = models.TextField('Options', blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return f'{self.name} {self.model}'


class Dealer(models.Model):
    name = models.CharField('Name', max_length=100)
    location = models.CharField('Location', max_length=100)

    def __str__(self):
        return f'{self.name} {self.location}'


class Company(models.Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return f'{self.name} {self.location}'


class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    Dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer')
    millage = models.IntegerField('Millage', )
    price = models.IntegerField('Price',)

    def __str__(self):
        return f'{self.brand} {self.Dealer} {self.millage} {self.price}'
