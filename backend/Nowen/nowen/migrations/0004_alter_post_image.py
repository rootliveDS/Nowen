# Generated by Django 4.1.3 on 2022-12-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nowen', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='nowen/image'),
        ),
    ]
