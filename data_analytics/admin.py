from django.contrib import admin
from . models import Data
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Data)
class DataAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','first_name','last_name','location','age','salary']

