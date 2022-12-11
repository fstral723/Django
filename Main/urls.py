from django.urls import path
from .import views

app_name = "Main"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('profile/',views.profile, name="profile"),
    path("logout/",views.logout_user, name="logout"),
    path("signin/",views.signin, name="signin"),
    path("signup/",views.signup, name="signup"),
    path("update/",views.update, name ="update"),
    path("delete/",views.delete, name ="delete"),
]
