from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('user-profile/<str:pk>', views.userProfile, name="user-profile"),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),

    path('add-skill/', views.createSkill, name="add-skill"),
    path('edit-skill/<str:pk>', views.updateSkill, name="edit-skill"),
    path('delete-skill/<str:pk>', views.deleteSkill, name="delete-skill"),
]