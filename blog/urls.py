from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='blog'
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)