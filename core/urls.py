from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import settings
from portfolio_app import views

urlpatterns = [
    path('inna_admin_saidkhasayeva/', admin.site.urls),
    path('', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
