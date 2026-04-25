

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

# In production on Render, DEBUG=False, so media file URLs are not served automatically.
# If you are using local media uploads, keep this route so /media/ URLs still resolve.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

