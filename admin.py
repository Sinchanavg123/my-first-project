from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'department',
        'salary',
        'hire_date',
    )

    list_filter = ('department', 'hire_date')
    search_fields = ('first_name', 'last_name', 'department')
    ordering = ('id',)

