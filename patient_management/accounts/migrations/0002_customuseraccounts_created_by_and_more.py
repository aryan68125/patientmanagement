# Generated by Django 5.1.2 on 2024-10-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuseraccounts',
            name='created_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuseraccounts',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
