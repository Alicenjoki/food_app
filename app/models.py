from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

category =(
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
    ('Drinks', 'Drinks'),
)
class Meal(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(choices=category ,max_length=120, null=True)

    class Meta:
        verbose_name_plural = 'meal'

    def __str__(self):
        return self.name

choice = (
    ('none','none'),
    ('starter','starter'),
    ('main_course', 'main_course'),
    ('dessert', 'dessert'),
    ('Gin', 'Gin'),
    ('Whisky','Whisky'),
    ('Vodka','Vodka'),
)
class Course(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(choices=choice,max_length=120, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'course'

    def __str__(self):
        return f'{self.meal} | {self.name}'
    
    
class Food(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=120)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='food_pics/', default='/media/food.jpg')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ='food'
        ordering =('-created',)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'cart'

    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
    @property
    def no_items(self):
        cartitems = self.cartitems.all()
        quantity= sum([item.quantity for item in cartitems])
        return quantity
    
class Cartitem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cartitem'
        ordering = ('-added_at',)

    def __str__(self):
        return self.food.name
    
    @property
    def price(self):
        new_price = self.food.price* self.quantity
        return new_price
    
    
