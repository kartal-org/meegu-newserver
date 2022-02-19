from django.contrib import admin
from django.urls import path, include, re_path

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
    path('api-auth/', include('rest_framework.urls')),

    path("users/", include("accounts.urls", namespace="accounts")),
    path("chats/", include("chats.urls", namespace="chats")),
    path("classrooms/", include("classrooms.urls", namespace="classrooms")),
    path("institutions/", include("institutions.urls", namespace="institutions")),
    path("libraries/", include("library.urls", namespace="library")),
    path("notifications/", include("notification.urls", namespace="notification")),
    path("publications/", include("publication.urls", namespace="publication")),
    path("resources/", include("resources.urls", namespace="resources")),
    path("transactions/", include("transactions.urls", namespace="transactions")),
    path("workspaces/", include("workspaces.urls", namespace="workspaces")),

    re_path('auth/', include('drf_social_oauth2.urls', namespace="drf")),

    # YASG
    path("api/api.json/", schema_view.without_ui(cache_timeout=0),
         name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path("", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
]
