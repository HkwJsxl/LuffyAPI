from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),

    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('home/', include(('home.urls', 'home'), namespace='home')),
    path('course/', include(('course.urls', 'course'), namespace='course')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
]
