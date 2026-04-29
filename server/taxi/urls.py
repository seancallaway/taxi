from django.contrib import admin
from django.urls import path

from accounts.views import LoginView, SignUpView

urlpatterns = [
    path('api/signup/', SignUpView.as_view(), name='sign_up'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
