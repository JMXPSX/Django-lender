from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="" ),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    path('dashboard', views.dashboard, name="dashboard"),
    path('lender-entry', views.lender_entry, name="lender-entry"),
    path('lender-results', views.lender_results, name="lender-results"),
]