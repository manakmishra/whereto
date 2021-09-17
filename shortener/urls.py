from django.urls import path
from shortener import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="home"),
    path('/shorten',views.shorten, name="shorten"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)