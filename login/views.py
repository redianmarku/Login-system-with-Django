import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from .forms import Register, Login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Post



def home(request):
	posts = Post.objects.all().order_by('-date')

	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		user = request.user
		date = datetime.datetime.now()
		new_post = Post(title=title, content=content, author=user, date=date)
		new_post.save()
		return redirect('home')

	context = {
		'posts':posts
	}

	return render(request, 'login/home.html', context)

def register(request):
	if request.method == 'POST':
		form = Register(request.POST)
		if form.is_valid():
			form.save()
			userData = form.cleaned_data
			user = authenticate(username=userData['username'],password=userData['password1'])
			auth.login(request, user)
			return redirect('home')
	else:
		form = Register()

	return render(request, 'login/index.html', {'form':form})


def login(request):
	form = Login()
	context = {
		'form':form
	}
	if request.method == 'POST':
		form = Login(request.POST)
		if form.is_valid():
			userData = form.cleaned_data
			user = authenticate(request, username=userData['username'], password=userData['password'])
			if user is not None:
				auth.login(request, user)
				return redirect('home')
			else:
				messages.error(request, f'Incorrect username or password!')
				return redirect('login')
	else:
		form = Login()
	return render(request, 'login/login.html', context)


@login_required
def delete(request, post_id):
	Post.objects.get(id=post_id).delete()
	messages.success(request, f'Post deleted successful.')
	return redirect('home')

@login_required
def logout(request):
	auth.logout(request)
	return redirect('login')


@login_required
def profile(request):
	return render(request, 'login/profile.html')