from django.urls import path
from .views import *

urlpatterns = [
    path("",UserList.as_view()),
    path("<int:pk>/",UserExtraView.as_view()),
    path("user/",UserCreate.as_view()),
    #path("<int:pk>/update",UserUpdate.as_view()),
]