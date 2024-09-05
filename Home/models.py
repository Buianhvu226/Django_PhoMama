from email.mime import image
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField

class Account(models.Model):
    AccountID = models.AutoField(primary_key=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)
    isDeleted = models.BooleanField(default=False)
    isStaff = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    RoleID = models.IntegerField(primary_key=True)
    RoleName = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Measure(models.Model):
    MeasureID = models.IntegerField(primary_key=True)
    MeasureName = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    DistrictID = models.IntegerField(primary_key=True)
    DistrictName = models.CharField(max_length=50)

    def __str__(self):
        return self.DistrictName

class Ward(models.Model):
    WardId = models.IntegerField(primary_key=True)
    WardName = models.CharField(max_length=50)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE, null=True, related_name='wards')
    def __str__(self):
        return self.WardName

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=100, null=True)
    Phone = models.CharField(max_length=10)
    Gender = models.BooleanField(null=True)
    HouseNumber = models.CharField(max_length=255, null=True)
    Ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.CustomerName or ""

class Staff(models.Model):
    StaffID = models.IntegerField(primary_key=True)
    StaffName = models.CharField(max_length=100, null=True)
    Phone = models.CharField(max_length=10, null=True)
    Gender = models.BooleanField(null=True)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    HouseNumber = models.CharField(max_length=255, null=True)
    Ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    FoodID = models.AutoField(primary_key=True)
    FoodName = models.CharField(max_length=255)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    originPrice = models.FloatField()
    ImageFood = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    IsDeleted = models.BooleanField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.FoodName

class Ingredients(models.Model):
    IngredientsId = models.IntegerField(primary_key=True)
    IngredientsName = models.CharField(max_length=200)
    IngredientsPrice = models.FloatField()
    IngredientsQty = models.FloatField()
    IsDeleted = models.BooleanField()
    Measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food_Ingredients(models.Model):
    Food = models.ForeignKey(Food, on_delete=models.CASCADE)
    Ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    QuantityIG = models.FloatField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    Order_id = models.AutoField(primary_key=True)
    Sale_date = models.DateTimeField()
    Arrive_time = models.DateTimeField(blank=True, null=True)
    Customer_name = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=20)  # Adjust max_length based on your requirements

    Note = models.TextField(default='', blank=True)  # Adjust max_length as needed
    Temp_money = models.FloatField()
    Shipping_money = models.FloatField()
    Total_money = models.FloatField()
    Status_odr = models.IntegerField()

    House_number = models.CharField(max_length=255, blank=True, null=True)
    Ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    Chef_staff = models.ForeignKey(Staff, related_name='chef_orders', on_delete=models.CASCADE, blank=True, null=True)
    Shipper_staff = models.ForeignKey(Staff, related_name='shipper_orders', on_delete=models.CASCADE, blank=True, null=True)

    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer_name}"
    
class Order_Food(models.Model):
    Orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Food = models.ForeignKey(Food, on_delete=models.CASCADE)
    QuantityOF = models.IntegerField()
    PriceOF = models.FloatField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Food = models.ForeignKey(Food, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    @property
    def total_price(self):
        return self.Food.Price * self.Quantity

    def __str__(self):
        return f'{self.Customer.CustomerName} - {self.Food.FoodName} - {self.Quantity}'
        
class Review(models.Model):
    ReviewID = models.IntegerField(primary_key=True)
    Star = models.IntegerField()
    Content = models.TextField()
    Img = models.TextField()
    DateReview = models.DateTimeField()
    CustomerID = models.IntegerField()
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    FoodID = models.IntegerField()
    Food = models.ForeignKey(Food, on_delete=models.CASCADE)
    Orders = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return self.name







