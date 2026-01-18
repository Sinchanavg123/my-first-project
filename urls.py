from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from employee_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Employee Management
    path('', views.index, name='dashboard'),
    path('add/', views.add_employee, name='add_employee'),
    path('remove/<int:emp_id>/', views.remove_employee, name='remove_employee'),
    path('edit/<int:emp_id>/', views.edit_employee, name='edit_employee'),
    path('filter/', views.filter_employee, name='filter_employee'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='employee_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Secure logout redirect
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
