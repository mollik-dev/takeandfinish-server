from django.urls import path
from . import views

urlpatterns = [
	path('', views.main_page, name='index'),
	path('view_level/lvl<int:id>', views.view_level, name='view_lvl'),
	path('login/', views.login_page, name='login'),
	path('register/', views.register_page, name='register'),
]