from django.shortcuts import render
from .forms import orderForm
from first.forms import orderForm
from .models import food, order
def index(request):
    context={
        'fd':food.objects.all()
    }
    return render(request,'pages/index.html',context)

def categories(request):
    context={
        'fd' :food.objects.all()
    }
    return render(request,'pages/categories.html',context)

def foods(request):
    context={
        'fd':food.objects.all()
    }
    return render(request,'pages/foods.html',context)

def order(request,id):
    if request.method == "POST":
        add_order=orderForm(request.POST,request.FILES)
        if add_order.is_valid():
            add_order.save()
            
    food_id=food.objects.get(id=id)
    context={
        'fd_id' :food_id,
        'form': orderForm()
    }
    return render(request,'pages/order.html',context)

def category_food(request):
    context={
        'fd' :food.objects.all()
    }
    return render(request,'pages/category_food.html',context)

def food_search(request):
    context={
        'fd':food.objects.all()
    }
    return render(request,'pages/food_search.html',context)