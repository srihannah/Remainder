from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm, CustomUserCreationForm  # Import both forms

@login_required
def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'datas': users})  # Ensure correct context name

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Interview Added')
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'adduser.html', {'form': form})

def update_user(request, id):
    user = get_object_or_404(User, pk=id)  # Get the user by ID or return 404
    
    if request.method == "POST":
        # Retrieve form data
        user.Company_Name = request.POST.get("Company_Name")
        user.Job_Role = request.POST.get("Job_Role")
        user.DateofInterview = request.POST.get("DateofInterview")
        user.TimeofInterview = request.POST.get("TimeofInterview")
        user.Address = request.POST.get("Address")

        # Save updated user data
        user.save()

        messages.success(request, "User details updated successfully!")
        return redirect("home")  # Redirect to the home page after updating

    return render(request, "updateuser.html", {"data": user})

def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.success(request, 'Interview Record Deleted')
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, "register.html", {"form": form})
