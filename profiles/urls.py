from django.urls import path
from profiles import views


urlpatters = [
    path('profiles/', views.ProfileList.as_view())
]