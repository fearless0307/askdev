from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from users import views_ck as views

urlpatterns = [
    # apps urls
    path('', include('questions.urls')),
    path('', include('stories.urls')),
    path('', include('users.urls')),

    # api urls
    path('api/', include('questions.urls_api')),
    path('api/', include('stories.urls_api')),
    path('api/', include('users.urls_api')),

    path('ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),

    # path('ckeditor/', include('ckeditor_uploader.urls')),

    # users urls
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns +=\
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
