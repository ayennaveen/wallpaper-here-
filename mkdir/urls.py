from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView # Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Prefix backend routes with 'api/' to avoid conflicts with React
    path('api/', include('main.urls')), 
]

# Serve uploaded media files from MEDIA_ROOT at /media/.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Catch-all route to serve the React index.html
# MUST be the last route in the file!
urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]