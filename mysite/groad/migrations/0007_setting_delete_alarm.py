# Generated by Django 4.0.6 on 2022-11-03 15:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0006_alter_inquiry_gi_contents'),
    ]

    operations = [
        migrations.CreateModel(
            name='setting',
            fields=[
                ('gs_seq', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)], verbose_name='시퀀스')),
                ('gs_map', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('gs_theme', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('gs_onoff1', models.BooleanField(default=False)),
                ('gs_onoff2', models.BooleanField(default=False)),
                ('gs_onoff3', models.BooleanField(default=False)),
                ('gs_gu_seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gs_gu_seq', to='groad.user')),
            ],
        ),
        migrations.DeleteModel(
            name='alarm',
        ),
    ]
