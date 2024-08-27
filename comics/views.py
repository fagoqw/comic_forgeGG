from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comic, Comment, Tag, ComicImage
from .forms import ComicForm, ComicImageForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count



@login_required
def create_comic(request):
    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES)
        if form.is_valid():
            comic = form.save(commit=False)
            comic.user = request.user
            comic.save()
            return redirect('upload_images', comic_id=comic.id)
    else:
        form = ComicForm()
    return render(request, 'comics/create_comic.html', {'form': form})


@login_required
def upload_images(request, comic_id):
    comic = get_object_or_404(Comic, id=comic_id)

    if request.method == 'POST':
        if 'upload_image' in request.POST:
            form = ComicImageForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.save(commit=False)
                image.comic = comic
                image.save()
        elif 'delete_image' in request.POST:
            image_id = request.POST.get('image_id')
            image = get_object_or_404(ComicImage, id=image_id)
            image.delete()
        elif 'order_images' in request.POST:
            for index, image_id in enumerate(request.POST.getlist('image_ids')):
                image = get_object_or_404(ComicImage, id=image_id)
                image.order = index
                image.save()

        return redirect('upload_images', comic_id=comic.id)

    form = ComicImageForm()
    images = comic.images.all().order_by('order')
    return render(request, 'comics/upload_images.html', {'form': form, 'comic': comic, 'images': images})


@login_required
def detail_comic(request, comic_id):
    comic = get_object_or_404(Comic, id=comic_id)

    if request.method == 'POST':
        if 'like_comic' in request.POST:
            comic.likes += 1
            comic.save()
            return redirect('detail_comic', comic_id=comic.id)
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.comic = comic
                comment.user = request.user
                comment.save()
                return redirect('detail_comic', comic_id=comic.id)
    else:
        comment_form = CommentForm()

    if not request.session.get(f'viewed_comic_{comic_id}', False):
        comic.views += 1
        comic.save()
        request.session[f'viewed_comic_{comic_id}'] = True

    comments = comic.comments.all()
    return render(request, 'comics/detail_comic.html',
                  {'comic': comic, 'comments': comments, 'comment_form': comment_form})


@login_required
def view_comics(request):
    comics = Comic.objects.filter(user=request.user)
    return render(request, 'comics/view_comics.html', {'comics': comics})


def home(request):
    popular_comics = Comic.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:10]
    return render(request, 'comics/home.html', {'popular_comics': popular_comics})


def search_comics(request):
    query = request.GET.get('q', '')
    comics = Comic.objects.all()

    if query:
        comics = comics.filter(
            title__icontains=query
        )

        comics = comics.filter(author__username__icontains=query).distinct()

    return render(request, 'comics/search_results.html', {'comics': comics, 'query': query})


@login_required
def delete_comic(request, comic_id):
    comic = get_object_or_404(Comic, id=comic_id)
    if comic.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this comic.")
    comic.delete()
    return redirect('view_comics')


