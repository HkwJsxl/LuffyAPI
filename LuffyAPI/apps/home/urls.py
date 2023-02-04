from django.urls import path, re_path

from rest_framework.routers import SimpleRouter

from views import home

router = SimpleRouter()
router.register('banner', home.BannerView)

urlpatterns = [
    path('update_banner/', home.UpdateBanner.as_view())
]

urlpatterns += router.urls
