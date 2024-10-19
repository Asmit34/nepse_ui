from django.urls import path
from .views import SignInView, SignUpView, LogoutView, index, profile_view

urlpatterns = [
    path('signin/', SignInView, name='signin'),
    path('signup/', SignUpView, name='signup'),
    path('logout/', LogoutView, name='logout'),
    path('index/', index, name='index'),
    path('profile/<int:user_id>/', profile_view, name='profile_view'),
]
