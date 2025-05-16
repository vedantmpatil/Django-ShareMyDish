from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.
def explore(request):
    items = Item.objects.all().order_by('-id')  # latest first
    return render(request, 'dish/explore.html', {'items': items})

def recipes(request):
    items = Item.objects.all().order_by('-id')  # latest first
    return render(request, 'dish/recipes.html', {'items': items})

def recipe_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'dish/recipe_detail.html', {'item': item})

def add_recipe(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish:explore')  # or 'all_recipes'
    else:
        form = ItemForm()
    return render(request, 'dish/add_recipe.html', {'form': form})

def update_recipe(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('dish:recipe_detail', pk=item.pk)
    return render(request, 'dish/update_recipe.html', {'form': form, 'item': item})


def delete_recipe(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dish:all_recipes')
    return render(request, 'dish/delete_recipe.html', {'item': item})

def about(request):
    return render(request, 'dish/about.html')
