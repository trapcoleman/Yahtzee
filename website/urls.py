from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('player/<int:pk>', views.player_info, name='player'),
    path('add_scorecard/', views.add_scorecard, name='add_scorecard'),
    path('view_scorecard/', views.view_scorecard, name='view_scorecard'),
    # path('delete_scorecard/', views.delete_scorecard, name='delete_scorecard'),
]
