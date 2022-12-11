from django.urls import path
from kitaplar.api import views as api_views

urlpatterns = [
    path('kitaplar/',api_views.KitapListCreatedAPIView.as_view(),name="kitap-listesi"),
]
