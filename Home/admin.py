from django.contrib import admin
from .models import Account, Cart, Category, Customer, Food, Food_Ingredients, Ingredients, Measure, Order_Food, Ward, Review, Orders, Role, Staff, Ward, District
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)

admin.site.register(Account)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Food_Ingredients)
admin.site.register(Ingredients)
admin.site.register(Measure)
admin.site.register(Order_Food)
admin.site.register(Review)
admin.site.register(Orders)
admin.site.register(Role)
admin.site.register(Staff)
admin.site.register(Ward)
admin.site.register(District)