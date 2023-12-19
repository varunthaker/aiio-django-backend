# Generated by Django 5.0 on 2023-12-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcatergory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('subCategoryId', models.IntegerField()),
                ('subCategoryName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryId', models.IntegerField()),
                ('subProductId', models.IntegerField()),
                ('subProductName', models.CharField(max_length=200)),
            ],
        ),
    ]