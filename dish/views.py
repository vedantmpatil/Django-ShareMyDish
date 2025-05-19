from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Home/Explore view
def explore(request):
    items = Item.objects.all().order_by('-id')  # latest first
    return render(request, 'dish/explore.html', {'items': items})

# List all recipes
def recipes(request):
    items = Item.objects.all().order_by('-id')
    return render(request, 'dish/recipes.html', {'items': items})

# Single recipe detail
def recipe_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'dish/recipe_detail.html', {'item': item})

# Add a recipe (only for logged-in users)
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user  # Automatically associate with current user
            item.save()
            return redirect('dish:explore')
    else:
        form = ItemForm()
    return render(request, 'dish/add_recipe.html', {'form': form})

# Update a recipe (only by the user who created it)
@login_required
def update_recipe(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if item.created_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this recipe.")

    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('dish:recipe_detail', pk=item.pk)
    return render(request, 'dish/update_recipe.html', {'form': form, 'item': item})

# Delete a recipe (only by the user who created it)
@login_required
def delete_recipe(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if item.created_by != request.user:
        return HttpResponseForbidden("You are not allowed to delete this recipe.")

    if request.method == 'POST':
        item.delete()
        return redirect('dish:recipes')
    return render(request, 'dish/delete_recipe.html', {'item': item})

# About page
def about(request):
    return render(request, 'dish/about.html')
