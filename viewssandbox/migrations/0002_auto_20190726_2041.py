# Generated by Django 2.0 on 2019-07-26 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewssandbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['first_name']},
        ),
    ]