from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authub/',include('authub.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('dietitians/',include('dietitians.urls')),
    path('reviews/',include('reviews.urls')),
    path('survey/',include('survey.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
