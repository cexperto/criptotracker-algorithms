from django.urls import path
from algorithms.views import home, Compound, Nominal
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [    
    path('', home),
    path('compound/', Compound.as_view()),
    path('nominal/', Nominal.as_view()),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
