from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.models import User

def index(request):
	articles = Article.objects.all().order_by("-date_posted")
	context = {
		'articles': articles
	}
	return render(request, "core/index.html", context)

def article_detail(request, str):
	article = get_object_or_404(Article, slug=str)
	context = {
		'article': article
	}
	return render(request, "core/article_detail.html", context)

def signup(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		confirm_password = request.POST["confirm_password"]

		new_user = User.objects.create_user(username=username, email=email, password=password)
		new_user.save()
		return redirect("index")
	return render(request, "core/signup.html")