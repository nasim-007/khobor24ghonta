"""news365 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('politics/', include('politics.urls')),
    path('education/', include('education.urls')),
    path('bangladesh/', include('bangladesh.urls')),
    path('international/', include('international.urls')),
    path('sport/', include('sport.urls')),
    path('travel/', include('travel.urls')),
    path('health/', include('health.urls')),
    path('technology/', include('technology.urls')),
    path('funny/', include('funny.urls')),
    path('fashion/', include('fashion.urls')),
    
    path('summernote/', include('django_summernote.urls')),
    
]


admin.site.site_header = "খবর২৪ঘন্টা এডমিন"
admin.site.site_title = "খবর২৪ঘন্টা এডমিন পোর্টাল"
admin.site.index_title = "স্বাগতম খবর২৪ঘন্টা নিউজপোর্টালে!"

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


