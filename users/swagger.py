from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Referral System API Task",
        default_version='v1',
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="afrinshdiih52@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)