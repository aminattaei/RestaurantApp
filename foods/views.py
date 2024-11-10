from django.shortcuts import render
from .models import Food


def food_list(request):
    foodList = Food.objects.all()
    context = {
        "foodList": foodList
    }
    return render(request, "foods/index.html", context=context)


def food_detail(request,pk):
    food=Food.objects.get(pk=pk)
    context={
        'food':food
    }
    return render(request,'foods/foodsDetail.html',context=context)


