

from django.urls import path
import apps.admin_suppliers_and_others.views as view

urlpatterns = [
    path('employee_payroll/',view.Employe_payroll_view.as_view()),
    path('employee_payroll_details/<int:id>',view.show_employee_payroll_details,name='payroll')
]
