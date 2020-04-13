from django.urls import path
from .apis import HomeNewsAPIView

urlpatterns = [
    path('news', HomeNewsAPIView.as_view())
]