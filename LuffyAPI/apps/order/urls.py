from django.urls import path, re_path

from views import order

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('pay', order.OrderPayView)

urlpatterns = [

]

urlpatterns += router.urls
