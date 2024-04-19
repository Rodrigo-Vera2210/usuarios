from django.urls import path, include
from .views import *

urlpatterns = [
    path('crear/',UserAPI.as_view()),
    path('lista/',UserListAPI.as_view(),name="lista"),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout')
]
