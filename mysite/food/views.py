from django.shortcuts import render, HttpResponse, redirect
from django.template import loader

from .models import *
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('index.html')
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse('This is items menu.')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'item_form.html', {'form': form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'item_form.html', {'form':form, 'item':item})


def delete_item(request, id):
    item = Item.objects.get(id=id)
    # if request.method == 'POST':
    item.delete()
    return redirect('food:index')
    
    # return render(request, 'item_delete.html', {'item' : item})