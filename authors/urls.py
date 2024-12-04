from django.urls import path
from authors import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.AuthorRegisterView.as_view(), name='register'),
    path('login/', views.AuthorLoginView.as_view(), name='login'),
    path('logout/', views.AuthorLogoutView.as_view(), name='logout'),
]
