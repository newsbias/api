# Generated by Django 2.0.2 on 2018-02-05 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='url',
            new_name='article_url',
        ),
    ]
