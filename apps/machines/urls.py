from django.urls import include, path
from . import views

app_name = 'machines'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('', views.IndexView.as_view(), name='index'),
	
]