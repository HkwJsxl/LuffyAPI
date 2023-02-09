from django.urls import path, re_path

from views import account

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('register', account.UserRegisterView)

urlpatterns = [
    path('login/', account.UserLoginView.as_view(), name='login'),
    path('sms/', account.GetSmsView.as_view(), name='sms'),
    path('register/email/', account.VerifyEmailView.as_view(), name='email'),
]

urlpatterns += router.urls
