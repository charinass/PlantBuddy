from django.urls import path
from PlantBuddy.views import index


urlpatterns = [
    path('', index.as_view(), name='index'),
]