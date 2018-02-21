from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('club/', include('club.urls', namespace='club')),
    path('member/', include('member.urls', namespace='member')),
    path('account/', include('account.urls', namespace='account')),
    path('core/', include('core.urls', namespace='core')),
    path('finance/', include('finance.urls', namespace='finance')),
    path('attendance/', include('attendance.urls', namespace='attendance')),
    path('recruiting/', include('recruiting.urls', namespace='recruiting')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
