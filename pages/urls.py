from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainpage),
    path('company/',views.company),
    path('company/history/',views.history),
    path('company/target',views.target),
    path('company/business_area',views.business_area),
    path('company/information',views.information),
]