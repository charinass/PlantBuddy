from django.urls import path
from PlantBuddy.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
