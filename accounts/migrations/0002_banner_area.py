# Generated by Django 3.2.12 on 2022-03-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner_Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/banner_img')),
                ('discount_deal', models.CharField(max_length=100)),
                ('quote', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
            ],
        ),
    ]