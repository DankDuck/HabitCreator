from django.shortcuts import render, redirect
from .forms import UserRegisterForm
# Create your views here.
def signUp(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "user/signUp.html", {"form": form})