from django.contrib import admin
from django.urls import path

from accounts.views import SignUpView

urlpatterns = [
    path('api/signup/', SignUpView.as_view(), name='sign_up'),
    path('admin/', admin.site.urls),
]
