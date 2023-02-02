from django.urls import path, re_path

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('banner', views.BannerView)

urlpatterns = [
    path('update_banner/', views.UpdateBanner.as_view())
]

urlpatterns += router.urls
