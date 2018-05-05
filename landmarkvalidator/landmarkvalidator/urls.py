from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('calc/', include('calc.urls')),
    path('admin/', admin.site.urls),
]
