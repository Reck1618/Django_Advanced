from django.urls import path, include, re_path
from blog.api.views import PostViewSet, UserDetail, TagViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
import os

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="Api for Blango Blog",
    ),
    url= f"http://localhost:8000/api/v1/",
    public=True,
)

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

