# Generated by Django 2.1 on 2020-01-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewssandbox', '0010_auto_20200129_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='status',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Professional', 'Professional')], help_text='Please choose your current position as student or professionsl.', max_length=12, null=True),
        ),
    ]
