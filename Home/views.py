# from django.shortcuts import render,redirect, get_object_or_404
# #importing the models
# from .models import Account, Cart, Category, Customer, Food, Food_Ingredients, Ingredients, Measure, Order_Food, Ward, Review, Orders, Role, Staff, Ward, District
# from django.core.paginator import Paginator
# from django.core.paginator import PageNotAnInteger
# from django.core.paginator import EmptyPage
# import urllib.parse
# from .helpers import PagingModel

# def template(request):
#      return render(request, 'template.html')
 
# # Home function
# def home(request):
#     account = Account.objects.all()
#     cart = Cart.objects.all()
#     category = Category.objects.all()
#     customer = Customer.objects.all()
#     food = Food.objects.all()
#     food_ingredients = Food_Ingredients.objects.all()
#     ingredients = Ingredients.objects.all()
#     measure = Measure.objects.all()
#     order_food = Order_Food.objects.all()
#     ward = Ward.objects.all()
#     review = Review.objects.all()
#     orders = Orders.objects.all()
#     role = Role.objects.all()
#     staff = Staff.objects.all()
#     ward = Ward.objects.all()
#     district = District.objects.all()

#     # # render the home page
#     #return render(request, 'index.html', {'categories': categories, 'items': items,'cart':cart,'cart_total':cart_total,'cart_nbr':cart_nbr,'reviews':reviews,'restaurant':restaurant,'coming_soon':coming_soon,'about':about})
#     return render(request, 'index.html', {'account': account, 'cart': cart, 'category': category, 'customer': customer, 'foods': food, 'food_ingredients': food_ingredients, 'ingredients': ingredients, 'measure': measure, 'order_food': order_food, 'ward': ward, 'review': review, 'orders': orders, 'role': role, 'staff': staff, 'ward': ward, 'district': district})

# def login_register(request):
#     # Logic for handling login/register POST requests
#     if request.method == 'POST':
#         # Process form data
#         pass  # Implement your form processing logic here

#     return render(request, 'login_register.html', context={})

# def menu(request):
#     categories = Category.objects.all()  # Lấy danh sách danh mục
#     # Xử lý các tham số truyền vào để lọc sản phẩm
#     category_id = request.GET.get('CategoryID')
#     price_range = request.GET.get('Price')
#     sort_by = request.GET.get('sortBy')
#     search_text = request.GET.get('search')

#     # Lọc sản phẩm theo các tham số
#     foods = Food.objects.all()
#     if category_id:
#         foods = foods.filter(category_id=category_id)
#     if price_range:
#         # Xử lý lọc theo mức giá
#         # Ví dụ: nếu price_range là '1-2', thì lọc các sản phẩm có giá từ 1 triệu đến 2 triệu
#         # foods = foods.filter(price__gte=1000000, price__lte=2000000)
#         price_range = price_range.split('-')
#         try:
#             price_min = int(price_range[0])
#             price_max = int(price_range[1])
#             foods = foods.filter(price__gte=price_min, price__lte=price_max)
#         except:
#             pass
#     if sort_by:
#         if sort_by == 'price-asc':
#             foods = foods.order_by('price')
#         elif sort_by == 'price-desc':
#             foods = foods.order_by('-price')
#         elif sort_by == 'name-asc':
#             foods = foods.order_by('name')
#         elif sort_by == 'name-desc':
#             foods = foods.order_by('-name')
#     if search_text:
#         # Xử lý tìm kiếm
#         foods = foods.filter(name__icontains=search_text)
    
#     # Pagination
#     paginator = Paginator(foods, 6)  # Show 6 foods per page
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'categories': categories,
#         'foods': page_obj.object_list,
#         'page_obj': page_obj,
#         'categoryID': category_id,
#         'priceRange': price_range,
#         'sortBy': sort_by,
#         'searchText': search_text
#     }
#     return render(request, 'Home/menu.html', context)

# def detail_food(request, food_id):
#     food = get_object_or_404(Food, pk=food_id)
#     reviews = Review.objects.filter(food=food)
    
#     if reviews:
#         total_rating = sum(review.star for review in reviews) / len(reviews)
#     else:
#         total_rating = 0

#     rating_percentage = (total_rating / 5) * 100

#     context = {
#         'food': food,
#         'category': food.Category.name,
#         'reviews': reviews,
#         'total_rating': total_rating,
#         'rating_percentage': rating_percentage,
#         'max_qty': food.max_qty,  # Assuming this field exists in your Food model
#         'product_info': request.POST.get('product_info', None)  # Example, adapt as necessary
#     }

#     return render(request, 'Home/detail_food.html', context)

# def cart(request):
#     context = {
#     }

#     return render(request, 'Home/cart.html', context)

# def payment(request):
#     context = {
#     }

#     return render(request, 'Home/payment.html', context)

# def my_order(request):
#     context = {
#     }

#     return render(request, 'Home/my_order.html', context)


# # add to cart function
# def add_to_cart(request, id):

#     return redirect('Home')

# # delete from cart function
# def delete_from_cart(request, id):
#     # get the item id
#     item_id = str(id)
#     # delete the item from the cart
#     del request.session['cart'][item_id]
#     request.session.modified = True
#     # redirect to home
#     return redirect('Home')

# # checkout function
# def checkout(request):

#     wp_link = "https://api.whatsapp.com/send?phone="
#     # redirect to the whatsapp link
#     return redirect(wp_link)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Cart, Category, Customer, Food, Food_Ingredients, Ingredients, Measure, Order_Food, Ward, Review, Orders, Role, Staff, Ward, District
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import PageNotAnInteger, EmptyPage
import urllib.parse
from .helpers import PagingModel
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.db.models import F
from django.http import HttpResponseBadRequest
from datetime import datetime
from .forms import FoodForm

def template(request):
     return render(request, 'Home/index_body.html')

def home(request):
    account = Account.objects.all()
    cart = Cart.objects.all()
    category = Category.objects.all()
    customer = Customer.objects.all()
    food = Food.objects.all()
    food_ingredients = Food_Ingredients.objects.all()
    ingredients = Ingredients.objects.all()
    measure = Measure.objects.all()
    order_food = Order_Food.objects.all()
    ward = Ward.objects.all()
    review = Review.objects.all()
    orders = Orders.objects.all()
    role = Role.objects.all()
    staff = Staff.objects.all()
    ward = Ward.objects.all()
    district = District.objects.all()
    
    email = request.session.get('Email')
    return render(request, 'index.html', {
        'account': account, 'cart': cart, 'category': category,
        'customer': customer, 'foods': food, 'food_ingredients': food_ingredients,
        'ingredients': ingredients, 'measure': measure, 'order_food': order_food,
        'ward': ward, 'review': review, 'orders': orders, 'role': role,
        'staff': staff, 'ward': ward, 'district': district, 'email': email
    })

def login_register(request):
    if request.method == 'POST':
        pass  # Implement your form processing logic here

    return render(request, 'login_register.html', context={})

def menu(request):
    categories = Category.objects.all()  # Get all categories
    
    # Retrieve filter parameters from the request
    category_id = request.GET.get('CategoryID')
    price_range = request.GET.get('priceRange')
    sort_by = request.GET.get('sortBy')
    search_text = request.GET.get('searchText')

    # Start with all food items
    foods = Food.objects.all()

    # Filter by category if category_id is provided and not empty
    if category_id:
        foods = foods.filter(Category_id=category_id)

    # Filter by price range if provided
    if price_range:
        price_parts = price_range.split('-')
        if len(price_parts) == 2:
            price_min, price_max = map(int, price_parts)
            foods = foods.filter(Price__gte=price_min, Price__lte=price_max)

    # Sort the results if sort_by is provided
    if sort_by:
        if sort_by == 'price-asc':
            foods = foods.order_by('Price')  # Sort ascending by Price
        elif sort_by == 'price-desc':
            foods = foods.order_by('-Price')  # Sort descending by Price
        elif sort_by == 'name-asc':
            foods = foods.order_by('FoodName')  # Sort ascending by FoodName
        elif sort_by == 'name-desc':
            foods = foods.order_by('-FoodName')  # Sort descending by FoodName

    # Filter by search text if provided
    if search_text:
        foods = foods.filter(FoodName__icontains=search_text)
    
    # Pagination
    paginator = Paginator(foods, 6)  # Show 6 foods per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'foods': page_obj.object_list,
        'page_obj': page_obj,
        'categoryID': category_id,
        'priceRange': price_range,
        'sortBy': sort_by,
        'searchText': search_text
    }
    return render(request, 'Home/menu.html', context)

def login(request):
    return render(request, 'Login/login_register.html')

def detail_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    reviews = Review.objects.filter(Food=food)
    
    if reviews.exists():
        total_rating = sum(review.Star for review in reviews) / reviews.count()
    else:
        total_rating = 0

    rating_percentage = (total_rating / 5) * 100 if total_rating else 0

    context = {
        'food': food,
        'category': food.Category.CategoryName,
        'reviews': reviews,
        'total_rating': total_rating,
        'rating_percentage': rating_percentage,
        'max_qty': food.Quantity,
        'product_info': request.POST.get('product_info', None)
    }

    return render(request, 'Home/detail_food.html', context)

def cart(request, customer_id):
    if customer_id:
        try:
            customer = Customer.objects.get(Account_id=customer_id)
            carts = Cart.objects.filter(Customer=customer)
            total_money = sum(cart.Quantity * cart.Food.Price for cart in carts)
            total_payment = total_money + total_money * 3 / 100

            context = {
                'carts': carts,
                'totalMoney': total_money,
                'totalPayment': total_payment
            }
            return render(request, 'Home/cart.html', context)
        except Customer.DoesNotExist:
            return render(request, 'Home/cart.html', {'error_message': 'Customer does not exist'})
    else:
        return render(request, 'Home/cart.html', {'error_message': 'Customer ID not provided'})

def add_plus_1(request, id):
    item_id = str(id)
    customer_id = request.POST.get('user_id')
    cart_item = Cart.objects.get(id=item_id)
    cart_item.Quantity = F('Quantity') + 1
    cart_item.save()
    return redirect('Home/cart',  customer_id=customer_id)

def minus_plus_1(request, id):
    item_id = str(id)
    customer_id = request.POST.get('user_id')
    cart_item = Cart.objects.get(id=item_id)
    if cart_item.Quantity > 1:
        cart_item.Quantity = F('Quantity') - 1
        cart_item.save()
    return redirect('Home/cart', customer_id=customer_id)

def delete_from_cart(request, id):
    item_id = str(id)
    del request.session['cart'][item_id]
    request.session.modified = True
    return redirect('Home/menu')

def payment(request):
    if request.method == 'POST':
        temp_money = request.POST.get('total_money')
        # Convert temp_money to float to perform arithmetic operations
        temp_money = float(temp_money)
        sale_money = temp_money * 3 / 100
        sum_money = temp_money + sale_money + 15500
        
        list_districts = District.objects.all()
        initial_district_id = list_districts[0].DistrictID if list_districts else None
        list_wards = Ward.objects.filter(DistrictID=initial_district_id) if initial_district_id else []
        
        context = {
            'temp_money': temp_money,
            'sale_money': sale_money,
            'sum_money': sum_money,
            'list_districts': list_districts,
            'list_wards': list_wards,
        }
        return render(request, 'Home/payment.html', context)

    return render(request, 'Home/payment.html')

def get_wards(request, district_id):
    wards = Ward.objects.filter(district_id=district_id)
    ward_list = list(wards.values('id', 'WardName'))
    return JsonResponse(ward_list, safe=False)

def my_order(request):
    # Assuming user_id is stored in session
    customer_id = request.session.get('user_id')
    
    if customer_id:
        customer = Customer.objects.get(Account_id=customer_id)
        orders = Orders.objects.filter(Customer=customer)
    else:
        orders = []

    context = {
        'orders': orders,
    }

    return render(request, 'Home/my_order.html', context)

def order_detail(request):
    if request.method == 'POST':
        receiver_name = request.POST.get('Name')
        phone_number = request.POST.get('PhoneNumber')
        district_id = request.POST.get('combobox_Item_District')
        ward_id = request.POST.get('combobox_Item_Ward')
        house_number = request.POST.get('HouseNumber')
        note = request.POST.get('Note')
        address = f'{house_number}, {Ward.objects.get(WardId=ward_id).WardName}, {District.objects.get(DistrictID=district_id).DistrictName}'

        customer_id = request.session.get('user_id')
        customer = get_object_or_404(Customer, Account_id=customer_id)

        carts = Cart.objects.filter(Customer=customer)
        total_money = sum(cart.Quantity * cart.Food.Price for cart in carts)
        sale_money = total_money * 0.03
        shipping_fee = 15500
        sum_money = total_money + sale_money + shipping_fee

        order = Orders.objects.create(
            Customer_name=receiver_name,
            Phone_number=phone_number,
            Note=note,
            Temp_money=total_money,
            Shipping_money=shipping_fee,
            Total_money=sum_money,
            Sale_date=datetime.now(),
            Status_odr=1,
            House_number=house_number,
            Customer=customer,
            Ward_id=ward_id,
        )

        carts_list = [
            {
                "FoodName": cart.Food.FoodName,
                "Quantity": cart.Quantity,
                "Price": cart.Food.Price,
                "ImageFood": cart.Food.ImageFood,
                "total_price": cart.Quantity * cart.Food.Price  # Tính tổng giá cho mỗi cart item
            } for cart in carts
        ]

        # Save order data in session
        request.session['order_data'] = {
            'receiver_name': receiver_name,
            'phone_number': phone_number,
            'district_id': district_id,
            'ward_id': ward_id,
            'house_number': house_number,
            'sale_date': order.Sale_date.strftime('%d/%m/%Y %H:%M'),
            'carts': carts_list,
            'note': note,
            'address': address,
            'total_money': total_money,
            'sale_money': sale_money,
            'sum_money': sum_money,
            'order_id': order.Order_id
        }

        for item in carts_list:
            print(item['FoodName'])

        context = request.session['order_data']  # Truyền dữ liệu session vào context

        return render(request, 'Home/order_detail.html', context)
    else:
        context = {}
        return render(request, 'Home/order_detail.html', context)


def detail_order(request, order_id):
    order = get_object_or_404(Orders, Order_id=order_id)
    customer = order.Customer
    carts = Cart.objects.filter(Customer=customer)

    carts_list = [
        {
            "FoodName": cart.Food.FoodName,
            "Quantity": cart.Quantity,
            "Price": cart.Food.Price,
            "ImageFood": cart.Food.ImageFood,
            "total_price": cart.Quantity * cart.Food.Price
        } for cart in carts
    ]

    # Fetch district and ward names for the address
    ward_name = Ward.objects.get(WardId=order.Ward_id).WardName
    address = f'{order.House_number}, {ward_name}'

    context = {
        'receiver_name': order.Customer_name,
        'phone_number': order.Phone_number,
        'district_id': order.Ward_id,  # assuming district id is stored in ward_id
        'ward_id': order.Ward_id,
        'house_number': order.House_number,
        'sale_date': order.Sale_date.strftime('%d/%m/%Y %H:%M'),
        'carts': carts_list,
        'note': order.Note,
        'address': address,
        'total_money': order.Temp_money,
        'sale_money': order.Temp_money * 0.03,  # Assuming the same logic for sale money
        'shipping_fee': order.Shipping_money,
        'sum_money': order.Total_money,
        'order_id': order.Order_id
    }

    return render(request, 'Home/order_detail.html', context)


def add_to_cart(request, id):
    return redirect('home')

def delete_cart(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        customer_id = request.POST.get('user_id')

        if customer_id and food_id:
            try:
                customer = Customer.objects.get(Account_id=customer_id)
                food = Food.objects.get(FoodID=food_id)
                cart_item = Cart.objects.get(Customer=customer, Food=food)
                cart_item.delete()  # Delete the cart item completely
                return redirect('home:cart', customer_id=customer_id)  # Pass customer_id as URL parameter
            except (Customer.DoesNotExist, Food.DoesNotExist, Cart.DoesNotExist):
                return redirect('home:menu')

    return HttpResponseBadRequest("Invalid request")  # Add this line
        
def cart_add(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        customer_id = request.POST.get('user_id')

        if customer_id and food_id:
            try:
                customer = Customer.objects.get(Account_id=customer_id)
                food = Food.objects.get(FoodID=food_id)
                cart_item, created = Cart.objects.get_or_create(Customer=customer, Food=food, defaults={'Quantity': 1})
                if not created:
                    cart_item.Quantity = F('Quantity') + 1  # Increment quantity for existing cart item
                    cart_item.save()
                return redirect('home:cart', customer_id=customer_id)  # Pass customer_id as URL parameter
            except (Customer.DoesNotExist, Food.DoesNotExist):
                return redirect('home:menu')

def checkout(request):
    wp_link = "https://api.whatsapp.com/send?phone="
    return redirect(wp_link)

def logout(request):
    return render(request, 'Login/login_register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        before_login = email.split('@')[0]

        # Xác thực thông tin người dùng
        user = Account.objects.get(Email=email, Password=password)
        customer = Customer.objects.get(Account_id=user.AccountID)
        if user is not None:
            # Lưu thông tin đăng nhập vào session               
            request.session['logged_in'] = True
            request.session['user_email'] = before_login
            request.session['user_id'] = user.AccountID
            request.session['customer_id'] = customer.CustomerID
            return render(request, 'Home/index_body.html')

def empty_cart(request):
    return render(request, 'Home/empty_cart.html')

# Admin views






# def menu(request):
#     categories = Category.objects.all()  # Get all categories
    
#     # Retrieve filter parameters from the request
#     category_id = request.GET.get('CategoryID')
#     price_range = request.GET.get('priceRange')
#     sort_by = request.GET.get('sortBy')
#     search_text = request.GET.get('searchText')

#     # Start with all food items
#     foods = Food.objects.all()

#     # Filter by category if category_id is provided and not empty
#     if category_id:
#         foods = foods.filter(Category_id=category_id)

#     # Filter by price range if provided
#     if price_range:
#         price_parts = price_range.split('-')
#         if len(price_parts) == 2:
#             price_min, price_max = map(int, price_parts)
#             foods = foods.filter(Price__gte=price_min, Price__lte=price_max)

#     # Sort the results if sort_by is provided
#     if sort_by:
#         if sort_by == 'price-asc':
#             foods = foods.order_by('Price')  # Sort ascending by Price
#         elif sort_by == 'price-desc':
#             foods = foods.order_by('-Price')  # Sort descending by Price
#         elif sort_by == 'name-asc':
#             foods = foods.order_by('FoodName')  # Sort ascending by FoodName
#         elif sort_by == 'name-desc':
#             foods = foods.order_by('-FoodName')  # Sort descending by FoodName

#     # Filter by search text if provided
#     if search_text:
#         foods = foods.filter(FoodName__icontains=search_text)
    
#     # Pagination
#     paginator = Paginator(foods, 6)  # Show 6 foods per page
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'categories': categories,
#         'foods': page_obj.object_list,
#         'page_obj': page_obj,
#         'categoryID': category_id,
#         'priceRange': price_range,
#         'sortBy': sort_by,
#         'searchText': search_text
#     }
#     return render(request, 'Home/menu.html', context)

def admin_menu(request):
    foods = Food.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(foods, 100)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'foods': page_obj.object_list,
        'page_obj': page_obj,
        'categories': categories,
    }

    return render(request, 'Home/admin_menu.html', context)

from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Food, Category

def add_food(request):
    if request.method == 'POST':
        foodName = request.POST.get('foodName')
        categoryID = request.POST.get('category')
        category = Category.objects.get(CategoryID=categoryID)  # Get the Category instance
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.POST.get('image')
        description = request.POST.get('description')
        originPrice = 0.0  # Ensure originPrice is a float
        isDeleted = False

        # Create the Food object using the Category instance
        food = Food(FoodName=foodName, Category=category, Quantity=quantity, Price=price, ImageFood=image, Description=description, originPrice=originPrice, IsDeleted=isDeleted)
        food.save()

        if food.pk:  # Check if the food object has a primary key, indicating it was saved successfully
            return redirect('home:admin_menu')  # Redirect to the admin menu page
        else:
            return JsonResponse({'success': False})

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'Home/admin_menu.html', context)



def delete_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    food.delete()
    messages.success(request, 'Food item deleted successfully.')
    return redirect('home:admin_menu')

def order_admin(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'Home/order_admin.html', context)