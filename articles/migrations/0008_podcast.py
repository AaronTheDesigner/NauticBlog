# Generated by Django 2.0.7 on 2018-08-08 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_event_novella_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]