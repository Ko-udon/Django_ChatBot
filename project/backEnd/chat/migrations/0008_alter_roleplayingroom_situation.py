# Generated by Django 4.0.3 on 2023-11-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_remove_roleplayingroom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleplayingroom',
            name='situation',
            field=models.CharField(max_length=100, verbose_name='상황'),
        ),
    ]
