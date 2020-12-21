from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Tu cuenta se ha creado exitosamente! Tu usuario es {username}!')
			login(request, user)
			return redirect('clinica:index')
	else:	
		form = UserRegistrationForm()
	return render(request, 'accounts/register.html', {'form': form})