"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from rest_framework_nested import routers
from django.conf.urls import include

from accounts.views import (UserProfileViewSet, LoginViewSet, LogoutViewSet)
from payments.views import (PaymentsViewSet, AgreementsViewSet)


router =  routers.DefaultRouter()
router.register('profile', UserProfileViewSet, base_name='profile')
router.register('login', LoginViewSet, base_name='login')
router.register('logout', LogoutViewSet, base_name='logout')
router.register('agreements', AgreementsViewSet, base_name='agreements')

payments_router = routers.NestedSimpleRouter(router, r'agreements', lookup='agreement')
payments_router.register('payments', PaymentsViewSet, base_name='payments')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/v2/', include(router.urls)),
    url(r'api/v2/', include(payments_router.urls))
]
