from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from man_shop.views import cloth_detail_view


urlpatterns = (
        [

            path('admin/', admin.site.urls),
            path('', include("user.urls")),
            path('', include('man_shop.urls')),
            path('', include('parser_app.urls')),
            path('book', include('book.urls')),
            path('', include('user.urls')),
            path('cloth/<int:cloth_id>/', cloth_detail_view, name='cloth_detail')
        ]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
