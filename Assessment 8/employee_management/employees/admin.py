from django.contrib import admin


from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'f_name', 'l_name', 'company_name', 'email')
    search_fields = ('f_name', 'l_name', 'employee_id')
    list_filter = ('company_name', 'designation')