from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Add this import
from django.conf.urls.static import static
from django.shortcuts import render
from upload_notes import views  # Import views from the correct app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('to_do_list/', include('to_do_list.urls')),
    path('upload_notes/', views.upload_notes, name='upload_notes'),  # Use the correct view here
    path('', lambda request: render(request, 'blog/index.html'), name='home'),  # Directly render index.html
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)