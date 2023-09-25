from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
@login_required
def home (request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed = False)
    context={
        'cart':cart,
    }
    return render(request, 'pages/home.html',context )

@login_required
def breakfast (request):
    foods = Food.objects.all()
    meal = Meal.objects.filter(name='Breakfast')
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed = False)
    context={
        'foods':foods,
        'meal':meal,
        'cart':cart,
    }
    return render(request, 'pages/breakfast.html',context)

@login_required
def lunch (request):
    foods = Food.objects.all()
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed = False)
    context={
        'foods':foods,
        'cart':cart,
    }
    return render(request, 'pages/lunch.html', context )

@login_required
def dinner (request):
    foods = Food.objects.all()
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed = False)
    context={
        'foods':foods,
        'cart':cart,
    }
    return render(request, 'pages/dinner.html', context )

@login_required
def drinks (request):
    foods = Food.objects.all()
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed = False)
    context={
        'foods':foods,
        'cart':cart
    }
    return render(request, 'pages/drinks.html',context )

@login_required
def cart (request):
    cart=None
    cartitems = []
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed = False)
        cartitems = cart.cartitems.all()
        cartitems_count = cartitems.count() 
        context={
            'cart':cart,
            'cartitems':cartitems,
            'cartitems_count':cartitems_count,
        }
    return render(request, 'pages/cart.html',context )

def add_to_cart(request):
    data = json.loads(request.body)
    food_id = data["id"]
    food = Food.objects.get(id=food_id)

    if request.user.is_authenticated:
        cart, created =Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = Cartitem.objects.get_or_create(cart=cart,food=food)
        cartitem.quantity += 1
        cartitem.save()

        no_items = cart.no_items
    return JsonResponse(no_items, safe=False)
    

def adminhome (request):
    foods = Food.objects.all()
    form = AddFoodForm()
    if request.method == 'POST':
        form = AddFoodForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed = False)
        
    context={
        'foods':foods,
        'form':form,
        'cart':cart,
    }
    return render(request, 'pages/adminhome.html',context )

def edit_food(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        form = AddFoodForm(request.POST,request.FILES,instance=foods)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }
    return render(request, 'pages/editfood.html',context)

def delete_food(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        foods.delete()
        return redirect('adminhome')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }

    return render(request, 'pages/deletefood.html', context)

################## admdrinks ###################
def admdrinks (request):
    foods = Food.objects.all()
        
    context={
        'foods':foods,
    }
    return render(request, 'pages/admdrinks.html', context)

def edit_admdrinks(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        form = AddFoodForm(request.POST,request.FILES,instance=foods)
        if form.is_valid():
            form.save()
            return redirect('admdrinks')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }
    return render(request, 'pages/editfood.html',context)

def delete_admdrinks(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        foods.delete()
        return redirect('admdrinks')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }

    return render(request, 'pages/deletefood.html', context)

#################### End  #####################


###################  admlunch ##################
def admlunch(request):
    foods = Food.objects.all()
    context={
        'foods':foods,
    }
    return render(request, 'pages/admlunch.html',context )

def edit_admlunch(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        form = AddFoodForm(request.POST,request.FILES,instance=foods)
        if form.is_valid():
            form.save()
            return redirect('admlunch')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }
    return render(request, 'pages/editfood.html',context)

def delete_admlunch(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        foods.delete()
        return redirect('admlunch')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }

    return render(request, 'pages/deletefood.html', context)

##################  end###############

##################admdinner####################
def admdinner(request):
    foods = Food.objects.all()
    context={
        'foods':foods,
    }
    return render(request, 'pages/admdinner.html',context )

def edit_admdinner(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        form = AddFoodForm(request.POST,request.FILES,instance=foods)
        if form.is_valid():
            form.save()
            return redirect('admdinner')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }
    return render(request, 'pages/editfood.html',context)

def delete_admdinner(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        foods.delete()
        return redirect('admdinner')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }

    return render(request, 'pages/deletefood.html', context)

################### end ######################

################# admbreakfast ###################
def admbreakfast(request):
    foods = Food.objects.all()
    context={
        'foods':foods,
    }
    return render(request, 'pages/admbreakfast.html',context )

def edit_admbreakfast(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        form = AddFoodForm(request.POST,request.FILES,instance=foods)
        if form.is_valid():
            form.save()
            return redirect('admbreakfast')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }
    return render(request, 'pages/editfood.html',context)

def delete_admbreakfast(request,uuid):
    foods = Food.objects.get(id=uuid)
    if request.method == 'POST':
        foods.delete()
        return redirect('admbreakfast')
    else:
        form = AddFoodForm(instance=foods)

        
    context={
        'foods':foods,
        'form':form,
    }

    return render(request, 'pages/deletefood.html', context)

##################### End ######################
