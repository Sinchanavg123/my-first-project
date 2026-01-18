from django.urls import path
from .api_views import (
    EmployeeListCreateAPIView,
    EmployeeRetrieveUpdateDestroyAPIView,
    AuditLogListAPIView,
    analytics_view
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee_list_create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee_detail'),

    path('audit-logs/', AuditLogListAPIView.as_view(), name='audit_logs'),

    path('analytics/', analytics_view, name='analytics'),
]
