from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from . import models

admin.site.site_title = "Shivankar Distributors"
admin.site.index_title = "Messy"


class MyAdminSite(admin.AdminSite):
    site_title = "Shivankar Distributors"
    index_title = "Messy"

    site_header = "JASKDLASJD"
    site_url = "/admin"


admin_site = MyAdminSite(name='myadmin')


class KentUserAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">wc</i>'
    search_fields = ('name', 'phone')
    list_filter = ('purchase_date', 'month')
    list_display = ('name', 'phone', 'month')


class TechnicianAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">tag_faces</i>'


class ServiceTaskAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">build</i>'
    raw_id_fields = ('customer',)
    list_display = ('customer', 'technician', 'date_and_time', 'status')


class EmployeeAttendanceForm(forms.ModelForm):
    date = forms.DateField()
    employees = forms.ModelMultipleChoiceField(queryset=models.Employee.objects.all(),
                                               widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = models.EmployeeAttendance
        fields = ('date', 'employees')


class EmployeeAttendanceAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">date_range</i>'
    form = EmployeeAttendanceForm


class EmployeeAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">group</i>'
    list_display = ('name', 'phone')


class PhotoAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">photo</i>'


admin_site.register(models.KentUser, KentUserAdmin)
admin_site.register(models.Technician, TechnicianAdmin)
admin_site.register(models.ServiceTask, ServiceTaskAdmin)
admin_site.register(models.Employee, EmployeeAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(models.Photo, PhotoAdmin)
admin_site.register(models.EmployeeAttendance, EmployeeAttendanceAdmin)
