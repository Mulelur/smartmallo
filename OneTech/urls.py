
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from categories.views import search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
    path('categories/', include('categories.urls')),
    path('test/', include('asset.urls')),
    path('account/', include('account.urls')),
    path('help/', include('help.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('article/', include('article.urls')),
    path('search/', search, name='search')
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)