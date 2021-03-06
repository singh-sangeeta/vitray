# Generated by Django 3.1 on 2020-10-14 11:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('date_created', models.DateField(null=True)),
                ('date_deleted', models.DateField(null=True)),
                ('date_updated', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_details', models.CharField(max_length=100)),
                ('date_created', models.DateField(null=True)),
                ('date_deleted', models.DateField(null=True)),
                ('date_updated', models.DateField(null=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateField(null=True)),
                ('date_updated', models.DateField(null=True)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.IntegerField()),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
