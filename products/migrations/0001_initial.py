# Generated by Django 4.0.1 on 2022-01-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('Accessories', 'Accessories'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Skincare', 'Skincare')], max_length=50)),
                ('type', models.CharField(choices=[('Accessories', (('Bags', 'Bags'), ('Gloves', 'Gloves'), ('Hair', 'Hair'), ('Hats', 'Hats'), ('Jewellery', 'Jewellery'), ('Socks', 'Socks'), ('Sunglasses', 'Sunglasses'), ('Tights', 'Tights'))), ('Clothing', (('Coats + Jackets', 'Coats + Jackets'), ('Dresses', 'Dresses'), ('Jeans', 'Jeans'), ('Knitwear', 'Knitwear'), ('Shorts', 'Shorts'), ('Skirts', 'Skirts'), ('Sweatshirt', 'Sweatshirt'), ('T-shirts', 'T-shirts'), ('Trousers', 'Trousers'), ('Underwear', 'Underwear'))), ('Shoes', (('Trainers', 'Trainers'), ('Flats', 'Flats'), ('Heels', 'Heels'), ('Trainers', 'Trainers'))), ('Skincare', (('Cleansers', 'Cleansers'), ('Eyes + Lips', 'Eyes + Lips'), ('Moisturisers', 'Moisturisers'), ('Serums', 'Serums'), ('Suncream', 'Suncream'), ('Tools', 'Tools')))], max_length=50)),
            ],
        ),
    ]
