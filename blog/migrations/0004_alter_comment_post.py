# Generated by Django 4.2.1 on 2023-06-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_post_id_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.CharField(max_length=500),
        ),
    ]
