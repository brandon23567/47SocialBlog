from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('article_detail/<str:str>/', views.article_detail, name="article_detail"),
	path('signup/', views.signup, name="signup"),
]