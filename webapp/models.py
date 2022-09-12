from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry


class Company(models.Model):
    name = models.CharField('Name', max_length=100)
    website = models.CharField('Website', max_length=255, blank=True, null=True)
    created_at = models.DateField('Created At', default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.website}'


class Vehicle(models.Model):
    name = models.CharField('Name', max_length=255, blank=True, null=True)
    YOM = models.CharField('Year of Make', max_length=255, null=True)
    image = models.CharField('Image', max_length=255, blank=True, null=True)
    price = models.CharField('Price', max_length=255, null=True)
    make = models.CharField('Model', max_length=255, blank=True, null=True)
    millage = models.CharField('Millage', max_length=255, blank=True, null=True)
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
        return f'{self.title} {self.pub_date}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    review = models.TextField('Review', blank=True, null=True)
    rating = models.IntegerField('Rating', blank=True, null=True)
    date_created = models.DateTimeField('Date Created', default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.review} {self.rating}'


class CustomLogEntry(LogEntry):
    log_type = models.CharField('Log Type', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.user} {self.action_time} {self.change_message}'
