from django.contrib import admin
from django.urls import path
from MyEngineNgeSearch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myenginengesearch/', views.index),
    path('myenginengesearch/result/', views.result),
    path('myenginengesearch/result/<str:doc_name>/', views.download),
    path('pagination/', views.pagination),
]
