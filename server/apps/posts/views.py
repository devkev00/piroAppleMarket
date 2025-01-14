from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def main(request):
    posts = Post.objects.all()

    search_txt = request.GET.get("search_txt")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if search_txt:
      posts = Post.objects.filter(title__contains=search_txt)

    if min_price or max_price: # 최소 / 최대 가격 중 하나만 쿼리에 담기는 경우
      try: 
        if min_price:
          min_price = int(min_price)
          posts = posts.filter(price__gte=min_price)
        if max_price:
          max_price = int(max_price)
          posts = posts.filter(price__lte=max_price)
      except:
        posts = Post.objects.all()
        
    ctx = {
      'posts': posts,
      'search_txt': search_txt,
      'min_price': min_price,
      'max_price': max_price,
    }

    return render(request, 'posts/list.html', context=ctx)


def create(request):
  if request.method == 'GET':
    form = PostForm()
    ctx = {'form': form}
    return render(request, 'posts/create.html', context = ctx)    
  else:
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()      
    return redirect('/')
  

def detail(request, pk):
  target_post = Post.objects.get(id = pk)
  ctx = {'post' : target_post,}
  return render(request, 'posts/detail.html', context=ctx)
  
  
def update(request, pk):
  if request.method == 'GET':
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)    
    ctx = {'form': form,
           'pk': pk}  
    
    return render(request, 'posts/update.html', context=ctx)
  else:
    post = Post.objects.get(id=pk)
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():      
      form.save()
    return redirect(f'/posts/detail/{pk}', pk)
  
  
def delete(request, pk):
  post = Post.objects.get(id=pk)
  post.delete()
  return redirect('/')