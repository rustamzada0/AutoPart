from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import sign_in

app_name = 'accounts'

urlpatterns = [
    path('login/', sign_in, name='login'),
]