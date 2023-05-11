from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from web.views import SitemapView


sitemaps = {
    'static': SitemapView,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots_file')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler500 = 'web.views.server_error'
# handler404 = 'web.views.page_not_found'
# handler400 = 'web.views.bad_request'
# handler403 = 'web.views.permission_denied'
