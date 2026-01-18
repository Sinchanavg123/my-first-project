from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Employee, AuditLog
from .serializers import EmployeeSerializer, AuditLogSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# JWT Authentication Views
from rest_framework_simplejwt.tokens import RefreshToken

# Employee CRUD
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

# Audit Logs
class AuditLogListAPIView(generics.ListAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can view logs

# Analytics
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def analytics_view(request):
    employees = Employee.objects.all()
    total_employees = employees.count()
    departments = employees.values_list('department', flat=True)
    
    # Count per department
    from collections import Counter
    department_counts = Counter(departments)
    
    return Response({
        'total_employees': total_employees,
        'department_counts': department_counts
    })
