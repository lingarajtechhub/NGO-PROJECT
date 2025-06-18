from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import WidowProfile
from .forms import WidowProfileForm

# Public profile creation view (no authentication required)
def public_profile_create(request):
    if request.method == 'POST':
        form = WidowProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile submitted successfully!')
            return redirect('public_profile_create')
        else:
            print("Form errors:", form.errors)  # Debug
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WidowProfileForm()
    return render(request, 'profiles/profile_form.html', {'form': form})

# Admin sign-in view
def admin_signin(request):
    if request.user.is_authenticated:
        return redirect('profile_list')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully signed in.")
            return redirect('profile_list')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'profiles/admin_signin.html')

# Admin sign-up view
def admin_signup(request):
    if request.user.is_authenticated:
        return redirect('profile_list')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('admin_signin')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('admin_signin')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('admin_signin')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please sign in.")
        return redirect('admin_signin')
    return render(request, 'profiles/admin_signin.html')

# Logout view
def signout(request):
    logout(request)
    return redirect('admin_signin')

# Admin profile views, protected with @login_required
@login_required
def profile_list(request):
    query = request.GET.get('q', '')
    action = request.GET.get('action', '')  # Extract the 'action' parameter
    if query:
        profiles = WidowProfile.objects.filter(
            Q(name__icontains=query) | Q(registration_number__icontains=query)
        )
    else:
        profiles = WidowProfile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles, 'query': query, 'action': action})

@login_required
def profile_create(request):
    if request.method == 'POST':
        form = WidowProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile added successfully!')
            return redirect('profile_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WidowProfileForm()
    return render(request, 'profiles/profile_form.html', {'form': form})

@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(WidowProfile, pk=pk)
    if request.method == 'POST':
        form = WidowProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WidowProfileForm(instance=profile)
    return render(request, 'profiles/profile_form.html', {'form': form})

@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(WidowProfile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('profile_list')
    return render(request, 'profiles/profile_confirm_delete.html', {'profile': profile})

@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(WidowProfile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})

@login_required
def profile_print(request, pk):
    profile = get_object_or_404(WidowProfile, pk=pk)
    return render(request, 'profiles/profile_print.html', {'profile': profile})

@login_required
def print_empty_profile(request):
    """
    View to render and print an empty Widow/Widower Profile form.
    """
    # Create an empty WidowProfile instance
    empty_profile = WidowProfile()
    
    # Render the profile_print.html template with the empty profile
    context = {
        'profile': empty_profile,
        'title': 'Empty Widow/Widower Profile Form',
    }
    return render(request, 'profile_print_empty.html', context)