# Generated by Django 4.1.3 on 2022-11-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='')),
                ('genre', models.CharField(max_length=200)),
                ('duration', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=400)),
            ],
        ),
    ]
