from django.contrib import admin

# Register your models here.
from django.core.checks import messages
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse

from Myemployee.models import Employee_model


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Name', 'Gender', 'Email', 'Age', 'DOJ', 'Salary')
    list_per_page = 5

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Employee_model.objects.update_or_create(
                    Id=fields[0],
                    Name=fields[1],
                    Gender=fields[2],
                    Email=fields[3],
                    Age=fields[4],
                    DOJ=fields[5],
                    Salary=fields[6],

                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


admin.site.register(Employee_model, EmployeeAdmin)
