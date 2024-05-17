from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include('products.urls')),
   path('api/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('', RedirectView.as_view(url='api/v1/')),
    

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)