from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from comics.models import Comic
from .models import UserProfile


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    comics = Comic.objects.filter(user=user)

    return render(request, 'users/profile.html', {'profile': profile, 'comics': comics})



@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user)

    user_profile = get_object_or_404(UserProfile, user=user_to_follow)

    request.user.profile.follows.add(user_profile)
    return redirect('profile', username=username)


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user_to_unfollow)
    request.user.profile.follows.remove(user_profile)
    return redirect('profile', username=username)
