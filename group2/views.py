from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from group2.forms import ProfileForm
from group2.models import PartnerFindingProfile


# Create your views here.


def home(request):
    return  render (request , 'group2.html' , {'group_number': '2'})


@login_required
def complete_profile(request):
    try:
        profile = PartnerFindingProfile.objects.get(user=request.user)
        messages.info(request, 'You already have a profile.')
        return redirect('home')
    except PartnerFindingProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # Create profile with current user
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm()

    return render(request, 'group2/complete_profile.html', {'form': form})


@login_required
def search_for_partner(request):
    try:
        profile = PartnerFindingProfile.objects.get(user=request.user)
    except PartnerFindingProfile.DoesNotExist:
        return redirect('complete_profile')

    match_profiles = PartnerFindingProfile.objects.filter(
        learning_goal=profile.learning_goal,
        language_proficiency=profile.language_proficiency,
        appear_in_search=True
    ).exclude(user=request.user)

    match_users = []

    for profile in match_profiles:
        match_users.append(profile.user.username)

    return render(request, 'group2/search.html', {
        'match_profiles': match_users,
        'user_profile': profile
    })







