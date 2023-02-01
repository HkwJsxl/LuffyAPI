from django.urls import path, re_path

# from .views import account
# from LuffyAPI.apps.views import account

from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('register', views.UserRegisterView)

urlpatterns = [
    # path('login/', account.UserLoginView.as_view(), name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('sms/', views.GetSmsView.as_view(), name='sms'),
]

urlpatterns += router.urls
