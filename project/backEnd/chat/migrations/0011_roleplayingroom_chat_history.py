# Generated by Django 4.0.3 on 2023-11-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_alter_roleplayingroom_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='roleplayingroom',
            name='chat_history',
            field=models.CharField(default='', max_length=10000, verbose_name='채팅 기록'),
            preserve_default=False,
        ),
    ]