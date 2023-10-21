"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from library.views import AuthorModelViewSet, BookModelViewSet
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, License, Contact
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    Info(
        title='Library',
        default_version='1.0',
        description='description',
        license=License(name='MIT'),
        contact=Contact(email='test@yandex.ru')
    )
)

router = DefaultRouter()
router.register('authors', AuthorModelViewSet, basename='authors')
router.register('books', BookModelViewSet, basename='books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('swagger', schema_view.with_ui()),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
]
