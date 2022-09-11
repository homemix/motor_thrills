from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating', 'user']

    def save(self, commit=True):
        review = super(ReviewForm, self).save(commit=False)
        review.user = self.cleaned_data["user"]
        review.review = self.cleaned_data["review"]
        review.rating = self.cleaned_data["rating"]
        if commit:
            review.save()
        return review
