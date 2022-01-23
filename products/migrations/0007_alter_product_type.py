# Generated by Django 4.0.1 on 2022-01-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Accessories', (('Bags', 'Bags'), ('Gloves', 'Gloves'), ('Hair', 'Hair'), ('Hats', 'Hats'), ('Jewellery', 'Jewellery'), ('Socks', 'Socks'), ('Sunglasses', 'Sunglasses'), ('Tights', 'Tights'))), ('Clothing', (('Coats + Jackets', 'Coats + Jackets'), ('Dresses', 'Dresses'), ('Jeans', 'Jeans'), ('Knitwear', 'Knitwear'), ('Shorts', 'Shorts'), ('Skirts', 'Skirts'), ('Sweatshirt', 'Sweatshirt'), ('T-shirts', 'T-shirts'), ('Trackpants', 'Trackpants'), ('Trousers', 'Trousers'), ('Underwear', 'Underwear'))), ('Shoes', (('Boots', 'Boots'), ('Flats', 'Flats'), ('Heels', 'Heels'), ('Trainers', 'Trainers'))), ('Skincare', (('Cleansers', 'Cleansers'), ('Eyes + Lips', 'Eyes + Lips'), ('Moisturisers', 'Moisturisers'), ('Serums', 'Serums'), ('Suncream', 'Suncream'), ('Tools', 'Tools')))], max_length=50),
        ),
    ]