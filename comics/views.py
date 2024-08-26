from django.shortcuts import render, redirect
from .models import Comic
from .forms import ComicForm, ComicImageForm
from django.contrib.auth.decorators import login_required


@login_required
def create_comic(request):
    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES)
        if form.is_valid():
            comic = form.save(commit=False)
            comic.user = request.user
            comic.save()
            return redirect('view_comics')
    else:
        form = ComicForm()
    return render(request, 'comics/create_comic.html', {'form': form})


@login_required
def view_comics(request):
    comics = Comic.objects.filter(user=request.user)
    return render(request, 'comics/view_comics.html', {'comics': comics})


@login_required
def detail_comics(request):
    comics = Comic.objects.filter(user=request.user)

