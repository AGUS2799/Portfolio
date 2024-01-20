from django.urls import path
from django.conf import settings
from .views import HomeView, contact, ContactView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact-message/', ContactView.as_view(), name='contact-m'),
    path('contact/', contact, name='contact')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)