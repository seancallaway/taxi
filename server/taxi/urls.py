from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from accounts.views import LoginView, SignUpView

urlpatterns = [
    path('api/signup/', SignUpView.as_view(), name='sign_up'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/trip/', include('trips.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
