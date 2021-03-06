# Generated by Django 2.0.7 on 2018-08-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events_One',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('thumb', models.ImageField(upload_to='')),
                ('link', models.URLField()),
                ('date', models.TimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events_Three',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('thumb', models.ImageField(upload_to='')),
                ('link', models.URLField()),
                ('date', models.TimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events_Two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('thumb', models.ImageField(upload_to='')),
                ('link', models.URLField()),
                ('date', models.TimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_one', models.CharField(max_length=50)),
                ('category_two', models.CharField(max_length=50)),
                ('category_three', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Works_One',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_one', models.CharField(max_length=50)),
                ('thumb_one', models.ImageField(upload_to='')),
                ('blurb_one', models.TextField()),
                ('quote_one', models.TextField()),
                ('reviewer_one', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Works_Three',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_three', models.CharField(max_length=50)),
                ('thumb_three', models.ImageField(upload_to='')),
                ('blurb_three', models.TextField()),
                ('quote_three', models.TextField()),
                ('reviewer_three', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Works_Two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_two', models.CharField(max_length=50)),
                ('thumb_two', models.ImageField(upload_to='')),
                ('blurb_two', models.TextField()),
                ('quote_two', models.TextField()),
                ('reviewer_two', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
