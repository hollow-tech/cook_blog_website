# Generated by Django 3.2.7 on 2021-09-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
