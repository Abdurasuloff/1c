from django.contrib import admin
from .models import Balance, Item , CheckBalance
from import_export.admin import ImportExportModelAdmin


@admin.register(Balance)
class userdat(ImportExportModelAdmin):
      pass

admin.site.register(Item)
admin.site.register(CheckBalance)

