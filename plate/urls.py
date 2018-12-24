from django.urls import path
from . import views

app_name = 'plate'

urlpatterns = [
    # path('/?$', views.PlateDetail.as_view(), name='search'),
    path('', views.findPlate, name='search'),
    path('<int:pk>', views.loadPlatePage, name='detail'),
]
