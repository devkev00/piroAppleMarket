from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.

def list(request):
  users = User.objects.all()

  ctx = {
    'users': users
  }
  return render(request, 'users/list.html', ctx)

def create(request):
  if request.method == 'GET':
    form = UserForm()

    ctx = {
      'form':form
    }

    return render(request, 'users/create.html', ctx)
  
  form = UserForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('users:list')

def delete(request, pk):
  User.objects.get(id=pk).delete()
  return redirect('users:list')

def update(request, pk):
  user = User.objects.get(id=pk)
  if request.method == 'GET':
    form = UserForm(instance=user)

    ctx = {
      'form': form,
      'pk': pk,
    }

    return render(request, 'users/update.html', ctx)
  
  form = UserForm(request.POST, instance=user)
  if form.is_valid():
    form.save()
  return redirect('users:list')