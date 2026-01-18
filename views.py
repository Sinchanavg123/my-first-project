
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Avg
from .models import Employee, AuditLog

# Role check
def is_admin(user):
    return user.is_staff  # Or user.groups.filter(name='Admin').exists()


@login_required
def index(request):
    
    employees = Employee.objects.all()

    # Chart data
    department_data = employees.values('department').annotate(count=Count('id')).order_by('department')
    labels = [entry['department'] for entry in department_data]
    data = [entry['count'] for entry in department_data]

    # Average salary
    avg_salary = employees.aggregate(Avg('salary'))['salary__avg'] or 0

    # Notifications (latest 5 actions)
    notifications = AuditLog.objects.order_by('-timestamp')[:5]

    context = {
        'employees': employees,
        'total_employees': employees.count(),
        'total_departments': employees.values('department').distinct().count(),
        'average_salary': avg_salary,
        'labels': labels,
        'data': data,
        'notifications': notifications,
    }
    return render(request, 'employee_app/index.html', context)



@login_required
@user_passes_test(is_admin)
def add_employee(request):
    if request.method == "POST":
        emp = Employee.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            department=request.POST['department'],
            salary=request.POST['salary'],
        )
        # Log action
        AuditLog.objects.create(user=request.user, action=f"Added employee {emp.first_name} {emp.last_name}")
        return redirect('/')
    return render(request, 'employee_app/add_employee.html')


@login_required
def edit_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    if request.method == "POST":
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.save()

        AuditLog.objects.create(user=request.user, action=f"Edited employee {employee.first_name} {employee.last_name}")
        return redirect('/')
    return render(request, 'employee_app/edit_employee.html', {'employee': employee})


@login_required
@user_passes_test(is_admin)
def remove_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    AuditLog.objects.create(user=request.user, action=f"Deleted employee {employee.first_name} {employee.last_name}")
    employee.delete()
    return redirect('/')


@login_required
def filter_employee(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        department = request.POST.get('department')
        if name:
            employees = employees.filter(first_name__icontains=name)
        if department:
            employees = employees.filter(department__icontains=department)
    return render(request, 'employee_app/filter_employee.html', {'employees': employees})
