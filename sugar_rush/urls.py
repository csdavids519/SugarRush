from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('checkout/', include('checkout.urls')),
    path('products/', include('products.urls')),
    path('profiles/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'sugar_rush.views.handler404'
handler500 = 'sugar_rush.views.handler500'