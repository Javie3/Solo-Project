from django.shortcuts import render, redirect
from .models import *
from .forms import ListForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item Has Been Added To List'))
        return render(request, "index.html",{'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, "index.html", {'all_items': all_items})


def delete(request, id):
    destroyed = List.objects.get(id=id)
    destroyed.delete()
    messages.success(request, ('Item Has Been Deleted!!'))
    return redirect('/')   


def cross_off(request, id):
    item = List.objects.get(id=id)
    item.completed = True
    item.save()
    return redirect('/')

def uncross(request, id):
    item = List.objects.get(id=id)
    item.completed = False
    item.save()
    return redirect('/')


def edit(request, id):
    if request.method == 'POST':
     item = List.objects.get(id=id)

     form = ListForm(request.POST or None, instance=item)

     if form.is_valid():
        form.save()
        messages.success(request, ('Item Has Been Edited!'))
        return redirect('/')

    else:
        item = List.objects.get(id=id)
        return render(request, "edit.html", {'item':item})            
