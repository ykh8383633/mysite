from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index') # views에 index를 앱url과 연결
]