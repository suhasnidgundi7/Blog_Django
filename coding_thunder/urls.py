from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Admin Panel'                    
admin.site.index_title = 'Welcome to Coding Thunder'                 
admin.site.site_title = 'By Suhas Nidgundi'