# Generated by Django 3.0.6 on 2020-05-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='email',
            field=models.CharField(blank=True, default='someone@gmail.com', max_length=100, null=True),
        ),
    ]