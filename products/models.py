
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Accessories', 'Accessories'),
        ('Clothing', 'Clothing'),
        ('Shoes', 'Shoes'),
        ('Beauty + Lifestyle', 'Beauty + Lifestyle'),
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
            ('Trackpants', 'Trackpants'),
            ('Trousers', 'Trousers'),
        )
        ),
        ('Shoes', (
            ('Boots', 'Boots'),
            ('Flats', 'Flats'),
            ('Heels', 'Heels'),
            ('Trainers', 'Trainers'),
        )
        ),
        ('Beauty + Lifestyle', (
            ('Skincare', 'Skincare'),
            ('Makeup', 'Makeup'),
            ('Home', 'Home'),
        )
        ),
    ]
    COLOR_CHOICES = [
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Camel', 'Camel'),
        ('Cream', 'Cream'),
        ('Green', 'Green'),
        ('Grey', 'Grey'),
        ('Lilac', 'Lilac'),
        ('Mixed', 'Mixed'),
        ('Natural', 'Natural'),
        ('Olive', 'Olive'),
        ('Peach', 'Peach'),
        ('Pink', 'Pink'),
        ('Purple', 'Purple'),
        ('Red', 'Red'),
        ('Sand', 'Sand'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('N/A', 'N/A'),
    ]
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=60)
    description = models.TextField()
    image = models.CharField(max_length=300)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    featured_product = models.BooleanField(default=False)

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
        related_name='wishlisted_products',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Wishlisted {self.id} - Product {self.product}'

class Wardrobe(models.Model):
    '''Wardrobe Model'''
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        related_name='in_wardrobe_of',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='products_in_wardrobe',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Product {self.product} in Wardrobe {self.id}'

class ShoppingBag(models.Model):
    '''Shopping Bag Model'''
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        related_name='in_shopping_bag_of',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='products_in_shopping_bag',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Product {self.product} in Shopping Bag {self.id}'
