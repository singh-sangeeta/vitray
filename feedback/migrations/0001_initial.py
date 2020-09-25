# Generated by Django 3.1 on 2020-09-22 13:01

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('product_id', models.ForeignKey(on_delete=models.SET(products.models.Product), to='products.product')),
            ],
        ),
    ]