from django.urls import path;
import core.views;

urlpatterns = [
    path('', core.views.index),
    path('persons/', core.views.allPersons),
    path('persons/<int:id>/', core.views.person),
]