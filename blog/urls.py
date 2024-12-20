from django.urls import path
from .views import PostModelGetView,PostModelCreateView, CommentModelGetView, CommentModelCreateView

urlpatterns= [
    path("get/",PostModelGetView.as_view()),  
    path('create/',PostModelCreateView.as_view()),
    path("get/<int:pk>/",PostModelGetView.as_view()),
]