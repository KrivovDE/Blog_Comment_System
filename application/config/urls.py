from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .api_routers import router as api_v1_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
