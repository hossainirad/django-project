from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about/', views.about, name="about"),
    # path('', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
