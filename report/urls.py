from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('index/', views.list_page, name='index'),
    path('', views.list_page, name='index'),
    path('list/', views.list_page, name='list'),
    path('<int:pk>/like/', views.add_like, name='like'),
    path('<int:pk>/unlike/', views.add_unlike, name='unlike'),
    path('create/', views.CreateReport.as_view(), name='create'),
    # path('<int:pk>', views.DetailReport.as_view(), name='detail'),
    path('<int:pk>', views.report_detail, name='detail'),
    path('<int:pk>/delete/', views.DeleteReport.as_view(), name='delete'),
    path('<int:pk>/update/', views.UpdateReport.as_view(), name='update'),
]
