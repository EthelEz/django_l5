from django.conf.urls import url
from cbv_app import views
from django.urls import path

app_name = 'cbv_app'         #The app_name is set such that the navigation in template could be clearly set and inheritted

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),                   #we chose SchoolListView as view bc its a class based view
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
]
