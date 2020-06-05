from django.urls import path
from . import views
urlpatterns=[
 path('',views.home),
 path('hey',views.hello),
 path('gender',views.genderapi)
]