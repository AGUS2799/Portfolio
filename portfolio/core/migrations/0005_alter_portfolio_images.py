# Generated by Django 4.1.4 on 2022-12-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_portfolio_alter_education_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
    ]
