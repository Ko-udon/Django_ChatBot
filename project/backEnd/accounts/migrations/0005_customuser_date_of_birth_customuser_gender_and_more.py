# Generated by Django 4.0.3 on 2023-11-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_options_remove_customuser_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '남자'), ('female', '여자')], max_length=6),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='이름', max_length=6),
        ),
    ]
