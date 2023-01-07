from django.urls import path
from . import views
urlpatterns = [
    path('',views.TaskListCreateView.as_view()),
    path('<int:id>/',views.TaskUpdateView.as_view()),
]