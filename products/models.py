
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Accessories', 'Accessories'),
        ('Clothing', 'Clothing'),
        ('Shoes', 'Shoes'),
        ('Skincare', 'Skincare'),
    ]
    TYPE_CHOICES = [
        ('Accessories', (
            ('Bags', 'Bags'),
            ('Gloves', 'Gloves'),
            ('Hair', 'Hair'),
            ('Hats', 'Hats'),
            ('Jewellery', 'Jewellery'),
            ('Socks', 'Socks'),
            ('Sunglasses', 'Sunglasses'),
            ('Tights', 'Tights'),
        )
        ),
        ('Clothing', (
            ('Coats + Jackets', 'Coats + Jackets'),
            ('Dresses', 'Dresses'),
            ('Jeans', 'Jeans'),
            ('Knitwear', 'Knitwear'),
            ('Shorts', 'Shorts'),
            ('Skirts', 'Skirts'),
            ('Sweatshirt', 'Sweatshirt'),
            ('T-shirts', 'T-shirts'),
            ('Trousers', 'Trousers'),
            ('Underwear', 'Underwear'),
        )
        ),
        ('Shoes', (
            ('Trainers', 'Trainers'),
            ('Flats', 'Flats'),
            ('Heels', 'Heels'),
            ('Trainers', 'Trainers'),
        )
        ),
        ('Skincare', (
            ('Cleansers', 'Cleansers'),
            ('Eyes + Lips', 'Eyes + Lips'),
            ('Moisturisers', 'Moisturisers'),
            ('Serums', 'Serums'),
            ('Suncream', 'Suncream'),
            ('Tools', 'Tools'),
        )
        ),
    ]
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=60)
    description = models.TextField()
    image = models.CharField(max_length=300)
    color = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.designer}'

class Wishlist(models.Model):
    '''Wishlist Model'''
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        related_name='wishlisted_by',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='wishlisted_product',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Wishlisted {self.id} - Product {self.product}'