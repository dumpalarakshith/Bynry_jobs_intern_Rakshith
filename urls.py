from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gas/', include('gas_management.urls')),  # Make sure this is correct
]
