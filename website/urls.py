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
    path('detail_scorecard/<int:pk>', views.detail_scorecard, name='detail_scorecard'),
    path('delete_scorecard/<int:pk>', views.delete_scorecard, name='delete_scorecard'),
    path('update_scorecard/<int:pk>', views.update_scorecard, name='update_scorecard'),
    path('top_10_scorecards/', views.top_10_scorecards, name='top_10_scorecards'),
]
