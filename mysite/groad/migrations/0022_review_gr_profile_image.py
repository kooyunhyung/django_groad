# Generated by Django 4.0.6 on 2022-11-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0021_remove_review_gr_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='gr_profile_image',
            field=models.CharField(max_length=500, null=True, verbose_name='프로필사진'),
        ),
    ]
