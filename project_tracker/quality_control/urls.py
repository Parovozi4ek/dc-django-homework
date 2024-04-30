from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),

    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('bugs/new/', views.create_bug_report, name='create_bug_report'),
    path('features/new/', views.create_feature_request, name='create_feature_request'),
    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),

    # path('bugs/', views.BugListView.as_view(), name='bug_list'),
    # path('features/', views.FeatureListView.as_view(), name='feature_list'),
    # path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    # path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    # path('bugs/new/', views.BugReportCreateView.as_view(), name='create_bug_report'),
    # path('features/new/', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),
    # path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug'),
    # path('bugs/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature'),
    # path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),
    # path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),
]
