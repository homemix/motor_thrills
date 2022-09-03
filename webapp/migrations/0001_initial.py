# Generated by Django 4.1 on 2022-09-03 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('created_at', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('link', models.TextField(blank=True, max_length=255, null=True, verbose_name='Link')),
                ('pub_date', models.TextField(blank=True, null=True, verbose_name='Published Date')),
                ('creator', models.CharField(blank=True, max_length=255, null=True, verbose_name='Creator')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date_created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date Created')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('YOM', models.IntegerField(null=True, verbose_name='Year of Make')),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('price', models.IntegerField(null=True, verbose_name='Price')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='Model')),
                ('millage', models.IntegerField(null=True, verbose_name='Millage')),
                ('more_info', models.TextField(blank=True, null=True, verbose_name='More Information')),
                ('created_at', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Created At')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com1pany', to='webapp.company')),
            ],
        ),
    ]
