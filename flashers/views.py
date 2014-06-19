from django.shortcuts import render, get_object_or_404, redirect
from flashers.models import Post
from flashers.forms import CardForm

def index(request):
    last_five = Post.objects.order_by('-created')[:5]
    if request.method == 'POST':
        form = CardForm(request.POST, instance=post)
        if form.is_valid():
            model_instance = form.save()
            return redirect('cards/index.html')
    else:
        form = CardForm()
    return render(request, 'cards/index.html', {'last_five': last_five, 'form': form})


def detail(request, post_id):
    one_card = get_object_or_404(Post, id=post_id)
    return render(request, 'cards/detail.html', {'one_card': one_card})
    '''
    last_five = Post.objects.order_by('-created')[:5]
    post = Post.objects.get(post_id)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('cards/index.html')
    else:
        form = CardForm(instance=post)
    return render(request, 'cards/detail.html', {'last_five': last_five, 'form': form})
    '''
