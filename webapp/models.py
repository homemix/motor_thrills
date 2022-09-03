from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField('Name', max_length=100)
    website = models.CharField('Website', max_length=255, blank=True, null=True)
    created_at = models.DateField('Created At', default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.location}'


class Vehicle(models.Model):
    name = models.CharField('Name', max_length=255, blank=True, null=True)
    YOM = models.IntegerField('Year of Make', null=True)
    image = models.CharField('Image', max_length=255, blank=True, null=True)
    price = models.IntegerField('Price', null=True)
    model = models.CharField('Model', max_length=255, blank=True, null=True)
    millage = models.IntegerField('Millage', null=True)
    more_info = models.TextField('More Information', blank=True, null=True)
    created_at = models.DateField('Created At', default=timezone.now, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='com1pany', )

    def __str__(self):
        return f'{self.name} {self.YOM} {self.millage} {self.price}'


class News(models.Model):
    title = models.TextField('Title', max_length=255, blank=True, null=True)
    link = models.TextField('Link', max_length=255, blank=True, null=True)
    pub_date = models.TextField('Published Date', blank=True, null=True)
    creator = models.CharField('Creator', max_length=255, blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    date_created = models.DateTimeField('Date Created', default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.link}'
