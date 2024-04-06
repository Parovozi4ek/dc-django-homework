from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bug_list, name='bug_list'),
    path('feature_list/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail),
    path('feature_list/<int:feature_id>/', views.feature_id_detail),
]
